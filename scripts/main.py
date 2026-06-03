import argparse
import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from html import unescape

# Your Google Scholar user ID
scholar_id = 'ngEXyLkAAAAJ'

# The path to save the badge
output_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'scholar_badge.svg')

def fetch_scholar_profile(scholar_id):
    """Fetches the Google Scholar profile page."""
    url = f'https://scholar.google.com/citations?user={scholar_id}&hl=en&pagesize=100'
    request = urllib.request.Request(
        url,
        headers={
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/125.0.0.0 Safari/537.36'
            )
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode('utf-8', errors='replace')


def parse_total_citations(html):
    """Extracts the total profile citation count."""
    match = re.search(r'Cited by\s+([0-9,]+)', html)
    if not match:
        raise ValueError('Could not find citation count in Scholar profile')
    return int(match.group(1).replace(',', ''))


def parse_publications(html):
    """Extracts paper citation counts keyed by Scholar paper ID."""
    publications = {}
    row_pattern = re.compile(r'<tr class="gsc_a_tr">(.*?)</tr>', re.DOTALL)
    for row in row_pattern.findall(html):
        id_match = re.search(r'citation_for_view=([^"&]+)', row)
        title_match = re.search(r'class="gsc_a_at"[^>]*>(.*?)</a>', row, re.DOTALL)
        cite_match = re.search(r'class="gsc_a_ac[^"]*"[^>]*>([0-9,]*)</a>', row)
        if not id_match or not title_match:
            continue

        paper_id = unescape(id_match.group(1))
        title = re.sub(r'<[^>]+>', '', title_match.group(1))
        title = unescape(title).strip()
        citations = int(cite_match.group(1).replace(',', '')) if cite_match and cite_match.group(1) else 0
        publications[paper_id] = {
            'title': title,
            'num_citations': citations,
        }
    return publications


def get_scholar_stats(scholar_id):
    """Fetches total and per-publication citation stats."""
    try:
        html = fetch_scholar_profile(scholar_id)
        return {
            'citedby': parse_total_citations(html),
            'updated': datetime.now(timezone.utc).isoformat(),
            'publications': parse_publications(html),
        }
    except Exception as e:
        print(f"Error fetching Scholar stats: {e}")
        return None

def create_badge(citations):
    """Creates a badge with the given number of citations."""
    label = 'Citations'
    value = str(citations)
    label_width = 63
    value_width = max(29, len(value) * 7 + 10)
    total_width = label_width + value_width
    label_center = label_width / 2
    value_center = label_width + (value_width / 2)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20">
    <linearGradient id="b" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <mask id="scholar_badge">
        <rect width="{total_width}" height="20" rx="3" fill="#fff"/>
    </mask>
    <g mask="url(#scholar_badge)">
        <path fill="#555" d="M0 0h{label_width}v20H0z"/>
        <path fill="#1E90FF" d="M{label_width} 0h{value_width}v20H{label_width}z"/>
        <path fill="url(#b)" d="M0 0h{total_width}v20H0z"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
        <text x="{label_center + 1:.1f}" y="15" fill="#010101" fill-opacity=".3">{label}</text>
        <text x="{label_center:.1f}" y="14">{label}</text>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
        <text x="{value_center + 1:.1f}" y="15" fill="#010101" fill-opacity=".3">{value}</text>
        <text x="{value_center:.1f}" y="14">{value}</text>
    </g>
</svg>
'''
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as badge:
        badge.write(svg)
    print(f"Badge created at {output_path} with {citations} citations.")


def write_stats(stats, stats_output_path):
    """Writes Scholar stats JSON for the homepage citation widgets."""
    os.makedirs(os.path.dirname(os.path.abspath(stats_output_path)), exist_ok=True)
    with open(stats_output_path, 'w', encoding='utf-8') as stats_file:
        json.dump(stats, stats_file, ensure_ascii=False, indent=2)
        stats_file.write('\n')
    print(f"Scholar stats written to {stats_output_path}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update Google Scholar citation assets.')
    parser.add_argument('--stats-output', default='gs_data.json')
    args = parser.parse_args()

    stats = get_scholar_stats(scholar_id)
    if stats is not None:
        create_badge(stats['citedby'])
        write_stats(stats, args.stats_output)
    else:
        print("Failed to fetch Scholar stats. Citation assets will not be updated.")

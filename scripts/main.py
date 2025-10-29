import requests
from bs4 import BeautifulSoup
import anybadge
import os

# The URL of your Google Scholar profile
url = 'https://scholar.google.com/citations?user=ngEXyLkAAAAJ&hl=en&authuser=1'

# The path to save the badge
output_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'scholar_badge.svg')

def get_scholar_citations(url):
    """Fetches the total number of citations from a Google Scholar profile."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep-alive',
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table with citation metrics
        stats_table = soup.find('table', {'id': 'gsc_rsb_st'})
        if not stats_table:
            print("Could not find the stats table.")
            return None

        # The total citations count is in the second row, first data cell
        total_citations = stats_table.find_all('td')[1].text
        return int(total_citations)
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except (IndexError, ValueError) as e:
        print(f"Error parsing citation count: {e}")
        return None

def create_badge(citations):
    """Creates a badge with the given number of citations."""
    if citations is None:
        citations = 'N/A'

    badge = anybadge.Badge(
        label='Citations',
        value=str(citations),
        default_color='dodgerblue'
    )
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    badge.write_badge(output_path, overwrite=True)
    print(f"Badge created at {output_path} with {citations} citations.")

if __name__ == "__main__":
    citations = get_scholar_citations(url)
    create_badge(citations)

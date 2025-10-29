import requests
from bs4 import BeautifulSoup
import anybadge
import anybadge
import os
from scholarly import scholarly

# The user ID of your Google Scholar profile
user_id = 'ngEXyLkAAAAJ'

# The path to save the badge
output_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'scholar_badge.svg')

def get_scholar_citations(user_id):
    """Fetches the total number of citations from a Google Scholar profile."""
    try:
        # Search for the author by user ID
        author = scholarly.search_author_id(user_id)
        # Fetch the author's full profile
        author = scholarly.fill(author, sections=['basics', 'indices'])
        # Get the total number of citations
        return author['citedby']
    except Exception as e:
        print(f"Error fetching citations: {e}")
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
    citations = get_scholar_citations(user_id)
    create_badge(citations)

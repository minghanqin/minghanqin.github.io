from scholarly import scholarly
import anybadge
import os

# Your Google Scholar user ID
scholar_id = 'ngEXyLkAAAAJ'

# The path to save the badge
output_path = os.path.join(os.path.dirname(__file__), '..', 'img', 'scholar_badge.svg')

def get_scholar_citations(scholar_id):
    """Fetches the total number of citations for a Google Scholar user."""
    try:
        # Search for the author by their Scholar ID
        author = scholarly.search_author_id(scholar_id)
        # Fill the author's details
        author = scholarly.fill(author, sections=['basics'])
        # Return the total number of citations
        return author['citedby']
    except Exception as e:
        print(f"Error fetching citations with scholarly: {e}")
        return None

def create_badge(citations):
    """Creates a badge with the given number of citations."""
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
    citations = get_scholar_citations(scholar_id)
    if citations is not None:
        create_badge(citations)
    else:
        print("Failed to fetch citations. The badge will not be updated.")

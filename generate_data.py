import os
from textwrap import dedent
from supabase import create_client, Client

# --- Configuration from Environment Variables (set by GitHub Actions) ---
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_SERVICE_ROLE_KEY = os.environ.get('SUPABASE_SERVICE_ROLE_KEY')

# Define the path where the generated Markdown file will be saved within your docs/ directory
OUTPUT_MD_FILE = 'docs/signatories.md'
TARGET_TABLE = 'signatories'

def fetch_public_submissions():
    """Fetches public submissions directly from Supabase using the service_role key."""
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise ValueError("Supabase URL or Service Role Key environment variables are not set.")

    # Initialize Supabase client with the service_role key
    # This client bypasses RLS
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

    try:
        # Directly query the 'submissions' table
        # We explicitly select only 'name' and 'affiliation'
        # And filter for 'is_private = false'
        response = supabase.table(TARGET_TABLE) \
                           .select('first_name, last_name, affiliation, show_name', count = "exact") \
                           .execute()

        # Supabase-py returns a PostgrestResponse object, check its data/error attributes
        if response.data:
            return response
        else:
            print(f"Error fetching data from Supabase: {response.error}")
            return None
    except Exception as e:
        print(f"An unexpected error occurred during Supabase fetch: {e}")
        return None

def generate_markdown_content(submissions):
    """Generates Markdown content from the fetched submissions."""


    md_content = dedent(f"""
    # Community Framework Signatories
    This page is updated daily.  If you've just signed up publicly, your name will appear on the next update.  
    Last updated: *{os.environ.get('GITHUB_RUN_TIMESTAMP', 'N/A')} (UTC)*
    """)

    if not submissions.data:
        md_content += "\n## No signatories available at this time."
        return md_content

    md_content += dedent(f"""
    There are **{submissions.count}** signatories.
    
    ## Public Signatories:
    """)

    md_content += "<ul>\n"
    for submission in submissions.data:
        if submission['show_name']:
            full_name = f"{submission.get('first_name', 'N/A')} {submission.get('last_name', 'N/A')}"
            affiliation = submission.get('affiliation', 'N/A')
            md_content += f"  <li><strong>{full_name}</strong> - {affiliation}</li>\n"
    md_content += "</ul>\n"

    return md_content

def write_content_to_file(content, filepath):
    """Writes the generated content to a file."""

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Content successfully written to {filepath}")

if __name__ == "__main__":
    print("Starting data generation for MkDocs...")
    all_submissions = fetch_public_submissions()

    if all_submissions is not None:
        md_output = generate_markdown_content(all_submissions)
        write_content_to_file(md_output, OUTPUT_MD_FILE)
    else:
        print("Failed to fetch public submissions. Skipping content generation.")

    print("Data generation finished.")
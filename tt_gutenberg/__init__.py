import pandas as pd

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/"

def load_tables():
    """
    Load and return the Gutenberg datasets.
    
    This function fetches three CSV files containing Gutenberg project metadata:
    - Author information
    - Language data for each work
    - General metadata about the works
    
    Returns:
        tuple: A tuple containing three pandas DataFrames in the order
    """
    # Load all the data
    authors   = pd.read_csv(url + "gutenberg_authors.csv")
    languages = pd.read_csv(url + "gutenberg_languages.csv")
    metadata  = pd.read_csv(url + "gutenberg_metadata.csv")
    return authors, languages, metadata


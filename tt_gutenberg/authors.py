from . import load_tables
import pandas as pd

def list_authors(by_languages: bool = True, alias: bool = True) -> list[str]:
    """
    Retrieve a list of author aliases sorted by the number of languages their works are available in.
    
    Args:
        by_languages: If True, sort authors by the number of languages their works are available in.
                     If False, the sorting behavior is undefined.
        alias: If True, return author aliases. If False, return author IDs instead.
              
    Returns:
        A list of author aliases (or IDs if alias=False) sorted by the number of languages their works are available in.
    """
    authors, languages, metadata = load_tables()

    # Drop duplicate language entries making them all unique
    sort_langs = languages[["gutenberg_id", "language"]].drop_duplicates()

    # Drop all NA entries for authors
    sort_authors = metadata[["gutenberg_id", "gutenberg_author_id"]].dropna()

    # Merge the authors with their respective languages, by id
    author_langs = sort_authors.merge(sort_langs, on="gutenberg_id")

    # Get the counts
    counts = author_langs.groupby("gutenberg_author_id")["language"].count().reset_index()

    # Merge all the data
    merged = counts.merge(authors[["gutenberg_author_id", "alias"]], on="gutenberg_author_id")

    # Sort by translation count
    merged = merged.sort_values("language", ascending=False)
    
    # return values
    return merged["alias"].dropna().tolist()
from pathlib import Path
import filters 


def search_file(directory, pattern):
    """
    Recursively search directory and return matching files.

    Args:
        directory: path to search.
        pattern: tuple (name, ext, size, days, search).

    Returns:
        Sorted list of (Path, size_str) tuples for files that match all filters.
    """
    name, ext, size, days, search = pattern
    directory = Path(directory)
    result = []
    
    for path in directory.rglob('*'):
        if (
            filters.match_name(path, name)
            and filters.match_extension(path, ext)
            and filters.match_size(path, size)
            and filters.match_date(path, days)
            and search_in_file(path, search)
        ):
            result.append((path, filters.format_size(path.stat().st_size)))

    return sorted(result, key=lambda x: x[0].name.lower())


def search_in_file(file, pat):
    """
    Check whether a file contains a text pattern.

    Args:
        file: Path object.
        pat: text to search for.

    Returns:
        bool: True if pattern is found, False otherwise.
    """
    if pat:

        try: 
            text = file.read_text().lower()
            return pat.lower() in text and pat != ''
        except UnicodeDecodeError:
            return False
        
    return True

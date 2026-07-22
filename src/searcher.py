from pathlib import Path
import filters 


def search_file(*args):
    
    directory, name, ext, days, search, size = args
    directory = Path(directory)
    result = []
    
    for path in directory.rglob('*'):
        if (
            filters.match_name(path, name)
            and filters.match_extension(path, ext)
            and filters.match_date(path, days)
            and filters.match_size(path, size)
            and search_in_file(path, search)
        ):
            result.append(path)

    return sorted(result, key=lambda x: x.name.lower())


def search_in_file(file, pat):
    if pat:

        try: 
            text = file.read_text().lower()
            return pat.lower() in text and pat != ''
        except UnicodeDecodeError:
            return False
        
    return True

from pathlib import Path
import filters 


def search_file(directory, pattern):
    name, ext, size, days = pattern
    directory = Path(directory)
    result = []
    
    for path in directory.rglob('*'):
        if (
            filters.match_name(path, name)
            and filters.match_extension(path, ext)
            and filters.match_size(path, size)
            and filters.match_date(path, days)
        ):
            result.append(path)

    return sorted(result)

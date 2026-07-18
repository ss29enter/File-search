from pathlib import Path


def search_file(directory, pattern):
    directory = Path(directory)
    result = []
    
    for path in directory.rglob('*'):
        if pattern.lower() in path.name.lower():
            result.append(path)

    return sorted(result)

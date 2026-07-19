from pathlib import Path


def search_file(directory, pattern):
    name, ext, size = pattern
    
    directory = Path(directory)
    result = []
    
    for path in directory.rglob('*'):
        if (
            match_name(path, name)
            and match_extension(path, ext)
            and match_size(path, size)
        ):
            result.append(path)

    return sorted(result)

def match_name(file, name):
    return name.lower() in file.name.lower()

def match_extension(file, ext):
    return ext == file.suffix

def match_size(file, size):
    return file.stat().st_size == size

import datetime


def match_name(file, name):
    return name.lower() in file.name.lower()


def match_extension(file, ext):
    return ext == file.suffix


def match_size(file, size):
    """
    Compare the file size with a size condition.

    Args:
        file: pathlib.Path-like object with stat().
        size: iterable where the first item is '=', '>' or '<',
              followed by a numeric value and unit, e.g. ['>', '10', 'MB'].

    Returns:
        bool: True if the file size satisfies the condition.
    """
    operation, *size_unit = size
    target_size = convert_to_bytes(size_unit)
    file_size = file.stat().st_size

    if operation == '=':
        return file_size == target_size
    elif operation == '>':
        return file_size > target_size
    else:
        return file_size < target_size


def match_date(file, recent_days):
    """
    Check if the file was modified within the last recent_days days.

    Args:
        file: pathlib.Path-like object with stat().
        recent_days: number of days as int or str.

    Returns:
        bool: True if the file is newer than recent_days.
    """
    date_modified = datetime.datetime.fromtimestamp(file.stat().st_mtime)
    date_now = datetime.datetime.now()
    recent_days = int(recent_days)

    diff_days = (date_now - date_modified).days
    return diff_days < recent_days


def convert_to_bytes(size):
    """
    Convert a size value and unit into bytes.

    Args:
        size: iterable with [value, unit], e.g. ['10', 'MB'].

    Returns:
        int: byte count.
    """
    size_int, unit = size
    size_int = int(size_int)
    if size_int == 0:
        return 0
    elif unit == 'B':
        return size_int
    elif unit == 'KB':
        return size_int * 2**10
    elif unit == 'MB':
        return size_int * 2**20
    else:
        return size_int * 2**30
    

def format_size(size,dec=2):
    """
    Format a byte count as a human-readable size string.
    """
    if size == 0:
        return '0 B'
    
    power = 1024
    units = ['B','KB','MB']
    import math
    i = int(math.floor(math.log(size, power)))
    
    return f'{size/(power**i):.{dec}f} {units[i]}'
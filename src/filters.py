from datetime import datetime


def match_name(file, name):
    if name:
        return name.lower() in file.name.lower()
    return True


def match_extension(file, ext):
    if ext:
        return ext == file.suffix
    return True


def match_date(file, recent_days):
    """
    Return True if the file was modified within recent_days.
    """
    if recent_days:
        date_modified = datetime.fromtimestamp(file.stat().st_mtime)
        date_now = datetime.now()

        diff_days = (date_now - date_modified).days
        return diff_days < recent_days
    return True


def match_size(file, size):
    """
    Return True if the file size meets the size condition.
    """
    if size:
        full_size, unit = tuple(size)
        full_size = int(full_size)
        bytes = convert_to_bytes(full_size, unit)
        file_size = file.stat().st_size

        return file_size >= bytes
    
    return True


def convert_to_bytes(size, unit):
    """
    Convert a numeric size and unit into bytes.
    
    Args:
        size: numeric value.
        unit: size unit ('B', 'KB', 'MB', 'GB').
        
    Returns:
        int: byte count.
    """
    int_size = int(size)
    if int_size == 0:
        return 0
    elif unit == 'B':
        return int_size
    elif unit == 'KB':
        return int_size * 2**10
    elif unit == 'MB':
        return int_size * 2**20
    else:
        return int_size * 2**30
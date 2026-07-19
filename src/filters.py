import datetime


def match_name(file, name):
    return name.lower() in file.name.lower()

def match_extension(file, ext):
    return ext == file.suffix

def match_size(file, size):
    operation, *size_unit = size
    bytes = format_size(size_unit)
    file_size = file.stat().st_size
    print(bytes, file_size)
    if operation == '=':
        return bytes == file_size
    
    elif operation == '>':
        return file_size > bytes

    else:
        return file_size < bytes

def match_date(file, recent_days):
    date_modified = datetime.datetime.fromtimestamp(file.stat().st_mtime)
    date_now = datetime.datetime.now()
    recent_days = int(recent_days)

    diff_days = (date_now - date_modified).days
    return diff_days < recent_days

def format_size(size):
    size_int, unit = size
    size_int = int(size_int)
    if size_int == 0:
        return 0
    elif unit == 'B':
        return size_int
    elif unit == 'KB':
        return size_int*2**10
    elif unit == 'MB':
        return size_int*2**20
    else: 
        return size_int*2**30
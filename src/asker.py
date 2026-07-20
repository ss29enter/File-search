def ask_name():
    name = input('File name: ')
    if name == '':
        return ask_name()
    return name


def ask_ext():
    ext = input('Extension: [ exp: .py ] ')
    if not ext.startswith('.'):
        return ask_ext()
    return ext


def ask_size():
    size = input('Size: [ exp: > 10 KB ] ').split()
    if len(size) == 3:
        op, dig, unit = size
        if op not in ['>','<','='] or not dig.isdigit() or unit not in ['B','KB','MB','GB']:
             return ask_size()   
    else: 
        return ask_size()
    return size


def ask_days():
    days = input('Days since creation: ')
    if not days.isdigit():
        return ask_days()
    return days


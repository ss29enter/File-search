from searcher import search_file


base_dir = input('Search path: ')
pattern = (
    input('File name: '),
    input('Extension: [ exp: .py ] '),
    input('Size: [ exp: > 10 KB ] ').split(),
    input('Days since creation: ')
)
if input('\nInclude search in the file? [Y/N] ').lower() != 'n':
    pattern += (input('Search: '),)
else:
    pattern += (0,)


def main():
    files = search_file(base_dir, pattern)
    print(f'\n> Found: {len(files)} files')

    for id, (file, size) in enumerate(files, 1):
        print(f'{id}. {file}, ({size})')


if __name__ == '__main__':
    main()
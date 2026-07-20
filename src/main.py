from searcher import search_file
import asker as ask


base_dir = input('Search path: ')
pattern = (
    ask.ask_name(),
    ask.ask_ext(),
    ask.ask_size(),
    ask.ask_days()
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
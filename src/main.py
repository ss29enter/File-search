from searcher import search_file


base_dir = input('Seacrh path: ')
pattern = input('File name: ')

def main():
    files = search_file(base_dir, pattern)

    print('> Found: {} files\n'.format(len(files)))
    for id, file in enumerate(files, 1):
        print(f'{id}. {file}')


if __name__ == '__main__':
    main()
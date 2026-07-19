from searcher import search_file


base_dir = input('Seacrh path: ')
pattern = (
    input('File name: '), 
    input('Extension: [ exp: .py ] '), 
    input('Size: [ exp: > 10 KB ] ').split(),
    input('Days since creation: ')
)
def main():
    files = search_file(base_dir, pattern)

    print('\n> Found: {} files'.format(len(files)))
    for id, file in enumerate(files, 1):
        print(f'{id}. {file}')


if __name__ == '__main__':
    main()
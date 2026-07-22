from searcher import search_file
from pathlib import Path
import filters
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='File-searcher',
        description='Search for files based on specified parameters',
    )
    parser.add_argument(
        "-p", "--path",
        required=True,
        help="Directory for searching for files"
    )
    parser.add_argument(
        "-n", "--name",
        action='store',
        help="File name or part of the file name"
    )
    parser.add_argument(
        "-ext", "--extension",
        action='store',
        help="File extension, e.g. '.py'"
    )
    parser.add_argument(
        "-s", "--minsize",
        action='store',
        nargs=2,
        help="Minimum file size in Bytes, Kilobytes, Megabytes, e.g. '10 MB'"
    )
    parser.add_argument(
        "-d", "--days",
        type=int,
        action='store',
        help="Files that have been modified in the last N days"
    )
    parser.add_argument(
        "-S", "--search",
        action='store',
        help="Search for a sequence within a file"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    try:
        files = search_file(args.path, args.name, args.extension, args.days, args.search, args.minsize)
        search_dir = Path(args.path)
        print(f'\n> Found: {len(files)} files')

        for id, file in enumerate(files, 1):
                size = filters.format_size(file.stat().st_size)
                print(f'{id}. {file.relative_to(search_dir)} ({size})')

    except Exception as error:
        print(f'OOPS... error: {error}')

    
if __name__ == '__main__':
    main()
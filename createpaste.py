import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("api_paste_code_file", metavar="File name", type=argparse.FileType(
        'r'), help="File name to be pasted.")
    parser.add_argument("--format", "-f", metavar="File format", nargs='?',
                        help="File format used in code highlighting.", default=None)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()

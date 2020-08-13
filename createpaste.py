import argparse
import pyperclip
import os
import requests
API_KEY = '<Your api key>'
API_URL = 'https://pastebin.com/api/api_post.php'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("api_paste_code_file", metavar="filename", type=argparse.FileType(
        'r'), help="File name to be pasted.")
    parser.add_argument("--format", "-f", metavar="fileformat", nargs='?',
                        help="File format used in code highlighting.", default=None)
    parser.add_argument("--expire", "-e", metavar="expiration", nargs='?',
                        help="Time before paste will be deleted. (default: 'Never')", default='10M')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    request_data = {
        'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': args.api_paste_code_file.read(),
        'api_paste_name': os.path.basename(args.api_paste_code_file.name),
        'api_paste_format': args.format,
        'api_paste_expire_date': args.expire
    }
    response = requests.post(API_URL, data=request_data)
    paste_url = response.text
    pyperclip.copy(paste_url)
    print(f'Paste created!\nLink: {paste_url}\nCopied to clipboard!')

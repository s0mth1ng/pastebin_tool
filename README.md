# Pastebin CLI tool

Simple tool for sharing code via [pastebin.com](https://pastebin.com/)

## Installation

### 1. Clone this repo.

```bash
git clone https://github.com/s0mth1ng/pastebin_tool.git
```

### 2. Install requirements.
```bash
pip intall -r requirements.txt
```

### 3. Set api key. 
Open `createpaste.py` and set `API_KEY` variable to your api key. You can find it on 
https://pastebin.com/doc_api. Required registration, but it's free.

```python
API_KEY = '<Your api key>'
```

## Usage

```
$ python3 createpaste.py -h

usage: createpaste.py [-h] [--format [fileformat]] [--expire [expiration]] filename

positional arguments:
  filename              File name to be pasted.

optional arguments:
  -h, --help            show this help message and exit
  --format [fileformat], -f [fileformat]
                        File format used in code highlighting.
  --expire [expiration], -e [expiration]
                        Time before paste will be deleted. (default: 'Never')
```

`format` and `expire` variables are in the same format like in [Pastebin api doc](https://pastebin.com/doc_api)

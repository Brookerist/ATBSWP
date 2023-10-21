#! python3
# saves and loads pieces of text to the clipboard
# Usage:    py.exe mcb.pyw save <keyword> - saves current clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword text to clipboard.
#           py.exe mcb.pyw list -  Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')


# save clipboard contents
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list keywords and load contents
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

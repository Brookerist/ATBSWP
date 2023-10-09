# python3
# find and censor cc numbers
import re
import pyperclip

ccRegex = re.compile(r'((\d{4})(\s|-)(\d{4})(\s|-)(\d{4})(\s|-)(\d{4}))')

text = str(pyperclip.paste())
print(ccRegex.sub(r'**** **** **** \8', text))


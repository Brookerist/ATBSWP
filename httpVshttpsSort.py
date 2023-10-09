#! python3
# finds and sorts urls with https and http

import re
import pyperclip

urlRegex = re.compile(r'''(
    (https|http)?           # matches https
    (://)?                  # concerned face
    ([a-zA-Z0-9-]*)?        # matches www or similar
    (\.)?                   # dot
    ([a-zA-Z0-9-]*)         # domain name
    (\.)                    # dot
    ([a-zA-Z0-9]+)          # TLD
    (\/)?                   # Slash at end
)''', re.VERBOSE | re.I)


text = str(pyperclip.paste())
httpsMatch = []
httpMatch = []
unknownMatch = []

for groups in urlRegex.findall(text):
    if groups[1] == '':
        unknownMatch.append(groups[0])
    elif groups[1] == 'https':
        httpsMatch.append(groups[0])
    elif groups[1] == 'http':
        httpMatch.append(groups[0])


if len(httpMatch) > 0:
    print('Insecure sites:')
    print('\n'.join(httpMatch))
if len(httpsMatch) > 0:
    print('Secure Sites:')
    print('\n'.join(httpsMatch))
if len(unknownMatch) > 0:
    print('Unknown sites:')
    print('\n'.join(unknownMatch))

else:
    print('No web addresses found.')

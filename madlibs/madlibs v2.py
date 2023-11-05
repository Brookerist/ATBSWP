#! python3
# madlibs program
# reads text file and asks for input to replace words
# ADJECTIVE, NOUN, ADVERB, or VERB.

import re
import pyinputplus as pyip

# regex
regex = re.compile(r'ADJECTIVE|VERB|NOUN|ADVERB')
vowel_regex = re.compile(r'^[AEIOUaeiou]\w*')

# imports file and makes string
templ = open('madlibs-source.txt', 'r')
templ_str = templ.read()

#match regex
while True:
    match = regex.search(templ_str)

    if match is None:
        print('Printing to file.')
        input('Press any key to close')

        break

    #Get user input
    else:
        if vowel_regex.search(match.group()) == None:
            replace = pyip.inputStr(f'Enter a {match.group().lower()}:\n')
        else:
            replace = pyip.inputStr(f'Enter an {match.group().lower()}:\n')


    #Replace the words
    templ_str = templ_str[:match.span()[0]] + replace + templ_str[match.span()[1]:]

# Creates output file or overwrites existing output file
out_file = open('Madlibs-output.txt', 'w')
# Writes output to file
out_file.write(templ_str)
out_file.close()

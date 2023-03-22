import re
import pyperclip

text = str(pyperclip.paste())
matches = []

phoneRegex = re.compile(r''''(
    (\+\d+\s\d\s|\d\d\s)?
    (\d\d\s)
    (\d\d\s)
    (\d\d\s)
    (\d\d\s)
)''', re.VERBOSE)
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[2], groups[3], groups[4], groups[5]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found')

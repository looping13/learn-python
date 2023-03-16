#! /usr/bin/python3
# pw.py an insecure password locker program.

PASSWORD = {'email': 'qlfkgnqrlDFGfdgkSFdf57fds',
            'blog': 'SGtildhgnoFHrQGjjfemqthj41g',
            'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password ')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for account ' + account + ' copied to clipboard')

else:
    print('There is no account named ' + account)

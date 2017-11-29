#!/usr/bin/env python3

from getpass import getpass
import hashlib
import sys

def main():
    password1 = getpass()
    password2 = getpass()
    if password1 == password2:
        print(hashlib.sha1(password1.encode('utf-8')).hexdigest())
    else:
        print('Passwords do not match')

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
import sys
filename = 'abouts.txt'
while True:
    try:
        print('inside TRY')
        myfile = open(filename, mode='r', encoding='utf-8')
    except Exception:
        print('inside EXCEPT')
        print('error found')
        print(sys.exc_info()[1])
        filename = input('Enter correct filename: ')
    else:
        print('inside ELSE')
        print(myfile.read())
        sys.exit()
print('\n<~~~~~~~~~~~~~~~EOF~~~~~~~~~~~~~~~>\n')

#!/usr/bin/env python3
import sys
import os
print('Hello')

print(sys.argv)

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == '/?':
        print('Help Requested')
        print('Usage of this program is: myfile.py arg1 arg2 arg3')
    print('Arguments entered: ', str(sys.argv[1:]))
else:
    print('Argiments not provided')

os.system('ls -lah > log22.log')
sys.exit()

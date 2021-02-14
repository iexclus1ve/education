#!/usr/bin/env python3
for i in range (3, -1, -1):
    print(i)

guess_me = 7
number = 1
while True:
    if number < guess_me:
        print(number, 'is too low')
        number += 1
    elif number == guess_me:
        print(number, 'found it!')
        break
    else:
        print(number, 'oops!')
        break

guess_me = 5
for number in range(11):
    if number < guess_me:
        print(number, 'is too low')
    elif number == guess_me:
        print(number, 'found it')
    else:
        print(number, 'oops!')
        break

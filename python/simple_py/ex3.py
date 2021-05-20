#! /usr/bin/env python3
# IF, ELIF, ELSE
secret = 8
guess = 8

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')

small = False
green = False

if small:
    print('горошек', 'вишня')
elif green:
    print('горошек', 'арбуз')
else:
    print('тыква')

#! /usr/bin/env python3
secret = 8
guess = 8

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')

#!/usr/bin/env python3

name = input('Please enter Your name: ')
print('Hello', name)

num1 = input('Enter X: ')
num2 = input('Enter Y: ')
num3 = int(num1) + int(num2)
print(num3)

message = ''
while True:
    message = input('Enter password: ')
    if message == 'secret':
        break
    print('Access denied')
print('Password correct')

mylist = []
msg = ''
while msg != 'stop'.upper():
    msg = input('Enter new item "enter STOP to finish": ')
    mylist.append(msg)

print(mylist)

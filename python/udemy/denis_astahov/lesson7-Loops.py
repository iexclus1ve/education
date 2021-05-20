#!/usr/bin/env python3

for x in range(0, 10):
    print('*****')
    print('-----')

for x in range(0, 100):
    print(x)

for x in range(0, 100, 2):
    print(x)

for x in range(-100, 10, 2):
    print('Number x = ' + str(x))

for x in range(-100, 100, 2):
    print('Number x = ' + str(x))
    if x == 50:
        break

print('\n<~~~~~~~~~~EOF~~~~~~~~~~>\n')

x = 0
while True:
    print(x)
    x += 1
    if x == 500:
        break

#!/usr/bin/env python3
x = 26

if x == 25:
    print('Yes you right')
else:
    print('No, you are wrong')

age = 21

if age <= 4:
    print('You a baby')
elif 4<=age<=14:
    print('You are kid')
elif 15<=age<=19:
    print('You are teen')
else:
    print('You are old')

all_cars = ['chrusler', 'dacia', 'bmw', 'kia', 'vw', 'seat', 'skoda', 'lada', \
        'audi', 'ford', 'chevrolett']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars:
    print('Yes, LADA is in the list')
else:
    print('LADA not in the list')

for xxx in all_cars:
    if xxx in german_cars:
        print(xxx, 'is german car')
    else:
        print(xxx, 'is not german car')


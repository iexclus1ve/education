#!/usr/bin/env python3
my_string = 'bla bla bla'
name = 'mR. vaSyA pUpKin'
print(name)
print(name.title())
print(name.upper())
print(name.lower())
print('string #1\nstring #2\nstring #3')
print('Messages:\n\tMessage 1\n\tMessage 2\n\tMessage 3\nEND')
print('Lower name: ' + name.lower())
a = (' ..... ,-}dadya vasya ..... ')
print(a)
print(a.rstrip())  #Убирает пробелы справа
print(a.lstrip())  #Убирает пробелы слева
print(a.strip())  #Убирает пробелы слева и справа
print('\n<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\n')
print(a.strip('.  ,-}'))  #Убирает точки и пробелы слева и справа
print('\n<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\n')
a = ('..... dadya vasya .....')
a = a.strip('.')
print(a)
a = a.strip()
print(a)
print(a.title())

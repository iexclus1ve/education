#!/usr/bin/env python3

def napechatat_privetstvie(name):
    """Print privetstvie"""
    print('Congratulations', name, 'wish you all the best')


def aaa():
    print('aaa')


def summa(x, y):
    s = (x + y)
    return s


def factorial(x):
    '''calculate factorial of number x'''
    otvet = 1
    for i in range(1, x + 1):
        otvet *= i
    return otvet


# napechatat_privetstvie('Denis')
# napechatat_privetstvie('Vasya')
# aaa()


#x = summa(33, 22)
# print(x)
print(factorial(1))
print(factorial(5))

for i in range(1, 10):
    print(str(i) + "!\t = ", factorial(i))

#! /usr/bin/env python3
# DICTIONARY
empty_dict = {}
print(empty_dict)

bierce = {
    'day': 'A period of twenty-four hours, mostly misspent',
    'positive': 'Mistaken at the top of one`s voice',
    'misfortune': 'The kind of fortune that never miss'
}
print(bierce)

acme_customer = {'first': 'While', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
print(type(acme_customer))

acme_customer = dict(first='Wheile', middle='E', last='Coyote')
print(acme_customer)
print(type(acme_customer))

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(lol)
print(type(lol))

lol_dict = dict(lol)
print(lol_dict)
print(type(lol_dict))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(tol)
print(type(tol))

tol_dict = dict(tol)
print(tol_dict)
print(type(tol_dict))

los = ['ab', 'cd', 'ef']
print(los)
print(type(los))

los_dict = dict(los)
print(los_dict)
print(type(los_dict))

tos = ('ab', 'cd', 'ef')
print(tos)
print(type(tos))

tos_dict = dict(tos)
print(tos_dict)
print(type(tos_dict))

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Jones',
    'Michael': 'Palin',
    'Terry': 'Gilliam'
}
print(some_pythons)

print(pythons['Cleese'])
print('Groucho' in pythons)
print(pythons.get('Groucho', 'Not a pythons'))

signals = {
    'green': 'go', 
    'yellow': 'go faster', 
    'red': 'smile for camera'
}
print(signals.keys())
print(list(signals.keys()))
print(signals.values())
print(list(signals.values()))
print(list(signals.items()))
print(len(signals))
#! /usr/bin/env python3
# DICTIONARY
import copy
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

acme_customer = dict(first='While', middle='E', last='Coyote')
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

first = {'a': 'aginy', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
third = {'d': 'donats'}
x = {**first, **second, **third}
print(x)

others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']
}
signals_copy = signals.copy()
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']
}
signals_copy = copy.deepcopy(signals)
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

a = {1: 1, 2: 2, 3: 3}
b = {1: 1, 2: 2, 3: 3}
print(a == b)
a = {1: [1, 2], 2: [1], 3: [1]}
a = {1: [1, 3], 2: [1], 3: [1]}
print(a == b)

accusation = {
    'room': 'ballroom',
    'weapon': 'lead pipe',
    'person': 'Col. Mustard'
}
for card in accusation.keys():
    print(card)
for value in accusation.values():
    print(value)
for item in accusation.items():
    print(item)
for card, content in accusation.items():
    print('Card', card, 'has the contents', content)

word = 'letters'
letters_count = {letter: word.count(letter) for letter in word}
print(letters_count)

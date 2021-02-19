#! /usr/bin/env python3
# TUPLE
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)

for marx in marxes:
    print(marx)

# marxes.insert(2, 'Gummo')
print(marxes)
print(marxes.index('Groucho'))

others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

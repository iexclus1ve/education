year_list = [1990, 1991, 1992, 1993, 1994, 1995]
print('It was my third birthday in', year_list[3])
print('In', year_list[-1], 'I was 5 year old')

things = ['mozzarella', 'cinderella', 'salmonella']
print(things)

for hum in things:
    if hum.startswith('cin'):
        things[1] = hum.capitalize()
print(things)

for cheese in things:
    if cheese.startswith('m'):
        things[0] = cheese.upper()
print(things)

things.pop()
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']

surprise[-1] = surprise[-1].lower()
print(surprise)

even = []
for num in range(10):
    even.append(num)
print(even)

even = list(range(10))
print(even)
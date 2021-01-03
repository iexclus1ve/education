#!/usr/bin/env python3

# index    0     1       2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for car in cars:
    print(car.upper())

mynumber_list = (list(range(0, 10)))
print(mynumber_list)

for x in mynumber_list:
    x *= 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print(max(mynumber_list))
print(min(mynumber_list))
print(sum(mynumber_list))

mycars = cars[1:4]
print(mycars)

mycars = cars[:3]
print(mycars)

mycars = cars[-3:-1]
print(mycars)

mycars = cars[:]
mycars.append('gaz')
print(mycars)
print(cars)

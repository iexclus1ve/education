#!/usr/bin/env python3
def create_record(name, phone, address):
    '''Create Records'''
    record = {
        'name': name,
        'phone': phone,
        'address': address,
    }
    return record


def give_awards(medal, *persons):
    '''Give medal for persons'''
    for person in persons:
        print('Tovarish', person.title(), 'nagrazhdaetsya medaliyu', medal)


user1 = create_record('Vasya', '+78906543210', 'Tunissiya')
user2 = create_record('Denis', '+75467392635', 'Argentina')

print(user1)
print(user2)

give_awards('Za Berlin', 'Vasya', 'Petya')
give_awards('Za London', 'Petya', 'Alexander', 'Valentin')

#!/usr/bin/env python3

import json
filename = 'user_settings.txt'
myfile = open(filename, mode='w', encoding='latin-1')
player1 = {
    'PlayerName': 'Dinald Trump',
    'Score': 345,
    'Awards': ['OR', 'NV', 'NY']
}

player2 = {
    'PlayerName': 'Hillory Clinton',
    'Score': 350,
    'Awards': ['WT', 'TX', 'MI']
}

my_players = []
my_players.append(player1)
my_players.append(player2)
# print(my_players)
#~~~~~~~~~~~~Save by JSON~~~~~~~~~~~~~~#

json.dump(my_players, myfile)
myfile.close()

#~~~~~~~~~~~~Load by JSON~~~~~~~~~~~~~~#

myfile = open(filename, mode='r', encoding='latin-1')
json_data = json.load(myfile)

for user in json_data:
    print('PlayerName is: ' + str(user['PlayerName']))
    print('Player Score is: ' + str(user['Score']))
    print('Player awards #1: ' + str(user['Awards'][0]))
    print('Player awards #2: ' + str(user['Awards'][1]))
    print('Player awards #3: ' + str(user['Awards'][2]))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

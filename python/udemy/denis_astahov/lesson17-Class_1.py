#!/usr/bin/env python3

class Hero():
    """Class to Create Hero for our Game"""

    def __init__(self, name, level, race,):
        """initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters of this Hero"""
        discription = (self.name, 'Level is: ' + str(self.level), 'Race is: ' + self.race, 'Health is: ',
                       str(self.health))
        print(discription)

    def level_up(self):
        """Upgrade level for Hero"""
        self.level += 1

    def move(self):
        """Start moving Hero"""
        print("Hero", self.name, "start moving")


myhero1 = Hero('Vuradlak', 5, 'Orc')
myhero2 = Hero('Alexander', 4, 'Human')

myhero1.show_hero()
myhero2.show_hero()
myhero2.move()
myhero1.level_up()

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
        discription = ('Name is: ' + self.name + '\n' 'Level is: ' + str(self.level) + '\n'
                       'Race is: ' + self.race + '\n'
                       'Health is: ' + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade level for Hero"""
        self.level += 1

    def move(self):
        """Start moving Hero"""
        print("Hero", self.name, "start moving")

    def set_health(self, new_health):
        self.health = new_health
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Super_Hero(Hero):
    """Class to create Super_Hero"""

    def __init__(self, name, level, race, magic_level):
        """Initiate our Super_Hero"""
        super().__init__(name, level, race)
        self.magic_level = magic_level
        self.magic = 100

    def make_magic(self):
        """Use Magic"""
        self.magic -= 10

    def show_hero(self):
        """Print all parameters of this Hero"""
        discription = ('Name is: ' + self.name + '\n' 'Level is: ' + str(self.level) + '\n'
                       'Race is: ' + self.race + '\n'
                       'Magic is: ' + str(self.magic) + '\n'
                       'Health is: ' + str(self.health)).title()
        print(discription)

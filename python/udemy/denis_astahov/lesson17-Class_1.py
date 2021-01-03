#!/usr/bin/env python3
from l17mod import Hero
myhero1 = Hero('Vuradlak', 5, 'Orc')
myhero2 = Hero('Alexander', 4, 'Human')
myhero1.show_hero()
myhero2.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero2.set_health(60)
myhero2.show_hero()
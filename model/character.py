from random import uniform

import logging


class Character:
    name = None
    level = None
    yes = None
    no = None
    start = None
    luck = None
    health = 100

    def className(self):
        pass

    def levelUp(self):
        self.level += 1
        self.health = 100 * self.level

    def __init__(self, name, level, yes, no, start):
        self.name = name
        self.level = level
        self.yes = yes
        self.no = no
        self.start = start
        self.luck = uniform(0, 1)
        logging.info(f'Luck for {name} is {self.luck}')

    def __str__(self):
        return f'The {self.className()} {self.name} is level {self.level} and from {self.start}'

''' Tim Sonnen 6/21/2016
    v.01
    Starship Generator for a tabletop RPG

    Creates a starship with the input of Type and size
'''

import time, sys, random, string, json

class Ship:
    def __init__(self, shipType, shipSize):
        self.shipType = shipType
        self.shipSize = shipSize
        self.shipConfig = self.getConfig()

    def getConfig(self):
        configs = json.load(open("configs.json"))
        print(random.choice(configs["Standard"]))
        return random.choice(configs["Standard"])

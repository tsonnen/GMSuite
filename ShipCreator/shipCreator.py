''' Tim Sonnen 6/28/2016
    v.01
    Starship Generator for a tabletop RPG

    Creates a starship with the input of Type and size
'''

import time
import sys
import random
import string
import json

class Ship:
    def __init__(self, shipType):
        self.shipType = shipType

        self.getShipInfo()
        self.getArmor()
        self.getSpecial()

    def getShipInfo(self):
        infoFile = open("types.json")
        infoList = json.load(infoFile)

        self.shipSize = infoList[self.shipType]['size']
        self.shipClass = infoList[self.shipType]['class']

    def getArmor(self):
        armorFile = open("armor.json")
        armorList = json.load(armorFile)
        armorType = random.choice(armorList['armors'])

        self.shipArmor = [armorType['typeName'], armorType['protection']]

        armorFile.close()

    def getSpecial(self):
        self.shipSpecial = []

        specialFile = open("special.txt")
        specialList = specialFile.read().splitlines()

        for line in specialList:
            if random.randint(1, 100) > 50:
                self.shipSpecial.append(line)

        print(self.shipSpecial)

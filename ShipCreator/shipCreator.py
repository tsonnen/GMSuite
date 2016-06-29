''' Tim Sonnen 6/21/2016
    v.01
    Starship Generator for a tabletop RPG

    Creates a starship with the input of Type and size
'''

import time, sys, random, string, json

class Ship:
    def __init__(self, shipType):
        self.shipType = shipType
        self.shipSize = ""
        self.shipConfig = ""

        self.getShipInfo()

    def getShipInfo(self):
        infoFile = open("types.json")
        infoList = json.load(infoFile)

        self.shipSize = infoList[self.shipType]['size']
        self.shipClass = infoList[self.shipType]['class']


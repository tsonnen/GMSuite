''' 7/12/2016
    v/ 1.0
    Starship Generator for a tabletop RPG

    Creates a starship with the input of Type and size
'''

import time
import sys
import random
import string
import json
import os

sys.path.insert(0, os.path.dirname(__file__))

import markov

sys.path.pop(0)

class ship:
    def __init__(self, shipType):
        self.type = shipType

        self.get_shipInfo()
        self.get_armor()
        self.get_special()
        self.get_drives()
        self.get_electronics()
        self.get_rooms()
        self.get_vehicles()
        self.get_weapons()

    def get_shipInfo(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "shipData.json")

        dataList = json.load(dataFile)
        infoList = dataList['types']
        infoDict = dict()

        # Convert the list of values to a dict so str keys can be used
        for i in infoList:
            infoDict.update(dict(i))

        self.size = infoDict[self.type]['size']
        self.classType = infoDict[self.type]['class']

        markovNames = markov.markovname(dataList['names'], 2)
        self.name = markovNames.generate()

        dataFile.close()

    def get_armor(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "shipData.json")
        dataList = json.load(dataFile)
        armorList = dataList['armor']

        # Get a random armor for the ship
        armorType = random.choice(armorList)

        self.armor = [armorType['typeName'], armorType['protection']]

        dataFile.close()

    def get_special(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "shipData.json")
        dataList = json.load(dataFile)
        specialList = dataList['special']

        self.special = []

        # There is a 50% chance of each type of special item
        for line in specialList:
            if random.randint(1, 100) > 50:
                self.special.append(line)

        dataFile.close()

    def get_drives(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "shipData.json")
        dataList = json.load(dataFile)
        driveList = dataList['drives']

        self.drives = dict()

        # Get random values for the drives of the ship
        for line in driveList:
            self.drives[line] = random.choice(string.ascii_uppercase)

        dataFile.close()

    def get_electronics(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "shipData.json")
        dataList = json.load(dataFile)
        electronicsType = random.choice(dataList['electronics'])

        self.electronics = electronicsType['system']

        self.computer = random.randint(0,8)

        dataFile.close()

    def get_rooms(self):
        self.stateRooms = random.randint(int(self.size)/100, int(self.size)/50)

        if random.randint(0,100) > 50:  
            self.lowPassageBerths = random.randint(0, int(self.size)/10)
        else:
            self.lowPassageBerths = 0

    def get_vehicles(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "shipData.json")
        dataList = json.load(dataFile)
        vehicleList = dataList['vehicles']

        self.vehicles = dict()

        for line in vehicleList:
            if random.randint(0, int(self.size)/10)  < random.randint(0, int(self.size)): 
                self.vehicles[line] =  random.randint(0, int(self.size)/100)

        dataFile.close()
        
    def get_weapons(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "shipData.json")
        dataList = json.load(dataFile)

        self.weapons = []

        if self.classType == "military":
            weaponList = dataList['weapons']
            weaponDict = dict()

            # Convert to dict to use str keys
            for i in weaponList:
                weaponDict.update(dict(i))

            mountList = weaponDict['mounts']
            typeList = weaponDict['types']

            numWeapons = random.randint(int(self.size)/1000, int(self.size)/100)

            for i in range(0, numWeapons):
                mountType = random.choice(mountList)
                mountContents = []

                for i in range(0, int(mountType['ports'])):
                    mountContents.append(random.choice(typeList))

                self.weapons.append(weapon(mountType['mountName'], mountContents))

        dataFile.close()

class weapon:
    def __init__(self, mountType, mountContents= []):
        self.mountType = mountType
        self.mountContents = mountContents

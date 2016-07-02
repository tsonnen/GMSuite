''' 7/2/2016
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
        self.getDrives()
        self.getElectronics()
        self.getRooms()
        self.getVehicles()


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

        specialFile.close()

    def getDrives(self):
        driveFile = open("drives.txt")
        driveList = driveFile.read().splitlines()

        self.shipDrives = []

        for line in driveList:
            self.shipDrives.append([line, random.choice(string.ascii_uppercase)])

        driveFile.close()

    def getElectronics(self):
        electronicsFile = open('electronics.json')
        electronicsList = json.load(electronicsFile)
        electronicsType = random.choice(electronicsList['electronics'])

        self.shipElectronics = Electronics(electronicsType['system'], electronicsType['techLevel'], electronicsType['diceModifier'], electronicsType['contents'])

        self.shipComputer = random.randint(0,8)

        electronicsFile.close()

    def getRooms(self):
        self.shipStateRooms = random.randint(int(self.shipSize)/100, int(self.shipSize)/50)

        if random.randint(0,100) > 50:  
            self.shipLowPassageBerths = random.randint(0, int(self.shipSize)/10)
        else:
            self.shipLowPassageBerths = 0

    def getVehicles(self):
        vehicleFile = open("vehicles.txt")
        vehicleList = vehicleFile.read().splitlines()

        self.shipVehicles = []

        for line in vehicleList:
            if random.randint(0, int(self.shipSize)/10)  < random.randint(0, int(self.shipSize)): 
                self.shipVehicles.append([line, random.randint(0, int(self.shipSize)/100)])
        
    def getWeapons(self):
        if self.shipType == "military":
            weaponFile = open("weapon.json")
            weaponList = json.load(weaponFile)

            mountList = json.load(weaponList['mounts'])
            typeList = json.load(weaponList['types'])

            numWeapons = random.randint(int(self.shipSize)/1000, int(self.shipSize)/100)

            self.shipWeapons = []

            for i in range(0, numWeapons):
                mountType = random.choice(mountList)
                mountContents = []

                for i in range(0, int(mountType['ports'])):
                    mountContents.append(random.choice(typeList))

                self.shipWeapons.append(Weapon(mountType['mountName'], mountContents))
        else:
            self.shipWeapons = ['None']

class Electronics:
    def __init__(self, system, techLevel, diceModifier, contents= []):
        self.elctroSystem = system
        self.electroTechLevel = techLevel
        self.electroDiceModifier = diceModifier
        self.electroContents = contents

class Weapons:
    def __init__(self, mountType, mountContents= []):
        self.mountType = mountType
        self.mountContens = mountContents

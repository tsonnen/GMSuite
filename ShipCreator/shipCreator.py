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
        self.Type = shipType

        self.getShipInfo()
        self.getArmor()
        self.getSpecial()
        self.getDrives()
        self.getElectronics()
        self.getRooms()
        self.getVehicles()
        self.getWeapons()

    def getShipInfo(self):
        infoFile = open("types.json")
        infoList = json.load(infoFile)

        self.Size = infoList[self.Type]['size']
        self.Class = infoList[self.Type]['class']

    def getArmor(self):
        armorFile = open("armor.json")
        armorList = json.load(armorFile)
        armorType = random.choice(armorList['armors'])

        self.Armor = [armorType['typeName'], armorType['protection']]

        armorFile.close()

    def getSpecial(self):
        self.Special = []

        specialFile = open("special.txt")
        specialList = specialFile.read().splitlines()

        for line in specialList:
            if random.randint(1, 100) > 50:
                self.Special.append(line)

        specialFile.close()

    def getDrives(self):
        driveFile = open("drives.txt")
        driveList = driveFile.read().splitlines()

        self.Drives = []

        for line in driveList:
            self.Drives.append([line, random.choice(string.ascii_uppercase)])

        driveFile.close()

    def getElectronics(self):
        electronicsFile = open('electronics.json')
        electronicsList = json.load(electronicsFile)
        electronicsType = random.choice(electronicsList['electronics'])

        self.Electronics = electronicsType['system']

        self.Computer = random.randint(0,8)

        electronicsFile.close()

    def getRooms(self):
        self.StateRooms = random.randint(int(self.Size)/100, int(self.Size)/50)

        if random.randint(0,100) > 50:  
            self.LowPassageBerths = random.randint(0, int(self.Size)/10)
        else:
            self.LowPassageBerths = 0

    def getVehicles(self):
        vehicleFile = open("vehicles.txt")
        vehicleList = vehicleFile.read().splitlines()

        self.Vehicles = []

        for line in vehicleList:
            if random.randint(0, int(self.Size)/10)  < random.randint(0, int(self.Size)): 
                self.Vehicles.append([line, random.randint(0, int(self.Size)/100)])
        
    def getWeapons(self):
        self.Weapons = []

        if self.Class == "military":
            weaponFile = open("weapon.json")
            weaponList = json.load(weaponFile)

            mountList = weaponList['mounts']
            typeList = weaponList['types']

            numWeapons = random.randint(int(self.Size)/1000, int(self.Size)/100)

            for i in range(0, numWeapons):
                mountType = random.choice(mountList)
                mountContents = []

                for i in range(0, int(mountType['ports'])):
                    mountContents.append(random.choice(typeList))

                self.Weapons.append(Weapon(mountType['mountName'], mountContents))

class Weapon:
    def __init__(self, mountType, mountContents= []):
        self.mountType = mountType
        self.mountContents = mountContents

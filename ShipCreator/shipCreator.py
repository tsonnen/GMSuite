''' 7/7/2016
    v.01
    Starship Generator for a tabletop RPG

    Creates a starship with the input of Type and size
'''

import time
import sys
import random
import string
import json

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
        infoFile = open("types.json")
        infoList = json.load(infoFile)

        self.size = infoList[self.type]['size']
        self.classType = infoList[self.type]['class']

    def get_armor(self):
        armorFile = open("armor.json")
        armorList = json.load(armorFile)
        armorType = random.choice(armorList['armors'])

        self.armor = [armorType['typeName'], armorType['protection']]

        armorFile.close()

    def get_special(self):
        self.special = []

        specialFile = open("special.txt")
        specialList = specialFile.read().splitlines()

        for line in specialList:
            if random.randint(1, 100) > 50:
                self.special.append(line)

        specialFile.close()

    def get_drives(self):
        driveFile = open("drives.txt")
        driveList = driveFile.read().splitlines()

        self.drives = []

        for line in driveList:
            self.drives.append([line, random.choice(string.ascii_uppercase)])

        driveFile.close()

    def get_electronics(self):
        electronicsFile = open('electronics.json')
        electronicsList = json.load(electronicsFile)
        electronicsType = random.choice(electronicsList['electronics'])

        self.electronics = electronicsType['system']

        self.computer = random.randint(0,8)

        electronicsFile.close()

    def get_rooms(self):
        self.stateRooms = random.randint(int(self.size)/100, int(self.size)/50)

        if random.randint(0,100) > 50:  
            self.lowPassageBerths = random.randint(0, int(self.size)/10)
        else:
            self.lowPassageBerths = 0

    def get_vehicles(self):
        vehicleFile = open("vehicles.txt")
        vehicleList = vehicleFile.read().splitlines()

        self.vehicles = []

        for line in vehicleList:
            if random.randint(0, int(self.size)/10)  < random.randint(0, int(self.size)): 
                self.vehicles.append([line, random.randint(0, int(self.size)/100)])
        
    def get_weapons(self):
        self.weapons = []

        if self.classType == "military":
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

                self.weapons.append(weapon(mountType['mountName'], mountContents))

class weapon:
    def __init__(self, mountType, mountContents= []):
        self.mountType = mountType
        self.mountContents = mountContents

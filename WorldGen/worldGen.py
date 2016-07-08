''' 7/7/2016

    Generates the world. Currently does not 
    take any input as none is really needed
'''

import time
import sys
import random
import string
import json

class world:
    def __init__(self):
        self.get_geo()
        self.population = 10 ** random.randint(0, 12)
        self.get_government()

    # Get the geographical features of the world
    def get_geo(self):
        geoFile = open("geography.json")
        geoList = json.load(geoFile)
        
        self.size = random.choice(geoList['size'])
        self.atmosphere = random.choice(geoList['atmosphere'])
        self.temperature = random.choice(geoList['temperature'])
        self.hydrographics = random.choice(geoList['hydrographics'])

        geoFile.close()

    def get_government(self):
        governmentFile = open("government.json")
        governmentList = json.load(governmentFile)

        self.governmentType = random.choice(governmentList['government'])
        self.factions = []

        numFactions = random.randint(1,3)

        for i in range(0, numFactions):
            self.factions.append([random.choice(governmentList['factionStr']), 
                                  random.choice(governmentList['government'])])

        self.lawLevel = random.choice(governmentList['lawLevel'])

        print(self.factions)
        print(self.lawLevel['drugs'])

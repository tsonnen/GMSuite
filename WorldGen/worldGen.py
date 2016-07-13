''' 7/12/2016

    v. 1.0

    Generates the world. Currently does not 
    take any input as none is really needed
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

class world:
    def __init__(self):
        self.get_geo()
        self.population = 10 ** random.randint(0, 12)
        self.get_government()
        self.get_name()

    # Get the geographical features of the world
    def get_geo(self):
        geoFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + os.sep + "worldData.json")
        geoList = json.load(geoFile)
        
        self.size = random.choice(geoList['size'])
        self.atmosphere = random.choice(geoList['atmosphere'])
        self.temperature = random.choice(geoList['temperature'])
        self.hydrographics = random.choice(geoList['hydrographics'])

        geoFile.close()

    def get_government(self):
        governmentFile = open(os.path.dirname(os.path.realpath(__file__)) 
                            + os.sep + "worldData.json")
        governmentList = json.load(governmentFile)

        self.governmentType = random.choice(governmentList['government'])
        self.factions = []

        numFactions = random.randint(1,3)

        for i in range(0, numFactions):
            self.factions.append([random.choice(governmentList['factionStr']), 
                                  random.choice(governmentList['government'])])

        self.lawLevel = random.choice(governmentList['lawLevel'])

    def get_name(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                            + os.sep + "worldData.json")
        dataList = json.load(dataFile)

        markovNames = markov.markovname(dataList['names'])
        self.name = markovNames.generate()

        dataFile.close()

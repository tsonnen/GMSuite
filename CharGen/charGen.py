''' 7/11/2016
    v. .01
    Character Generator for a tabletop RPG
     
    Creates a charcter with the input of Class, Race, Setting, and System
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

class character:
    def __init__(self, system, classChoice, race):
        self.race = race
        self.classChoice = classChoice

        self.get_stats(system)
        self.get_name(race)
        self.get_skills()

    def get_stats(self, system):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "charData.json")
        dataList = json.load(dataFile)
        statChoices = dataList['stats']

        self.charStats = {}

        for i in range(0,len(statChoices)):
            self.charStats[statChoices[i]] = self.get_statVal(system)

    def get_statVal(self, system):
        if (system == "Dice"):
            return random.choice(["d6", "d8", "d10", "d12"])
        elif (system == "4d6"):
            total = 0
            for i in range(0,4):
                total += random.randrange(1,6)
            return total
        else:
            total = 0
            for i in range(0,2):
                 total += random.randrange(1,6)
            return total

    def get_name(self, race):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "charData.json")
        dataList = json.load(dataFile)
        nameList = dataList['names']
        nameDict = dict()

        for i in nameList:
            nameDict.update(dict(i))

        markovNames = markov.markovname(nameDict[race], 2)
        self.name = markovNames.generate()

    def get_skills(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "charData.json")
        dataList = json.load(dataFile)
        skillList = dataList['skills']

        skillVal = random.randrange(25, 40)

        charSkills = dict()

        baseList = dataList['classes']
        baseDict = dict()

        for y in baseList:
            baseDict.update(dict(y))

        baseSkills = baseDict[self.classChoice]

        for x in baseSkills:
            charSkills[x] = 0

        for i in range(0, skillVal):
            skill = random.choice(skillList)
            if skill in charSkills.keys():
                charSkills[skill] += 1;
            else:
                charSkills[skill] = 0;

        self.skills = charSkills

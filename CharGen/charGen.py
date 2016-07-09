''' 7/7/2016
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

class character:
    def __init__(self, system, classChoice, race, statChoices = [] ):
        self.race = race
        self.classChoice = classChoice
        self.get_stats(system, statChoices)
        self.name = self.get_name(race)
        self.skills = self.get_skills()
        self.stringCharacter()

    def get_stats(self, system, statChoices = [] ):
        self.charStats = []

        for i in range(0,len(statChoices)):
            self.charStats.append([statChoices[i], self.get_statVal(system)])

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
        names = json.load(open(os.path.dirname(os.path.realpath(__file__)) 
                                + os.sep + "firstnames.json"))
        return random.choice(names[race])

    def get_skills(self):
        skillVal = random.randrange(25, 40)
        skillFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + os.sep + "skills.txt")
        skillList = skillFile.read().splitlines()

        charSkills = []

        baseFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "classes.json")
        baseList = json.load(baseFile)
        baseSkills = baseList[self.classChoice]

        for x in baseSkills:
            charSkills.append([x, 0])

        for i in range(0, skillVal):
            skill = random.choice(skillList)
            if(skill in charSkills):
                charSkills[skill][0] += 1;
            else:
                charSkills.append([skill, 0]);
        return charSkills

    def stringCharacter(self):
        charstr = self.name + "\t" + self.race + " " + self.classChoice + "\n"
        for i in range(0, len(self.charStats)):
            charstr += self.charStats[i][0] + ": " + str(self.charStats[i][1]) + "\n"
        for x in range(0, len(self.skills)):
            charstr += self.skills[x][0] + "  " + str(self.skills[x][1]) + ", "
        return charstr

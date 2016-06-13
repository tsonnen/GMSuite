''' Tim Sonnen  6/12/2016
    v. .01
    Character Generator for a tabletop RPG
     
    Creates a character with minimal to no input from the user
'''
import time, sys, random, string

class Create:
    def __init__(self, system, setting,  classChoice, race, statChoices = [] ):
        self.charStats = [["Strength", 0],["Dexterity", 0],["Intelligence", 0],["Constitution", 0],["Wisdom", 0],["Charisma", 0],["Psionics",0]]
        self.getStats(system, statChoices)
        self.name = self.getName(setting, race)

    def getStats(self, system, statChoices = [] ):
        for i in range(0,len(statChoices)):
            self.charStats[i][1] = self.getStatVal(system)
        print(self.charStats)

    def getStatVal(self, system):
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

    def getName(self, setting, race):
        

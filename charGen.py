''' Tim Sonnen  6/12/2016
    v. .01
    Character Generator for a tabletop RPG
     
    Creates a character with minimal to no input from the user
'''
import time, sys, random, string, json

class Character:
    def __init__(self, system, setting,  classChoice, race, statChoices = [] ):
        self.race = race
        self.classChoice = classChoice
        self.charStats = [["Strength", 0],["Dexterity", 0],["Intelligence", 0],["Constitution", 0],["Wisdom", 0],["Charisma", 0],["Psionics",0]]
        self.getStats(system, statChoices)
        self.name = self.getName(race)
        self.skills = self.getSkills()
        self.stringCharacter()

    def getStats(self, system, statChoices = [] ):
        for i in range(0,len(statChoices)):
            self.charStats[i][1] = self.getStatVal(system)

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

    def getName(self, race):
        names = json.load(open("firstnames.json"))
        return random.choice(names[race])

    def getSkills(self):
        skillVal = random.randrange(25, 40)
        skillList = open("skills.txt").read().splitlines()
        charSkills = []

        for i in range(0, skillVal):
            new = []
            skill = random.choice(skillList)
            if(skill in charSkills):
                charSkills[skill][0] += 1;
            else:
                new.append(skill)
                new.append(0)
                charSkills.append(new);
        return charSkills

    def stringCharacter(self):
        charstr = self.name + "\t" + self.race + " " + self.classChoice + "\n"
        for i in range(0, len(self.charStats)):
            charstr += self.charStats[i][0] + ": " + str(self.charStats[i][1]) + "\n"
        for x in range(0, len(self.skills)):
            charstr += self.skills[x][0] + "  " + str(self.skills[x][1]) + ", "
        return charstr


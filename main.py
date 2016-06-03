''' Tim Sonnen  6/2/2016
    v. .01
    Character Generator for a tabletop RPG
     
    Creates a character with minimal to no input from the user
'''
import time, sys, random, string

def getName():
    fnametxt  = open('first_name.txt')
    lnametxt  = open('last_name.txt')
    fname     = random.choice(fnametxt.read().splitlines())
    lname     = random.choice(lnametxt.read().splitlines())
    name      = fname + ' ' + lname
    return name

def getTraits():


class Character:
    def __init__(self):
        self.name   = getName()
        self.traits = getTraits()
        print(self.name)

x = Character()

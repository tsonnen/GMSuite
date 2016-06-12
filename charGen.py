''' Tim Sonnen  6/12/2016
    v. .01
    Character Generator for a tabletop RPG
     
    Creates a character with minimal to no input from the user
'''
import time, sys, random, string

class Create:
    def __init__(self, statList, system, setting,  classChoice, race):
        switch system:
            case "dice":
                print("hello")
            case "2d6":
                print("what's up")
            case "4d6":
                print("dude")
            default:
                print("WAT")


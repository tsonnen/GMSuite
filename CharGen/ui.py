''' 7/7/2016
    Provides a Ui that allows the user to easily
    enter in the seed information to make a character
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
import charGen

class charGenUI:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("charGen.glade")

        window = builder.get_object("MainWindow")

        self.systemChoices = builder.get_object("systemChoices")
        self.raceChoices = builder.get_object("raceChoices")
        self.classChoices = builder.get_object("classChoices")
        self.submitButton = builder.get_object("submit")


        self.getSystems()
        self.getClasses()
        self.getRaces()

        statsFile = open("stats.txt")

        self.stats = statsFile.read().splitlines()
        self.submitButton.connect("clicked", self.submit_OnClick)

        window.show_all()
        window.connect("destroy", self.Destroy)

        statsFile.close()

        gtk.main()

    def getSystems(self):
        systemFile = open("systems.txt")
        systems    = systemFile.read().splitlines()

        for i in systems:
            self.systemChoices.append_text(i)

        self.systemChoices.set_active(0)

        systemFile.close()

    def getClasses(self):
        classFile = open("classes.json")
        classes = json.load(classFile)
        classList = classes

        self.classChoices.remove_all()
        
        for i in classList:
            self.classChoices.append_text(i)

        self.classChoices.set_active(0)

        classFile.close()

    def getRaces(self):
        racesFile = open("firstnames.json")
        races = json.load(racesFile)
        
        for i in races:
             self.raceChoices.append_text(i)

        self.raceChoices.set_active(0)

        racesFile.close()

    def submit_OnClick(self, button):
        character = charGen.Character(self.systemChoices.get_active_text(), self.classChoices.get_active_text(), self.raceChoices.get_active_text(), self.stats)

        self.PopUp(character)

    def PopUp(self, character):
        popUpBuilder = gtk.Builder()
        popUpBuilder.add_from_file("charGen.glade")

        popup = popUpBuilder.get_object("CharDisplay")

        charName = popUpBuilder.get_object("nameLbl")
        charRaceClass = popUpBuilder.get_object("raceClassLbl") 
        charStats = popUpBuilder.get_object("statsLbl")
        charSkills = popUpBuilder.get_object("skillsLbl")

        charName.set_text(character.name)
        charRaceClass.set_text(character.race + "/" + character.classChoice)

        statStr = ""
        skillStr = ""

        for x in range(0,len(character.skills)):
            skillStr += character.skills[x][0] + " " + str(character.skills[x][1]) + ", " 

        for i in range(0,len(character.charStats)):
            statStr += character.charStats[i][0] + ": " + str(character.charStats[i][1]) + "\n" 

        charStats.set_text(statStr)
        charSkills.set_text(skillStr)

        charSkills.set_line_wrap(True)
        charSkills.set_size_request(-1, -1)

        popup.show_all()

    def Destroy(self, obj):
        gtk.main_quit()

app = charGenUI()

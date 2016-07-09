''' 7/7/2016
    Provides a Ui that allows the user to easily
    enter in the seed information to make a character
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
import charGen
import os

class chargen_ui:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                + "/charGen.glade")

        window = builder.get_object("MainWindow")

        self.systemChoices = builder.get_object("systemChoices")
        self.raceChoices = builder.get_object("raceChoices")
        self.classChoices = builder.get_object("classChoices")
        self.submitButton = builder.get_object("submit")


        self.systems()
        self.classes()
        self.races()

        statsFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + "/stats.txt")

        self.stats = statsFile.read().splitlines()
        self.submitButton.connect("clicked", self.submit_OnClick)

        window.show_all()
        window.connect("destroy", self.Destroy)

        statsFile.close()

        gtk.main()

    def systems(self):
        systemFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + "/systems.txt")
        systemsList = systemFile.read().splitlines()

        for i in systemsList:
            self.systemChoices.append_text(i)

        self.systemChoices.set_active(0)

        systemFile.close()

    def classes(self):
        classFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + "/classes.json")
        classList = json.load(classFile)

        self.classChoices.remove_all()
        
        for i in classList:
            self.classChoices.append_text(i)

        self.classChoices.set_active(0)

        classFile.close()

    def races(self):
        racesFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + "/firstnames.json")
        racesList = json.load(racesFile)
        
        for i in racesList:
             self.raceChoices.append_text(i)

        self.raceChoices.set_active(0)

        racesFile.close()

    def submit_OnClick(self, button):
        character = charGen.character(self.systemChoices.get_active_text(), self.classChoices.get_active_text(), self.raceChoices.get_active_text(), self.stats)

        self.popup(character)

    def popup(self, character):
        popUpBuilder = gtk.Builder()
        popUpBuilder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                    + "/charGen.glade")

        popupWindow = popUpBuilder.get_object("CharDisplay")

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

        popupWindow.show_all()

    def Destroy(self, obj):
        gtk.main_quit()

''' 7/9/2016
    Provides a Ui that allows the user to easily
    enter in the seed information to make a character
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
from . import charGen
import os

class chargen_ui:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                + os.sep + "charGen.glade")

        window = builder.get_object("MainWindow")

        self.systemChoices = builder.get_object("systemChoices")
        self.raceChoices = builder.get_object("raceChoices")
        self.classChoices = builder.get_object("classChoices")
        self.submitButton = builder.get_object("submit")


        self.systems()
        self.classes()
        self.races()

        self.submitButton.connect("clicked", self.submit_OnClick)

        window.show_all()
        window.connect("destroy", self.Destroy)

        gtk.main()

    def systems(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + os.sep + "charData.json")
        dataList = json.load(dataFile)
        systemsList = dataList['systems']

        for i in systemsList:
            self.systemChoices.append_text(i)

        self.systemChoices.set_active(0)

        dataFile.close()

    def classes(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "charData.json")
        dataList = json.load(dataFile)
        classList = dataList['classes']

        for i in classList:
            self.classChoices.append_text(i.keys()[0])

        self.classChoices.set_active(0)

        dataFile.close()

    def races(self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__))
                        + os.sep + "charData.json")
        dataList = json.load(dataFile)
        racesList = dataList['names']
        
        for i in racesList:
             self.raceChoices.append_text(i.keys()[0])

        self.raceChoices.set_active(0)

        dataFile.close()

    def submit_OnClick(self, button):
        character = charGen.character(self.systemChoices.get_active_text(), self.classChoices.get_active_text(), self.raceChoices.get_active_text())

        self.popup(character)

    def popup(self, character):
        popUpBuilder = gtk.Builder()
        popUpBuilder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                    + os.sep + "charGen.glade")

        popupWindow = popUpBuilder.get_object("CharDisplay")

        charName = popUpBuilder.get_object("nameLbl")
        charRaceClass = popUpBuilder.get_object("raceClassLbl") 
        charStats = popUpBuilder.get_object("statsLbl")
        charSkills = popUpBuilder.get_object("skillsLbl")

        charName.set_text(character.name)
        charRaceClass.set_text(character.race + os.sep + "" + character.classChoice)

        statStr = ""
        skillStr = ""

        for x in character.skills.keys():
            skillStr += x + " " + str(character.skills[x]) + ", " 

        for i in character.charStats.keys():
            statStr += i + ": " + str(character.charStats[i]) + "\n" 

        charStats.set_text(statStr)
        charSkills.set_text(skillStr)

        charSkills.set_line_wrap(True)
        charSkills.set_size_request(-1, -1)

        popupWindow.show_all()

    def Destroy(self, obj):
        gtk.main_quit()

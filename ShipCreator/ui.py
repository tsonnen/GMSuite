'''Tim Sonnen   6/20/2016
   A UI for creating a ship to be used in a Sci-Fi
   tabletop RPG.
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
import shipCreator

class shipCreatorUI:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("ShipCreator.glade")

        window = builder.get_object("MainWindow")

        self.typeChoice = builder.get_object("typeChoice")
        self.submitButton = builder.get_object("submit")

        self.getTypes()

        self.submitButton.connect("clicked", self.submit_OnClick)

        window.show_all()

        gtk.main()

    def getTypes (self):
        typesFile = open("types.json")
        types = json.load(typesFile)

        for i in types:
            self.typeChoice.append_text(i)

        self.typeChoice.set_active(0)

        typesFile.close()

    def submit_OnClick(self, button):
        ship = shipCreator.Ship(self.typeChoice.get_active_text())

app = shipCreatorUI()

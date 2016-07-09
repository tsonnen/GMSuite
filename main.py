''' 7/8/2016

    Allows the user to launch the desired creation
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
import CharGen.ui as charui
import ShipCreator.ui as shipui
import WorldGen.ui as worldui

class mainui:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("main.glade")

        window = builder.get_object("mainwindow")

        self.charGen = builder.get_object("charGen")
        self.shipCreation = builder.get_object("shipCreation")
        self.worldGen = builder.get_object("worldGen")

        self.charGen.connect("clicked", self.charGen_OnClick)
        self.shipCreation.connect("clicked", self.shipCreation_OnClick)
        self.worldGen.connect("clicked", self.worldGen_OnClick)

        window.connect("destroy", self.Destroy)

        window.show_all()
        gtk.main()

    def charGen_OnClick(self, button):
        app = charui.chargen_ui()

    def worldGen_OnClick(self, button):
        app = worldui.worldgen_ui()

    def shipCreation_OnClick(self, button):
        app = shipui.shipcreator_ui()

    def Destroy(self, obj):
        gtk.main_quit()

app = mainui()

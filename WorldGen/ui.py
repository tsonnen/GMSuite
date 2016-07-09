''' 7/8/2016

    V. 0.9
    Shows the UI for the world generation
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
import worldGen
import os

class worldgen_ui:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                + "/WorldGen.glade")

        window = builder.get_object("mainwindow")

        self.typeChoice = builder.get_object("typeChoice")
        self.submitButton = builder.get_object("submit")

        self.submitButton.connect("clicked", self.submit_OnClick)
        window.connect("destroy", self.Destroy)

        window.show_all()

        gtk.main()

    def submit_OnClick(self, button):
        world = worldGen.world()

    def Destroy(self, obj):
        gtk.main_quit()

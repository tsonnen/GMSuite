''' 7/8/2016

    V. 0.9
    Shows the UI for the world generation
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
from . import worldGen
import os

class worldgen_ui:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                + os.sep + "WorldGen.glade")

        window = builder.get_object("mainwindow")

        self.typeChoice = builder.get_object("typeChoice")
        self.submitButton = builder.get_object("submit")

        self.submitButton.connect("clicked", self.submit_OnClick)
        window.connect("destroy", self.Destroy)

        window.show_all()

        gtk.main()

    def submit_OnClick(self, button):
        world = worldGen.world()

        self.popup(world)

    def popup(self, world):
        popUpBuilder = gtk.Builder()
        popUpBuilder.add_from_file(os.path.dirname(os.path.realpath(__file__))
                                        + os.sep + "WorldGen.glade")

        popupWindow = popUpBuilder.get_object("world_display")

        worldSize = popUpBuilder.get_object("sizeLbl")
        worldAtmosphere = popUpBuilder.get_object("atmosphereLbl")
        worldTemperature = popUpBuilder.get_object("temperatureLbl")
        worldHydrographics = popUpBuilder.get_object("hydrographicsLbl")
        worldGovernment = popUpBuilder.get_object("governmentLbl")
        worldFactions = popUpBuilder.get_object("factionsLbl")
        worldWeapons = popUpBuilder.get_object("weaponsLbl")
        worldDrugs = popUpBuilder.get_object("drugsLbl")
        worldInformation = popUpBuilder.get_object("informationLbl")
        worldTechnology = popUpBuilder.get_object("technologyLbl")
        worldTravellers = popUpBuilder.get_object("travellersLbl")
        worldPsionics = popUpBuilder.get_object("psionicsLbl")

        factionStr = ""

        for i in world.factions:
            factionStr += i[0] + " " + i[1] + "\n"

        worldSize.set_text(world.size)
        worldAtmosphere.set_text(world.atmosphere)
        worldTemperature.set_text(world.temperature)
        worldHydrographics.set_text(world.hydrographics)
        worldGovernment.set_text(world.governmentType)
        worldFactions.set_text(factionStr)
        worldWeapons.set_text("Illegal weapons:" + world.lawLevel['weapons'])
        worldDrugs.set_text("Illegal drugs:" + world.lawLevel['drugs'])
        worldInformation.set_text("Illegal information:" + world.lawLevel['information'])
        worldTechnology.set_text("Illegal technology:" + world.lawLevel['technology'])
        worldTravellers.set_text("Illegal travellers:" + world.lawLevel['travellers'])
        worldPsionics.set_text("Illegal psionics:" + world.lawLevel['psionics'])
        
        popupWindow.show_all()


    def Destroy(self, obj):
        gtk.main_quit()

'''7/13/2016
   A UI for creating a ship to be used in a Sci-Fi
   tabletop RPG.
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import json
from . import shipCreator
import os

class shipcreator_ui:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                + os.sep + "ShipCreator.glade")

        window = builder.get_object("MainWindow")

        self.typeChoice = builder.get_object("typeChoice")
        self.submitButton = builder.get_object("submit")

        self.get_types()

        self.submitButton.connect("clicked", self.submit_OnClick)

        window.show_all()
        
        window.connect("destroy", self.Destroy)

        gtk.main()

    # Load the types of ships from the json file
    def get_types (self):
        dataFile = open(os.path.dirname(os.path.realpath(__file__)) 
                        + os.sep + "shipData.json")
        dataList = json.load(dataFile)
        types = dataList['types']

        for i in types:
            self.typeChoice.append_text(list(i.keys())[0])

        self.typeChoice.set_active(0)

        dataFile.close()

    def submit_OnClick(self, button):
        ship = shipCreator.ship(self.typeChoice.get_active_text())
        
        self.popup(ship)

    def popup(self, ship):
        popUpBuilder = gtk.Builder()
        popUpBuilder.add_from_file(os.path.dirname(os.path.realpath(__file__)) 
                                    + os.sep + "ShipCreator.glade")

        popupWindow = popUpBuilder.get_object("ShipDisplay")

        shipName = popUpBuilder.get_object("nameLbl")
        shipInfo = popUpBuilder.get_object("infoLbl")
        shipSpecial = popUpBuilder.get_object("specialLbl")
        shipArmor = popUpBuilder.get_object("armorLbl")
        shipDrives = popUpBuilder.get_object("drivesLbl")
        shipElectronics = popUpBuilder.get_object("electronicsLbl")
        shipRooms = popUpBuilder.get_object("roomsLbl")
        shipVehicles = popUpBuilder.get_object("vehiclesLbl")
        shipWeapons = popUpBuilder.get_object("weaponsLbl")

        specialStr = ""
        driveStr = ""
        vehicleStr = ""
        weaponStr = ""

        for special in ship.special:
            specialStr += special + "\n"
        
        for drive in ship.drives.keys():
            driveStr += drive + ":" + ship.drives[drive] + "\n" 

        for vehicle in ship.vehicles.keys():
            vehicleStr +=  str(ship.vehicles[vehicle]) + " "  + vehicle + "\n"

        for weapon in ship.weapons:
            weaponStr += weapon.mountType + "\n"

            for item in weapon.mountContents:
                weaponStr += "\t" + item + "\n"

        shipName.set_text(ship.name)
        shipInfo.set_text(ship.type + " " + ship.size + " tons")
        shipArmor.set_text(ship.armor[0] + " : " + str(ship.armor[1]) + " protection")
        shipSpecial.set_text(specialStr)
        shipDrives.set_text(driveStr)
        shipRooms.set_text(str(ship.stateRooms) + " State rooms\n"  + str(ship.lowPassageBerths) + " Low passage berths")
        shipElectronics.set_text("Computer: " + str(ship.computer) + "\n" + ship.electronics + "Level electronics" )
        shipVehicles.set_text(vehicleStr)
        shipWeapons.set_text(weaponStr)


        popupWindow.show_all()

    def Destroy(self, obj):
        gtk.main_quit()

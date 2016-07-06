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
        
        window.connect("destroy", self.Destroy)

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
        
        self.PopUp(ship)

    def PopUp(self, ship):
        popUpBuilder = gtk.Builder()
        popUpBuilder.add_from_file("ShipCreator.glade")

        popup = popUpBuilder.get_object("ShipDisplay")

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

        for special in ship.Special:
            specialStr += special + "\n"
        
        for drive in ship.Drives:
            driveStr += drive[0] + ":" + drive[1] + "\n" 

        for vehicle in ship.Vehicles:
            vehicleStr +=  str(vehicle[1]) + " "  + vehicle[0] + "\n"

        for weapon in ship.Weapons:
            weaponStr += weapon.mountType + "\n"

            for item in weapon.mountContents:
                weaponStr += "\t" + item + "\n"

        shipInfo.set_text(ship.Type + " " + ship.Size + " tons")
        shipArmor.set_text(ship.Armor[0] + " : " + str(ship.Armor[1]) + " protection")
        shipSpecial.set_text(specialStr)
        shipDrives.set_text(driveStr)
        shipRooms.set_text(str(ship.StateRooms) + " State rooms\n"  + str(ship.LowPassageBerths) + " Low passage berths")
        shipElectronics.set_text("Computer: " + str(ship.Computer) + "\n" + ship.Electronics + "Level electronics" )
        shipVehicles.set_text(vehicleStr)
        shipWeapons.set_text(weaponStr)


        popup.show_all()

    def Destroy(self, obj):
        gtk.main_quit()

app = shipCreatorUI()

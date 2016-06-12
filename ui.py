from Tkinter import *
import json
import charGen

class App:

    def __init__(self, master):
        self.master = master
        self.system  = StringVar(master)
        self.setting = StringVar(master)
        self.classChoice = StringVar(master)
        self.race = StringVar(master)
        self.statChoices = []
        self.system.set("2d6")
        self.setting.set("Fantasy")
        self.classChoice.set("Scout")

        frame = Frame(master)
        frame.grid()

        Label(master, text = "Stats").grid(row = 0, column = 0, sticky=W)

        self.var1 = IntVar(master)
        Checkbutton(master, text="Strength", variable = self.var1).grid(row = 1, column = 0, sticky=W)

        self.var2 = IntVar(master)
        Checkbutton(master, text="Dexterity", variable = self.var2).grid(row = 2, column = 0, sticky=W)

        self.var3 = IntVar(master)
        Checkbutton(master, text="Intelligence", variable = self.var3).grid(row = 3, column = 0, sticky=W)

        self.var4 = IntVar(master)
        Checkbutton(master, text="Constitution", variable = self.var4).grid(row = 4, column = 0, sticky=W)

        self.var5 = IntVar(master)
        Checkbutton(master, text="Wisdom", variable = self.var5).grid(row = 5, column = 0, sticky=W)

        self.var6 = IntVar(master)
        Checkbutton(master, text="Charisma", variable = self.var6).grid(row = 6, column = 0, sticky=W)

        self.var7 = IntVar(master)
        Checkbutton(master, text="Psionics", variable = self.var7).grid(row = 7, column = 0, sticky=W)

        Label(master, text  = "System").grid(row = 0, column = 2, sticky=W)
        OptionMenu(master, self.system, "2d6", "4d6", "Dice").grid(row = 1, column = 2, sticky=W)

        Label(master, text = "Setting").grid(row = 2, column = 2, sticky=W)
        OptionMenu(master, self.setting, "Fantasy", "Sci-Fi", "IRL", 
                   command = lambda x: self.updateMenus()).grid(row = 3, column = 2, sticky=W)

        Label(master, text = "Class").grid(row = 5, column = 2, sticky=W)
        self.getClasses(self.setting.get())

        Label(master, text = "Race").grid(row = 7, column = 2, sticky = W)
        self.getRaces(self.setting.get())

        Button(master, text="Submit", command = lambda: self.submit()).grid(row = 9, column = 1, sticky = W)

    def updateMenus(self):
         self.getClasses(self.setting.get()) 
         self.getRaces(self.setting.get())

    def getClasses(self, setting):
        classes = json.load(open("classes.json"))
        classList = classes[setting]
        self.classChoice.set(classList[0])
        self.classMenu = OptionMenu(self.master, self.classChoice, *classList).grid(row = 6, column = 2, sticky = W)

    def getRaces(self, setting):
        races = json.load(open("races.json"))
        raceList = races[setting]
        self.race.set(raceList[0])
        self.raceMenu = OptionMenu(self.master, self.race, *raceList).grid(row = 8, column = 2, sticky = W)

    def submit(self):
        self.statChoices.append(self.var1.get())
        self.statChoices.append(self.var2.get())
        self.statChoices.append(self.var3.get())
        self.statChoices.append(self.var4.get())
        self.statChoices.append(self.var5.get())
        self.statChoices.append(self.var6.get())
        self.statChoices.append(self.var7.get())

        character = charGen.Create(self.statChoices, self.system, self.setting,  self.classChoice, self.race)

root = Tk()

app = App(root)

root.mainloop()

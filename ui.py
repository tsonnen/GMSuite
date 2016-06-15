import Tkinter as tk
import json
import charGen

class App(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.system  = tk.StringVar(self)
        self.setting = tk.StringVar(self)
        self.classChoice = tk.StringVar(self)
        self.race = tk.StringVar(self)
        self.system.set("2d6")
        self.setting.set("Fantasy")
        self.classChoice.set("Scout")

        self.grid()

        tk.Label(self, text = "Stats").grid(row = 0, column = 0, sticky=tk.W)

        self.var1 = tk.IntVar(self)
        tk.Checkbutton(self, text="Strength", variable = self.var1).grid(row = 1, column = 0, sticky=tk.W)

        self.var2 = tk.IntVar(self)
        tk.Checkbutton(self, text="Dexterity", variable = self.var2).grid(row = 2, column = 0, sticky=tk.W)

        self.var3 = tk.IntVar(self)
        tk.Checkbutton(self, text="Intelligence", variable = self.var3).grid(row = 3, column = 0, sticky=tk.W)

        self.var4 = tk.IntVar(self)
        tk.Checkbutton(self, text="Constitution", variable = self.var4).grid(row = 4, column = 0, sticky=tk.W)

        self.var5 = tk.IntVar(self)
        tk.Checkbutton(self, text="Wisdom", variable = self.var5).grid(row = 5, column = 0, sticky=tk.W)

        self.var6 = tk.IntVar(self)
        tk.Checkbutton(self, text="Charisma", variable = self.var6).grid(row = 6, column = 0, sticky=tk.W)

        self.var7 = tk.IntVar(self)
        tk.Checkbutton(self, text="Psionics", variable = self.var7).grid(row = 7, column = 0, sticky=tk.W)

        tk.Label(self, text  = "System").grid(row = 0, column = 2, sticky=tk.W)
        tk.OptionMenu(self, self.system, "2d6", "4d6", "Dice").grid(row = 1, column = 2, sticky=tk.W)

        tk.Label(self, text = "Setting").grid(row = 2, column = 2, sticky=tk.W)
        tk.OptionMenu(self, self.setting, "Fantasy", "Sci-Fi", "IRL", 
                   command = lambda x: self.updateMenus()).grid(row = 3, column = 2, sticky=tk.W)

        tk.Label(self, text = "Class").grid(row = 5, column = 2, sticky=tk.W)
        self.getClasses(self.setting.get())

        tk.Label(self, text = "Race").grid(row = 7, column = 2, sticky = tk.W)
        self.getRaces(self.setting.get())

        tk.Button(self, text="Submit", command = lambda: self.submit()).grid(row = 9, column = 1, sticky = tk.W)

    def updateMenus(self):
         self.getClasses(self.setting.get()) 
         self.getRaces(self.setting.get())

    def getClasses(self, setting):
        classes = json.load(open("classes.json"))
        classList = classes[setting]
        self.classChoice.set(classList[0])
        self.classMenu = tk.OptionMenu(self, self.classChoice, *classList).grid(row = 6, column = 2, sticky = tk.W)

    def getRaces(self, setting):
        races = json.load(open("races.json"))
        raceList = races[setting]
        self.race.set(raceList[0])
        self.raceMenu = tk.OptionMenu(self, self.race, *raceList).grid(row = 8, column = 2, sticky = tk.W)

    def submit(self):
        statChoices = []
        statChoices.append(self.var1.get())
        statChoices.append(self.var2.get())
        statChoices.append(self.var3.get())
        statChoices.append(self.var4.get())
        statChoices.append(self.var5.get())
        statChoices.append(self.var6.get())
        statChoices.append(self.var7.get())

        character = charGen.Character(self.system.get(), self.setting.get(),  self.classChoice.get(), self.race.get(), statChoices)

        strChar = character.stringCharacter()
        self.PopUp(strChar)

    def PopUp(self, stringCharacter):
        t = tk.Toplevel(self)
        tk.Label(t, text=stringCharacter).grid(row = 0, column = 0, sticky = tk.W)
        tk.Button(t, text = "Close").grid(row = 1, column = 0, sticky = tk.W)

app = App()
app.master.title('Character')
app.mainloop()

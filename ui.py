from Tkinter import *

class App:

    def __init__(self, master):
        system  = StringVar()
        setting = StringVar()

        frame = Frame(master)
        frame.grid()

        Label(master, text = "Stats").grid(row = 0, column = 0, sticky=W)

        var1 = IntVar()
        Checkbutton(master, text="Strength", variable = var1).grid(row = 1, column = 0, sticky=W)

        var2 = IntVar()
        Checkbutton(master, text="Dexterity", variable = var2).grid(row = 2, column = 0, sticky=W)

        var3 = IntVar()
        Checkbutton(master, text="Intelligence", variable = var3).grid(row = 3, column = 0, sticky=W)

        var4 = IntVar()
        Checkbutton(master, text="Constitution", variable = var4).grid(row = 4, column = 0, sticky=W)

        var5 = IntVar()
        Checkbutton(master, text="Wisdom", variable = var5).grid(row = 5, column = 0, sticky=W)

        var6 = IntVar()
        Checkbutton(master, text="Charisma", variable = var6).grid(row = 6, column = 0, sticky=W)

        var7 = IntVar()
        Checkbutton(master, text="Psionics", variable = var7).grid(row = 7, column = 0, sticky=W)

        Label(master, text  = "System").grid(row = 0, column = 2, sticky=W)
        OptionMenu(master, system, "2d6", "4d6", "Dice").grid(row = 1, column = 2, sticky=W)

        Label(master, text = "Setting").grid(row = 2, column = 2, sticky=W)
        OptionMenu(master, setting, "Fantasy", "Science Fiction", "Real Life o.O").grid(row = 3, column = 2, sticky=W)

        Label(master, text = "Class").grid(row = 5, column = 2, sticky=W)

        self.getClass(setting)

    def getClass(self, setting):
        classes = open("classes.txt").read().splitlines()

    def submit(self):
        print("Chickity check yoself\n")

root = Tk()

app = App(root)

root.mainloop()
root.destroy()

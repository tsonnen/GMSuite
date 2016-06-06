from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.grid()

        Checkbutton(master, text="Strength", variable = valArray[0], 
            onvalue = "str", offvalue = 0).grid(row = 0, sticky=W)
        
        Checkbutton(master, text="Dexterity", variable = valArray[1],
            onvalue = "dex", offvalue = 0).grid(row = 1, sticky=W)
        
        Checkbutton(master, text="Intelligence", variable = valArray[2], 
            onvalue = "int", offvalue = 0).grid(row = 2, sticky=W)

        Checkbutton(master, text="Constitution", variable = valArray[3], 
            onvalue = "con", offvalue = 0).grid(row = 3, sticky=W)

        Checkbutton(master, text="Wisdom", variable = valArray[4], 
            onvalue = "wis", offvalue = 0).grid(row = 4, sticky=W)
        
        Checkbutton(master, text="Charisma", variable = valArray[5], 
            onvalue = "char", offvalue = 0).grid(row = 5, sticky=W)

        Button(frame, text="Submit", command = self.submit(valArray)).grid(row = 6, sticky=W)


    def submit(self, valArray):
        print(valArray)

root = Tk()

app = App(root)

root.mainloop()
root.destroy()

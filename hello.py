from Tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

##        items = ["Apple", "Banana", "Cherry"]
##        self.list = Listbox(frame, width=5, height=1)
##        for item in items:
##            self.list.insert(END, item)
##        self.list.pack(side=LEFT)

        fruit = StringVar()
        fruit.set(items[1])
        self.menu = OptionMenu(frame, fruit, *items)
        self.menu.pack(side=LEFT)

        self.entry = Entry(frame, width=8)
        self.entry.insert(0, items[2])
        self.entry.pack(side=LEFT)

root = Tk()
app = App(root)
root.mainloop()

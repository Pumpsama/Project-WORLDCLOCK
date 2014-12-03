from Tkinter import *

root = Tk()

text = Label(root, text="Patiparn Dork")
text.pack()

def dok():
    doks = Label(root, text="Dok Dok Dok")
    doks.pack()

def del_dok():
    doks.pack_forget()

button = Button(root, text="Click to Dork", command=dok)
button.pack()

button_stop = Button(root, text="Stop Dork", command=del_dok)
button_stop.pack()

root.mainloop()

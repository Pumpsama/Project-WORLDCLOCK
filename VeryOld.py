'''Thai to World Clock Project'''
#------------------------------------------------------------
#PSIT PROJECT 2014
#Language   : Pythom 2.7.8
#Author     : Pumpsama and Patiparn
#UI         : Tkinter
#GIT        : https://github.com/Pumpsama
#Repository : https://github.com/Pumpsama/Thai-to-World-Clock
#------------------------------------------------------------

from Tkinter import *

def user_interface(master):
    '''Make window of Tkinter'''
    master.geometry("400x600")
    master.option_add("*font", "Courier 15 bold")
    master.config(bg="#27281F")

    #! Label Head "Thai to World Clock"
    label_head = Label(master, text="Thai to World Clock", fg="#E70A5C", bg="#27281F")
    label_head.grid(row=0, columnspan=5)

    #! Line 1
    line1 = Frame(height=1, width=400, bg="green")
    line1.grid(row=1, columnspan=5, pady=3)

    #! Label and Input Box Hour
    label_hour = Label(master, text="Hours   : ", fg="#0AD2EB", bg="#27281F")
    label_hour.grid(row=2, column=2, sticky=W)               
    input_hour = Entry(master, width="2")
    input_hour.grid(row=2, column=2, sticky=E, padx=30)

    #! Label and Input Box Minute
    label_minute = Label(master, text="Minutes : ", fg="#0AD2EB", bg="#27281F")
    label_minute.grid(row=4, column=2, sticky=W)              
    input_minute = Entry(master, width="2")
    input_minute.grid(row=4, column=2, sticky=E, padx=30)

    #! Line 2
    line2 = Frame(height=1, width=400, bg="green")
    line2.grid(row=5, columnspan=5, pady=3)

    #! Execute Button
    execute = Button(height=1, width=33, text="Change Time", fg="white", bg="#009600")
    execute.grid(row=6, columnspan=5, sticky=E, pady=3)
    

    #! Line 3
    line3 = Frame(height=1, width=400, bg="green")
    line3.grid(row=7, columnspan=5, pady=3)

    #! Make Unresizeable
    master.resizable(0,0)

    #! Return GUI
    return master.mainloop()
user_interface(Tk())

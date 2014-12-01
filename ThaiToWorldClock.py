'''Thai to World Clock Project'''
#------------------------------------------------------------
#PSIT PROJECT 2014
#Language   : Python 2.7.8
#Author     : Pumpsama and Patiparn
#UI         : Tkinter
#GIT        : https://github.com/Pumpsama
#Repository : https://github.com/Pumpsama/Thai-to-World-Clock
#------------------------------------------------------------

from Tkinter import *

class Gui:
    '''Make window of Tkinter'''
    
    #INIT : Define a TK Gui and its properties
    master = Tk()   
    master.geometry("850x700")
    master.option_add("*font", "Courier 15 bold")
    master.config(bg="#27281F")
    
    #LINES : Defines Gui Lines
    line1 = Frame(height=1, width=850, bg="#E70A5C")
    line2 = Frame(height=1, width=850, bg="#E70A5C")
    line3 = Frame(height=1, width=850, bg="#E70A5C")

    #LABEL1 : Defines Text Label "Thai to World Clock"
    txthead = "Thai to World Clock"
    label_head = Label(master, text=txthead, fg="Red", bg="#27281F")    
    #LABEL2 : Defines Text Label "Hour :" In front of the Input Box
    txthour = "Hours   : "
    label_hour = Label(master, text=txthour, fg="#6495ED", bg="#27281F")           
    input_hour = Entry(master, width="2")
    #LABEL3 : Defines Text Label "Minutes :" In front of the Input Box
    txtmin = "Minutes : "
    label_minute = Label(master, text=txtmin, fg="#6495ED", bg="#27281F")
    input_minute = Entry(master, width="2")

    #FLAGS : Defines Flag Label (.gif files are required)
    thaiimg = PhotoImage(file=".\\Images\\thailand_flag.gif")
    flag_thai = Label(image=thaiimg, borderwidth=2.5, bg="#464646")
    usimg = PhotoImage(file=".\\Images\\us_flag.gif")
    flag_us = Label(image=usimg, borderwidth=2.5, bg="#464646")


    #INIT : Display everything except Button
    #Labels
    label_head.grid(row=0, columnspan=5)
    label_hour.grid(row=3, column=2, sticky=W, padx=70)
    label_minute.grid(row=4, column=2, sticky=W, padx=70)
    #Lines
    line1.grid(row=1, columnspan=5, pady=3)
    line2.grid(row=5, columnspan=5, pady=3)
    line3.grid(row=7, columnspan=5, pady=3)
    #Boxes
    input_hour.grid(row=3, column=2, sticky=E, padx=80)
    input_minute.grid(row=4, column=2, sticky=E, padx=80)
    #Flags
    flag_thai.grid(row=2, column=2, pady=5) 
    #Make Window unresizeable
    master.resizable(0,0)


class Button:
    '''Make Button of Tkinter'''
    
    #BUTTONS : Defines all Buttons
    #Reset
    txtreset = "Reset"
    reset = Button(height=1, width=22, text=txtreset, fg="white", bg="#27281F")  
    #Execute
    txtexec = "Change Time"
    execute = Button(height=1, width=25, text=txtexec, fg="white", bg="#C80000")  
    #Close
    txtclos = "Close"
    close = Button(height=1, width=22, text=txtclos, fg="white", bg="#27281F", command=Gui.master.quit())

    #INITS : Display all Button
    reset.grid(row=6, column=0, columnspan=5, sticky=W, pady=3)
    execute.grid(row=6, column=2, columnspan=5, sticky=W, padx=35, pady=3)
    close.grid(row=6, column=0, columnspan=5, sticky=E, pady=3)  


Gui.master.mainloop()

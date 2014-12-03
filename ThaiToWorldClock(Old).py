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
import sys

class Gui:
    '''Make window of Tkinter'''
    
    #INIT : Define a TK Gui and its properties
    master = Tk()
    master.wm_title("Thai Clock to World Clocks")
    master.geometry("900x685")
    master.option_add("*font", "Courier 15 bold")
    master.config(bg="#27281F")
    
    #LINES : Defines Gui Lines
    line1 = Frame(height=1, width=900, bg="#E70A5C")
    line2 = Frame(height=1, width=900, bg="#E70A5C")
    line3 = Frame(height=1, width=900, bg="#E70A5C")

    #LABEL1 : Defines Text Label "Thai to World Clock"
    txthead = "Thai Clock to World Clocks"
    label_head = Label(master, text=txthead, fg="Red", bg="#27281F")    
    #LABEL2 : Defines Text Label "Hour :" In front of the Input Box
    txthour = "Hours   : "
    label_hour = Label(master, text=txthour, fg="#6495ED", bg="#27281F")           
    input_hour = Entry(master, width="2")
    #LABEL3 : Defines Text Label "Minutes :" In front of the Input Box
    txtmin = "Minutes : "
    label_minute = Label(master, text=txtmin, fg="#6495ED", bg="#27281F")
    input_minute = Entry(master, width="2")
    #LABELS : All Output Flags
    label_aus = Label(master, text="Australia", fg="white", bg="#27281F")
    label_bra = Label(master, text="Brazil", fg="white", bg="#27281F")
    label_can = Label(master, text="Canada", fg="white", bg="#27281F")
    label_chi = Label(master, text="China", fg="white", bg="#27281F")
    label_egy = Label(master, text="Egypt", fg="white", bg="#27281F")
    label_ind = Label(master, text="India", fg="white", bg="#27281F")
    label_jap = Label(master, text="Japan", fg="white", bg="#27281F")
    label_kor = Label(master, text="South Korea", fg="white", bg="#27281F")
    label_uk = Label(master, text="United Kingdom", fg="white", bg="#27281F")
    label_us = Label(master, text="United States", fg="white", bg="#27281F")
    #LABELS : Output Times
    #Reset Button
    label_reset_1 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_2 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_3 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_4 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_5 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_6 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_7 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_8 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_9 = Label(master, text="-- : --", fg="white", bg="#27281F")
    label_reset_10 = Label(master, text="-- : --", fg="white", bg="#27281F")
    #Output Time
    label_time_1 = Label(master, text="11 : 11", fg="white", bg="#27281F")
    
    #FLAGS : Defines Flag Label (.gif files are required)
    #Thailand Flag
    thaiimg = PhotoImage(file=".\\Images\\thailand_flag.gif")
    flag_thai = Label(image=thaiimg, borderwidth=2.5, bg="#464646")
    #Output Flags
    ausimg = PhotoImage(file=".\\Images\\1_aus_flag.gif")
    flag_aus = Label(image=ausimg, borderwidth=0, bg="#464646")
    braimg = PhotoImage(file=".\\Images\\2_brazil_flag.gif")
    flag_bra = Label(image=braimg, borderwidth=0, bg="#464646")
    canimg = PhotoImage(file=".\\Images\\3_can_flag.gif")
    flag_can = Label(image=canimg, borderwidth=0, bg="#464646")
    chiimg = PhotoImage(file=".\\Images\\4_china_flag.gif")
    flag_chi = Label(image=chiimg, borderwidth=0, bg="#464646")
    egyimg = PhotoImage(file=".\\Images\\5_egypt_flag.gif")
    flag_egy = Label(image=egyimg, borderwidth=0, bg="#464646")
    indimg = PhotoImage(file=".\\Images\\6_india_flag.gif")
    flag_ind = Label(image=indimg, borderwidth=0, bg="#464646")
    japimg = PhotoImage(file=".\\Images\\7_japan_flag.gif")
    flag_jap = Label(image=japimg, borderwidth=0, bg="#464646")
    korimg = PhotoImage(file=".\\Images\\8_sthkorea_flag.gif")
    flag_kor = Label(image=korimg, borderwidth=0, bg="#464646")
    ukimg = PhotoImage(file=".\\Images\\9_uk_flag.gif")
    flag_uk = Label(image=ukimg, borderwidth=0, bg="#464646")    
    usimg = PhotoImage(file=".\\Images\\10_us_flag.gif")
    flag_us = Label(image=usimg, borderwidth=0, bg="#464646")

    #INIT : Display everything except Button
    #.Labels
    #..GUI
    label_head.grid(row=0, columnspan=5)
    label_hour.grid(row=3, column=2, sticky=W, padx=70)
    label_minute.grid(row=4, column=2, sticky=W, padx=70)
    #..Flags
    label_aus.grid(row=9, columnspan=5, sticky=W, padx=62, pady=0)
    label_bra.grid(row=9, columnspan=20, sticky=W, padx=300, pady=0)
    label_can.grid(row=9, columnspan=20, sticky=E, padx=300, pady=0)
    label_chi.grid(row=9, columnspan=5, sticky=E, padx=85, pady=0)
    label_egy.grid(row=13, columnspan=5, sticky=W, padx=85, pady=0)
    label_ind.grid(row=13, columnspan=20, sticky=E, padx=305, pady=0)
    label_jap.grid(row=13, columnspan=20, sticky=W, padx=305, pady=0)
    label_kor.grid(row=13, columnspan=5, sticky=E, padx=50, pady=0)
    label_uk.grid(row=17, columnspan=20, sticky=E, padx=250, pady=0)
    label_us.grid(row=17, columnspan=20, sticky=W, padx=255, pady=0)
    #..Resets
    label_reset_1.grid(row=10, columnspan=5, sticky=W, padx=72, pady=0)
    label_reset_2.grid(row=10, columnspan=5, sticky=W, padx=293, pady=0)
    label_reset_3.grid(row=10, columnspan=5, sticky=E, padx=293, pady=0)
    label_reset_4.grid(row=10, columnspan=5, sticky=E, padx=72, pady=0)
    label_reset_5.grid(row=14, columnspan=5, sticky=W, padx=72, pady=0)
    label_reset_6.grid(row=14, columnspan=5, sticky=W, padx=293, pady=0)
    label_reset_7.grid(row=14, columnspan=5, sticky=E, padx=293, pady=0)
    label_reset_8.grid(row=14, columnspan=5, sticky=E, padx=72, pady=0)
    label_reset_9.grid(row=18, columnspan=5, sticky=W, padx=293, pady=0)
    label_reset_10.grid(row=18, columnspan=5, sticky=E, padx=293, pady=0)
    #Lines
    line1.grid(row=1, columnspan=5, pady=3)
    line2.grid(row=5, columnspan=5, pady=8)
    line3.grid(row=7, columnspan=5, pady=8)
    #Boxes
    input_hour.grid(row=3, column=2, sticky=E, padx=80)
    input_minute.grid(row=4, column=2, sticky=E, padx=80)
    #Flags
    #Thailand Flags
    flag_thai.grid(row=2, column=2, pady=5)
    #Output Flags
    flag_aus.grid(row=8, columnspan=5, sticky=W, padx=80, pady=15)
    flag_bra.grid(row=8, columnspan=20, sticky=W, padx=300, pady=15)
    flag_can.grid(row=8, columnspan=40, sticky=E, padx=300, pady=15)
    flag_chi.grid(row=8, columnspan=5, sticky=E, padx=80, pady=15)
    flag_egy.grid(row=12, columnspan=20, sticky=W, padx=80, pady=15)
    flag_ind.grid(row=12, columnspan=40, sticky=E, padx=300, pady=15)
    flag_jap.grid(row=12, columnspan=5, sticky=W, padx=300, pady=15)
    flag_kor.grid(row=12, columnspan=20, sticky=E, padx=80, pady=15)
    flag_uk.grid(row=16, columnspan=40, sticky=E, padx=300, pady=15)
    flag_us.grid(row=16, columnspan=100, sticky=W, padx=300, pady=15)
    #Make Window unresizeable
    master.resizable(0,0)


class Button:
    '''Make Button of Tkinter'''
    
    #BUTTONS : Defines all Buttons
    #.Reset
    def reset():
        Gui.label_reset_1.grid(row=10, columnspan=5, sticky=W, padx=72, pady=0)
        Gui.label_reset_2.grid(row=10, columnspan=5, sticky=W, padx=293, pady=0)
        Gui.label_reset_3.grid(row=10, columnspan=5, sticky=E, padx=293, pady=0)
        Gui.label_reset_4.grid(row=10, columnspan=5, sticky=E, padx=72, pady=0)
        Gui.label_reset_5.grid(row=14, columnspan=5, sticky=W, padx=72, pady=0)
        Gui.label_reset_6.grid(row=14, columnspan=5, sticky=W, padx=293, pady=0)
        Gui.label_reset_7.grid(row=14, columnspan=5, sticky=E, padx=293, pady=0)
        Gui.label_reset_8.grid(row=14, columnspan=5, sticky=E, padx=72, pady=0)
        Gui.label_reset_9.grid(row=18, columnspan=5, sticky=W, padx=293, pady=0)
        Gui.label_reset_10.grid(row=18, columnspan=5, sticky=E, padx=293, pady=0)
        Gui.label_time_1.grid_forget()
    txtreset = "Reset"
    reset = Button(height=1, width=24, text=txtreset, fg="white", bg="#27281F", command=reset)
    #.Execute
    def execute():
        Gui.label_time_1.grid(row=10, columnspan=5, sticky=W, padx=72, pady=0)
        Gui.label_reset_1.grid_forget()
    txtexec = "Change Time"
    execute = Button(height=1, width=26, text=txtexec, fg="white", bg="#C80000", command=execute)
    #.Close
    def close():
        Gui.master.quit()
    txtclos = "Close"
    close = Button(height=1, width=24, text=txtclos, fg="white", bg="#27281F", command=close)

    #INITS : Display all Button
    reset.grid(row=6, column=0, columnspan=5, sticky=W, pady=3)
    execute.grid(row=6, column=2, columnspan=5, sticky=W, padx=35, pady=3)
    close.grid(row=6, column=0, columnspan=5, sticky=E, pady=3)  


Gui.master.mainloop()

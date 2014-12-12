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
from time import strftime
<<<<<<< HEAD:ThaiToWorldClock (Windows & Linux).py
from winsound import PlaySound, SND_FILENAME
=======
>>>>>>> origin/master:ThaiToWorldClock (Windows & Linux).py

class Gui:
    '''Make window of Tkinter'''
    
    #INIT : Define a TK Gui and its properties
    master = Tk()
    master.wm_title("Thai Clock to World Clocks")
    master.geometry("900x700")
    master.option_add("*font", "Courier 14 bold")
    master.config(bg="#27281F")
    
    #LINES : Defines Gui Lines
    line1 = Frame(height=2, width=900, bg="Red")
    line2 = Frame(height=2, width=900, bg="Red")
    line3 = Frame(height=2, width=900, bg="Red")

    #LABEL1 : Defines Text Label "Thai to World Clock"
    txthead = "Thai Clock to World Clocks"
    label_head = Label(master, text=txthead, fg="Red", bg="#27281F")    
    #LABEL2 : Defines Text Label "Hour :" In front of the Input Box
    txthour = "Hours   : "
    label_hour = Label(master, text=txthour, fg="#6495ED", bg="#27281F")
    input_hour = Spinbox(master, width=3, borderwidth=0, \
                         from_=0, to=23, fg="#6495ED", bg="#27281F")
    #LABEL3 : Defines Text Label "Minutes :" In front of the Input Box
    txtmin = "Minutes : "
    label_minute = Label(master, text=txtmin, fg="#6495ED", bg="#27281F")
    input_minute = Spinbox(master, width=3, borderwidth=0, \
                           from_=0, to=59, fg="#6495ED", bg="#27281F")
    #LABEL4 : Defines Author Name
    txtauthor = "by Pumpsama & Palmkung"
    label_author = Label(master, text=txtauthor, fg="white", bg="#27281F")
    #LABELS : All Output Flags
    label_aus = Label(master, text="Australia\n(Canberra)", fg="white", bg="#27281F")
    label_bra = Label(master, text="Brazil\n(Brasillia)", fg="white", bg="#27281F")
    label_can = Label(master, text="Canada\n(Toronto)", fg="white", bg="#27281F")
    label_chi = Label(master, text="China", fg="white", bg="#27281F")
    label_egy = Label(master, text="Egypt", fg="white", bg="#27281F")
    label_ind = Label(master, text="India", fg="white", bg="#27281F")
    label_jap = Label(master, text="Japan", fg="white", bg="#27281F")
    label_kor = Label(master, text="South Korea", fg="white", bg="#27281F")
    label_uk = Label(master, text="United Kingdom", fg="white", bg="#27281F")
    label_us = Label(master, text="United States\n(Washington D.C.)", fg="white", bg="#27281F")
    label_us_keynote = Label(master, text="Apple Keynote\n(U.S. California)", fg="white", bg="#27281F")
    #LABELS : Reset Button
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
    label_reset_11 = Label(master, text="-- : --", fg="white", bg="#27281F")    
    #FLAGS : Defines Flag Label (.gif files are required)
    #Thailand Flag
    thaiimg = PhotoImage(file=".//Images//thailand_flag.gif")
    flag_thai = Label(image=thaiimg, borderwidth=0, bg="#464646")
    #Output Flags
    ausimg = PhotoImage(file=".//Images//1_aus_flag.gif")
    flag_aus = Label(image=ausimg, borderwidth=0)
    braimg = PhotoImage(file=".//Images//2_brazil_flag.gif")
    flag_bra = Label(image=braimg, borderwidth=0)
    canimg = PhotoImage(file=".//Images//3_can_flag.gif")
    flag_can = Label(image=canimg, borderwidth=0)
    chiimg = PhotoImage(file=".//Images//4_china_flag.gif")
    flag_chi = Label(image=chiimg, borderwidth=0)
    egyimg = PhotoImage(file=".//Images//5_egypt_flag.gif")
    flag_egy = Label(image=egyimg, borderwidth=0)
    indimg = PhotoImage(file=".//Images//6_india_flag.gif")
    flag_ind = Label(image=indimg, borderwidth=0)
    japimg = PhotoImage(file=".//Images//7_japan_flag.gif")
    flag_jap = Label(image=japimg, borderwidth=0)
    korimg = PhotoImage(file=".//Images//8_sthkorea_flag.gif")
    flag_kor = Label(image=korimg, borderwidth=0)
    ukimg = PhotoImage(file=".//Images//9_uk_flag.gif")
    flag_uk = Label(image=ukimg, borderwidth=0)    
    usimg = PhotoImage(file=".//Images//10_us_flag.gif")
    flag_us = Label(image=usimg, borderwidth=0)
    appimg = PhotoImage(file=".//Images//11_applekeynote.gif")
    flag_us_keynote = Label(image=appimg, borderwidth=0)

    #INIT : Display everything except Button
    #.Labels
    #..GUI Labels
    label_head.grid(row=0, columnspan=5)
    label_hour.grid(row=3, columnspan=20, sticky=W, padx=350)
    label_minute.grid(row=4, columnspan=100, sticky=W, padx=350)
    #label_author.grid(row=6, column=0, columnspan=5, sticky=W, padx=5)
    #..Resets Labels
    label_reset_1.grid(row=10, columnspan=5, sticky=W, padx=72, pady=0)
    label_reset_2.grid(row=10, columnspan=5, sticky=W, padx=293, pady=0)
    label_reset_3.grid(row=10, columnspan=5, sticky=E, padx=293, pady=0)
    label_reset_4.grid(row=10, columnspan=5, sticky=E, padx=72, pady=0)
    label_reset_5.grid(row=14, columnspan=5, sticky=W, padx=72, pady=0)
    label_reset_6.grid(row=14, columnspan=5, sticky=W, padx=293, pady=0)
    label_reset_7.grid(row=14, columnspan=5, sticky=E, padx=293, pady=0)
    label_reset_8.grid(row=14, columnspan=5, sticky=E, padx=72, pady=0)
    label_reset_9.grid(row=18, columnspan=5, sticky=W, padx=178, pady=0)
    label_reset_10.grid(row=18, columnspan=5, sticky=W, padx=400, pady=0)
    label_reset_11.grid(row=18, columnspan=5, sticky=E, padx=178, pady=0)
    #..Flags Labels
    label_aus.grid(row=9, columnspan=5, sticky=W, padx=60, pady=0)
    label_bra.grid(row=9, columnspan=20, sticky=W, padx=275, pady=0)
    label_can.grid(row=9, columnspan=20, sticky=E, padx=285, pady=0)
    label_chi.grid(row=9, columnspan=5, sticky=E, padx=85, pady=0)
    label_egy.grid(row=13, columnspan=5, sticky=W, padx=85, pady=0)
    label_ind.grid(row=13, columnspan=20, sticky=W, padx=305, pady=0)
    label_jap.grid(row=13, columnspan=20, sticky=E, padx=305, pady=0)
    label_kor.grid(row=13, columnspan=5, sticky=E, padx=50, pady=0)
    label_uk.grid(row=17, columnspan=20, sticky=W, padx=140, pady=0)
    label_us.grid(row=17, columnspan=20, sticky=W, padx=350, pady=0)
    label_us_keynote.grid(row=17, columnspan=20, sticky=E, padx=120, pady=0)
    #Lines
    line1.grid(row=1, columnspan=5, pady=4)
    line2.grid(row=5, columnspan=5, pady=4)
    line3.grid(row=7, columnspan=5, pady=4)
    #Inputs
    input_hour.grid(row=3, column=2, sticky=E, padx=80)
    input_minute.grid(row=4, column=2, sticky=E, padx=80)
    #Flags Images
    #Thailand Flags Image
    flag_thai.grid(row=2, column=2, pady=5)
    #Output Flags Images
    flag_aus.grid(row=8, columnspan=5, sticky=W, padx=75, pady=15)
    flag_bra.grid(row=8, columnspan=20, sticky=W, padx=297, pady=15)
    flag_can.grid(row=8, columnspan=40, sticky=E, padx=297, pady=15)
    flag_chi.grid(row=8, columnspan=5, sticky=E, padx=75, pady=15)
    flag_egy.grid(row=12, columnspan=20, sticky=W, padx=75, pady=15)
    flag_ind.grid(row=12, columnspan=40, sticky=W, padx=297, pady=15)
    flag_jap.grid(row=12, columnspan=5, sticky=E, padx=297, pady=15)
    flag_kor.grid(row=12, columnspan=20, sticky=E, padx=75, pady=15)
    flag_uk.grid(row=16, columnspan=40, sticky=W, padx=180, pady=15)
    flag_us.grid(row=16, columnspan=100, sticky=W, padx=405, pady=15)
    flag_us_keynote.grid(row=16, columnspan=100, sticky=E, padx=180, pady=15)
    #Make Window unresizeable
    master.resizable(0,0)

class Button:
    '''Make buttons of Tkinter'''
    
    #BUTTONS : Defines all Buttons
    #.Execute
    def execute_current():
        '''Show all time output using current time'''
<<<<<<< HEAD:ThaiToWorldClock (Windows & Linux).py
        
=======
>>>>>>> origin/master:ThaiToWorldClock (Windows & Linux).py
        #Get current time
        hour = int(strftime("%H"))
        minu = str(("0" * (2 - len(strftime("%M")))) + strftime("%M"))
        
        #.Australia
        hour1 = str((hour + 4) % 24)
        hour1 = ("0" * (2 - len(hour1))) + str(hour1)
        label_time_1 = Label(Gui.master, text=hour1 + " : " + str(minu), fg="white", bg="#27281F")
        #.Brazil
        hour2 = str((hour - 9) % 24)
        hour2 = ("0" * (2 - len(hour2))) + str(hour2)
        label_time_2 = Label(Gui.master, text=hour2 + " : " + str(minu), fg="white", bg="#27281F")
        #.Canada
        hour3 = str((hour - 12) % 24)
        hour3 = ("0" * (2 - len(hour3))) + str(hour3)
        label_time_3 = Label(Gui.master, text=hour3 + " : " + str(minu), fg="white", bg="#27281F")
        #.China
        hour4 = str((hour + 1) % 24)
        hour4 = ("0" * (2 - len(hour4))) + str(hour4)
        label_time_4 = Label(Gui.master, text=hour4 + " : " + str(minu), fg="white", bg="#27281F")
        #.Egypt
        hour5 = str((hour - 5) % 24)
        hour5 = ("0" * (2 - len(hour5))) + str(hour5)
        label_time_5 = Label(Gui.master, text=hour5 + " : " + str(minu), fg="white", bg="#27281F")
        #.India
        hour6 = str((hour - 2) % 24)
        hour6 = ("0" * (2 - len(hour6))) + str(hour6)
        label_time_6 = Label(Gui.master, text=hour6 + " : " + str(minu), fg="white", bg="#27281F")
        #.Japan
        hour7 = str((hour + 2) % 24)
        hour7 = ("0" * (2 - len(hour7))) + str(hour7)
        label_time_7 = Label(Gui.master, text=hour7 + " : " + str(minu), fg="white", bg="#27281F")
        #.South Korea
        hour8 = str((hour + 2) % 24)
        hour8 = ("0" * (2 - len(hour8))) + str(hour8)
        label_time_8 = Label(Gui.master, text=hour8 + " : " + str(minu), fg="white", bg="#27281F")
        #.United Kingdom
        hour9 = str((hour - 7) % 24)
        hour9 = ("0" * (2 - len(hour9))) + str(hour9)
        label_time_9 = Label(Gui.master, text=hour9 + " : " + str(minu), fg="white", bg="#27281F")        
        #.United States
        hour10 = str((hour - 12) % 24)
        hour10 = ("0" * (2 - len(hour10))) + str(hour10)
        label_time_10 = Label(Gui.master, text=hour10 + " : " + str(minu), fg="white", bg="#27281F")
        #.United States (Apple Keynote)
        hour11 = str((hour - 15) % 24)
        hour11 = ("0" * (2 - len(hour11))) + str(hour11)
        label_time_11 = Label(Gui.master, text=hour11 + " : " + str(minu), fg="white", bg="#27281F")
        
        label_time_1.grid(row=10, columnspan=5, sticky=W, padx=72, pady=0)
        label_time_2.grid(row=10, columnspan=5, sticky=W, padx=293, pady=0)
        label_time_3.grid(row=10, columnspan=5, sticky=E, padx=293, pady=0)
        label_time_4.grid(row=10, columnspan=5, sticky=E, padx=72, pady=0)
        label_time_5.grid(row=14, columnspan=5, sticky=W, padx=72, pady=0)
        label_time_6.grid(row=14, columnspan=5, sticky=W, padx=293, pady=0)
        label_time_7.grid(row=14, columnspan=5, sticky=E, padx=293, pady=0)
        label_time_8.grid(row=14, columnspan=5, sticky=E, padx=72, pady=0)
        label_time_9.grid(row=18, columnspan=5, sticky=W, padx=178, pady=0)
        label_time_10.grid(row=18, columnspan=5, sticky=W, padx=400, pady=0)
        label_time_11.grid(row=18, columnspan=5, sticky=E, padx=178, pady=0)
        #Hide -- : --
        Gui.label_reset_1.grid_forget()
        Gui.label_reset_2.grid_forget()
        Gui.label_reset_3.grid_forget()
        Gui.label_reset_4.grid_forget()
        Gui.label_reset_5.grid_forget()
        Gui.label_reset_6.grid_forget()
        Gui.label_reset_7.grid_forget()
        Gui.label_reset_8.grid_forget()
        Gui.label_reset_9.grid_forget()
        Gui.label_reset_10.grid_forget()
<<<<<<< HEAD:ThaiToWorldClock (Windows & Linux).py

=======
>>>>>>> origin/master:ThaiToWorldClock (Windows & Linux).py
    txtexecnow = "Convert using current time"
    executenow = Button(height=1, width=41, borderwidth=0, text=txtexecnow, fg="white", bg="#3CB371", command=execute_current)
    
    #.Execute with time input
    def execute_withset():
        '''Show all time output using input time'''
<<<<<<< HEAD:ThaiToWorldClock (Windows & Linux).py
        
        #Play Sound
        PlaySound('.//Sound//convert_win.wav', SND_FILENAME)
        
=======
>>>>>>> origin/master:ThaiToWorldClock (Windows & Linux).py
        #Get time from inputs
        hour = int(Gui.input_hour.get())
        minu = str(("0" * (2 - len(Gui.input_minute.get()))) + Gui.input_minute.get())
        
        #.Australia
        hour1 = str((hour + 4) % 24)
        hour1 = ("0" * (2 - len(hour1))) + str(hour1)
        label_time_1 = Label(Gui.master, text=hour1 + " : " + str(minu), fg="white", bg="#27281F")
        #.Brazil
        hour2 = str((hour - 9) % 24)
        hour2 = ("0" * (2 - len(hour2))) + str(hour2)
        label_time_2 = Label(Gui.master, text=hour2 + " : " + str(minu), fg="white", bg="#27281F")
        #.Canada
        hour3 = str((hour - 12) % 24)
        hour3 = ("0" * (2 - len(hour3))) + str(hour3)
        label_time_3 = Label(Gui.master, text=hour3 + " : " + str(minu), fg="white", bg="#27281F")
        #.China
        hour4 = str((hour + 1) % 24)
        hour4 = ("0" * (2 - len(hour4))) + str(hour4)
        label_time_4 = Label(Gui.master, text=hour4 + " : " + str(minu), fg="white", bg="#27281F")
        #.Egypt
        hour5 = str((hour - 5) % 24)
        hour5 = ("0" * (2 - len(hour5))) + str(hour5)
        label_time_5 = Label(Gui.master, text=hour5 + " : " + str(minu), fg="white", bg="#27281F")
        #.India
        hour6 = str((hour - 2) % 24)
        hour6 = ("0" * (2 - len(hour6))) + str(hour6)
        label_time_6 = Label(Gui.master, text=hour6 + " : " + str(minu), fg="white", bg="#27281F")
        #.Japan
        hour7 = str((hour + 2) % 24)
        hour7 = ("0" * (2 - len(hour7))) + str(hour7)
        label_time_7 = Label(Gui.master, text=hour7 + " : " + str(minu), fg="white", bg="#27281F")
        #.South Korea
        hour8 = str((hour + 2) % 24)
        hour8 = ("0" * (2 - len(hour8))) + str(hour8)
        label_time_8 = Label(Gui.master, text=hour8 + " : " + str(minu), fg="white", bg="#27281F")
        #.United Kingdom
        hour9 = str((hour - 7) % 24)
        hour9 = ("0" * (2 - len(hour9))) + str(hour9)
        label_time_9 = Label(Gui.master, text=hour9 + " : " + str(minu), fg="white", bg="#27281F")        
        #.United States
        hour10 = str((hour - 12) % 24)
        hour10 = ("0" * (2 - len(hour10))) + str(hour10)
        label_time_10 = Label(Gui.master, text=hour10 + " : " + str(minu), fg="white", bg="#27281F")
        #.United States (Apple Keynote)
        hour11 = str((hour - 15) % 24)
        hour11 = ("0" * (2 - len(hour11))) + str(hour11)
        label_time_11 = Label(Gui.master, text=hour11 + " : " + str(minu), fg="white", bg="#27281F")
        
        label_time_1.grid(row=10, columnspan=5, sticky=W, padx=72, pady=0)
        label_time_2.grid(row=10, columnspan=5, sticky=W, padx=293, pady=0)
        label_time_3.grid(row=10, columnspan=5, sticky=E, padx=293, pady=0)
        label_time_4.grid(row=10, columnspan=5, sticky=E, padx=72, pady=0)
        label_time_5.grid(row=14, columnspan=5, sticky=W, padx=72, pady=0)
        label_time_6.grid(row=14, columnspan=5, sticky=W, padx=293, pady=0)
        label_time_7.grid(row=14, columnspan=5, sticky=E, padx=293, pady=0)
        label_time_8.grid(row=14, columnspan=5, sticky=E, padx=72, pady=0)
        label_time_9.grid(row=18, columnspan=5, sticky=W, padx=178, pady=0)
        label_time_10.grid(row=18, columnspan=5, sticky=W, padx=400, pady=0)
        label_time_11.grid(row=18, columnspan=5, sticky=E, padx=178, pady=0)
        #Hide -- : --
        Gui.label_reset_1.grid_forget()
        Gui.label_reset_2.grid_forget()
        Gui.label_reset_3.grid_forget()
        Gui.label_reset_4.grid_forget()
        Gui.label_reset_5.grid_forget()
        Gui.label_reset_6.grid_forget()
        Gui.label_reset_7.grid_forget()
        Gui.label_reset_8.grid_forget()
        Gui.label_reset_9.grid_forget()
        Gui.label_reset_10.grid_forget()

    txtexec = "Convert using input time"
    execute = Button(height=1, width=41, borderwidth=0, text=txtexec, fg="white", bg="#C80000", command=execute_withset)
    
    #INITS : Display all Button
    executenow.grid(row=6, columnspan=5, sticky=W, pady=0)
    execute.grid(row=6, columnspan=300, sticky=E, padx=0)

Gui.master.mainloop()

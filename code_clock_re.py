class Clock():
    hour = int(raw_input())
    minute = int(raw_input())
#print Clock.hour, Clock.minute

def world():
    '''Change Thailand Time to World time'''
    
    #to fix lenght of hour and minute
    lenhour = "0" * (2 - int(len(str(Clock.hour))))
    lenmin = "0" * (2 - int(len(str(Clock.minute))))
    #Australia(Canberra, Melbern) to Thailand (+2 hr.)
    print "Australia(Canberra, Melbern) " + str(lenhour) + str((Clock.hour + 2) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Brazil(Brazilia) " + str(lenhour) + str((Clock.hour + 10) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Canada(Toronto) " + str(lenhour) + str((Clock.hour - 12) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "China " + str(lenhour) + str((Clock.hour + 1) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Denmark " + str(lenhour) + str((Clock.hour - 6) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Egypt " + str(lenhour) + str((Clock.hour - 5) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "France " + str(lenhour) + str((Clock.hour - 6) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "German " + str(lenhour) + str((Clock.hour - 6) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Greece " + str(lenhour) + str((Clock.hour - 5) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Hawaii " + str(lenhour) + str((Clock.hour - 12) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Hong Kong " + str(lenhour) + str((Clock.hour + 1) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "India " + str(lenhour) + str((Clock.hour + 1) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Japan " + str(lenhour) + str((Clock.hour - 2) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Mexico " + str(lenhour) + str((Clock.hour - 13) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Netherland " + str(lenhour) + str((Clock.hour - 6) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "New Zeland" + str(lenhour) + str((Clock.hour + 5) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Noway " + str(lenhour) + str((Clock.hour - 6) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Poland " + str(lenhour) + str((Clock.hour - 6) % 23) + ":" + str(lenmin) + str(Clock.minute)
    print "Portugal " + str(lenhour) + str((Clock.hour - 7) % 23) + ":" + str(lenmin) + str(Clock.minute)
print world()

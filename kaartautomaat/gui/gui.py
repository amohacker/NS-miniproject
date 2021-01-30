from tkinter import *
from tkinter import Label
from typing import List

from kaartautomaat.logic.Apirequester import *
from kaartautomaat.logic.getCode import *

def Start():

    def toonDepartureframe():
        loaddepartures()
        departureInformatieframe.pack()

    def veranderStation():
        naam = departurelocatieinvoer.get()
        departureframe.pack_forget()
        unloaddepartures()
        departureframe.pack()
        code = getCode(naam)
        loaddepartures(code)

    def unloaddepartures():
        i = 0
        for i in departurelijst:
            for i2 in i:
                i2.destroy()
        for i in departurebackgrounds:
            i.destroy()

    root = Tk()

    departureInformatieframe = Frame(master=root)
    departureInformatieframe.pack(fill="both", expand=True)
    departuremenubarframe = Frame(master=departureInformatieframe)
    departuremenubarframe.pack(fill="x", expand=True)
    departureconfirmknop = Button(master=departuremenubarframe, text="OK", background="blue", foreground="white", command=veranderStation) #Misschien wisselen naar dictionarys per scherm met gui items
    departureconfirmknop.pack(side=RIGHT, pady=4, padx=4)
    departurelocatieinvoer = Entry(master=departuremenubarframe, width=20)
    departurelocatieinvoer.insert(0, huidigStation())
    departurelocatieinvoer.pack(side=RIGHT, pady=4, padx=4)
    departureframe = Frame(master=departureInformatieframe)
    departureframe.pack(fill="both", expand=True)
    departurelijst: List[List[Label]] = []
    departurebackgrounds = []

    def loaddepartures(station=huidigStation()):
        departurebackgrounds.clear()
        departurebackgrounds.append(Frame(master=departureframe, bg='cyan', width='600', height='30'))
        departurebackgrounds[0].grid(row=0, column=0, columnspan=4)
        departurelijst.clear()
        departurelijst.append([
            Label(master=departureframe, text='Vertrek', background='cyan'),
            Label(master=departureframe, text='Naar', background='cyan'),
            Label(master=departureframe, text='Spoor', background='cyan'),
            Label(master=departureframe, text='Trein', background='cyan')])
        departurelijst[0][0].grid(row=0, column=0, pady=4, padx=10)
        departurelijst[0][1].grid(row=0, column=1, pady=4, padx=10)
        departurelijst[0][2].grid(row=0, column=2, pady=4, padx=10)
        departurelijst[0][3].grid(row=0, column=3, pady=4, padx=10)
        departures = getDepartures(station)
        i = 1
        for departure in departures:
            if i%2 == 0:
                colour='cyan'
            else:
                colour='white'
            departurebackgrounds.append(Canvas(master=departureframe, bg=colour, width='600', height='30'))

            departurebackgrounds[i].grid(row=i, column=0, columnspan=4)
            departurelijst.append([Label(master=departureframe, background=colour, text=departure['tijd'][-13:-5]),
                                   Label(master=departureframe, background=colour, text=departure['bestemming']),
                                   Label(master=departureframe, background=colour, text=departure['spoor']),
                                   Label(master=departureframe, background=colour, text=departure['type'])])
            i2 = 0

            for x in departurelijst[i]:
                x.grid(row=i, column=i2, pady=4, padx=10)
                i2 +=1
            i += 1

    toonDepartureframe()
    root.mainloop()

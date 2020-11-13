from tkinter import *
from kaartautomaat.logic.Apirequester import *

def Start():

    def toonHoofdframe():
        unloaddepartures()
        departureInformatieframe.pack_forget()
        #reisinfoselectframe.pack_forget()
        hooftframe.pack()

    #    def toonInfoSubframe():
    #        hooftframe.pack_forget()
    #        reisinfoselectframe.pack()

    def toonDepartureframe():
        #reisinfoselectframe.pack_forget()
        hooftframe.pack_forget()
        loaddepartures()
        departureInformatieframe.pack()

    def veranderStation():
        locatie = departurelocatieinvoer.get()
        departureframe.pack_forget()
        unloaddepartures()
        departureframe.pack()
        loaddepartures(locatie)

    def unloaddepartures():
        i = 0
        while i < len(departurelijst)-1:
            for i2 in departurelijst[i+1]:
                i2.pack_forget()
                i2.destroy()
            departurelijst.clear()
            i += 1
        for i in departurebackgrounds:
            i.pack_forget()
            i.destroy()
        departurebackgrounds.clear()

    root = Tk()

    hooftframe = Frame(master=root, background='yellow')
    hooftframe.pack(fill="both", expand=True)
    hooftbutton1 = Button(master=hooftframe, text="Kaarten bestellen", background="blue", foreground="white")
    hooftbutton1.pack(side=LEFT, pady=60, padx=4)
    hooftbutton2 = Button(master=hooftframe, text="Bestelling ophalen", background="blue", foreground="white")
    hooftbutton2.pack(side=LEFT, pady=60, padx=4)
    hooftbutton3 = Button(master=hooftframe, text="Opwaarderen", background="blue", foreground="white")
    hooftbutton3.pack(side=LEFT, pady=60, padx=4)
    hooftbutton4 = Button(master=hooftframe, text="Reisinformatie", background="blue", foreground="white", command=toonDepartureframe)
    hooftbutton4.pack(side=LEFT, pady=60, padx=4)

    #eventueel frame om verschillende soorten informatie te selecteren
    #reisinfoselectframe = Frame(master=root, background='yellow')
    #reisinfoselectframe.pack(fill="both", expand=True)
    #selectbutton1 = Button(master=reisinfoselectframe, text="Vertrektijden", background="blue", foreground="white", command=toonDepartureframe)
    #selectbutton1.pack(side=TOP, pady=4, padx=60)

    departureInformatieframe = Frame(master=root)
    departureInformatieframe.pack(fill="both", expand=True)
    departuremenubarframe = Frame(master=departureInformatieframe)
    departuremenubarframe.pack(fill="x", expand=True)
    departureterugknop = Button(master=departuremenubarframe, text="Terug", background="blue", foreground="white", command=toonHoofdframe)
    departureterugknop.pack(side=LEFT, pady=4, padx=4)
    departureconfirmknop = Button(master=departuremenubarframe, text="OK", background="blue", foreground="white", command=veranderStation) #Misschien wisselen naar dictionarys per scherm met gui items
    departureconfirmknop.pack(side=RIGHT, pady=4, padx=4)
    departurelocatieinvoer = Entry(master=departuremenubarframe, width=20)
    departurelocatieinvoer.insert(0, huidigStation())
    departurelocatieinvoer.pack(side=RIGHT, pady=4, padx=4)
    departureframe = Frame(master=departureInformatieframe)
    departureframe.pack(fill="both", expand=True)
    departurelijst = []
    departurebackgrounds = []

    def loaddepartures(station=huidigStation()):
        departurebackgrounds = [Frame(master=departureframe, bg='cyan', width='600', height='30')]
        departurebackgrounds[0].grid(row=0, column=0, columnspan=4)
        departurelijst = [[
            Label(master=departureframe, text='Vertrek', background='cyan'),
            Label(master=departureframe, text='Naar', background='cyan'),
            Label(master=departureframe, text='Spoor', background='cyan'),
            Label(master=departureframe, text='Trein', background='cyan')]]
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


    toonHoofdframe()
    root.mainloop()

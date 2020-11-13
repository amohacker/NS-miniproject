from tkinter import *
from treeTest.logic.testlogic1 import *

def clicked():
    grondtal = int(entry.get())
    kwadraat = kwadrateer(grondtal)
    tekst = "kwadraat: van {} = {}"
    label["text"] = tekst.format(grondtal, kwadraat)

def clicked2():
    grondtal = int(entry.get())
    tekst = "wortel: van {} = {}"
    label["text"] = tekst.format(grondtal, wortel(grondtal))

root = Tk()

label = Label(master=root, text='Hello World', height=3)
label.pack()

button = Button(master=root, text='Kwadraat', command=clicked)
button.pack(pady=10)

button2 = Button(master=root, text='Wortel', command=clicked2)
button2.pack(pady=10)


entry = Entry(master=root)
entry.pack(padx=10, pady=10)


root.mainloop()
from tkinter import *
from treeTest.logic.testlogic1 import *

def clicked():
    button2.destroy()

def clicked2():
    pass

root = Tk()

label = Label(master=root, text='Hello World', height=3)
label.grid()

button = Button(master=root, text='Kwadraat', command=clicked)
button.grid(pady=10)

button2 = Button(master=root, text='Wortel', command=clicked2)
button2.grid(pady=10)


entry = Entry(master=root)
entry.grid(padx=10, pady=10)


root.mainloop()
from tkinter import *
from tkinter.messagebox import showinfo

def clicked():
    bericht = 'Dit is een bericht voor de gebruiker!'
    showinfo(title='poppup', message=bericht)

root = Tk()
button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

root.mainloop()
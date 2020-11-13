from tkinter import *

def clicked():
    label["text"] = entry.get()

root = Tk()

label = Label(master=root, text='Hello World', height=3)
label.pack()

button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)


root.mainloop()
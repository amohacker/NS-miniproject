from tkinter import *

root = Tk()
label = Label(master=root, text='Hello World', height=3)
label.pack()

button = Button(master=root, text='Druk hier')
button.pack(pady=10) #pady zorgt voor een padding op y dus pady=10 zorgt voor een ruimte van 10 pixels

entry = Entry(master=root)
entry.pack(padx=10, pady=10)    #dit zoort tkinter objecten heten widgets


root.mainloop()
from tkinter import *

root = Tk()

linkerframe = Frame(master=root)
linkerframe.pack(side=LEFT)

button1 = Button(master=linkerframe, text='Button 1')
button1.pack(pady=4)

button2 = Button(master=linkerframe, text='Button 2')
button2.pack(pady=4)

button3 = Button(master=root, text='Button 3')
button3.pack(side=RIGHT, pady=4)

root.mainloop()
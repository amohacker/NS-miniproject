from tkinter import *

root = Tk()

button1 = Button(master=root, text='Button 1')
button1.grid(row=0, column=0, pady=4)

button2 = Button(master=root, text='Button 2')
button2.grid(row=1, column=0, pady=4)

button3 = Button(master=root, text='Button 3')
button3.grid(row=0, column=1, pady=4)

root.mainloop()
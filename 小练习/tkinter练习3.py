# Author:ZJF
from tkinter import *
window = Tk()
window.geometry("500x300")
window.title("My Window")
e1 = Entry(window, show="*", font=("Arial", 14))
var = StringVar()
e2 = Entry(window, show=None, font=("Arial", 14), textvariable=var)
e1.pack()
e2.pack()

window.mainloop()
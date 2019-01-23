# Author:ZJF
from tkinter import *
window = Tk()
window.title("My window")
# window.geometry("1000x618")
l = Label(window, text="你好!this is tkinter",
          bg="yellow", font=("Arial", 20), width=30, height=2)
l.pack()
window.mainloop()
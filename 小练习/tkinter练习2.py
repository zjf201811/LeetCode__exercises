# Author:ZJF
from tkinter import *
window = Tk()
window.geometry("500x300")
var = StringVar()
l = Label(window, textvariable=var, bg="green", fg="white",
          font=("Arial",12), width=30, height=2)
l.pack()
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("gg")
b = Button(window, textvariable="hit me", font=("Arial", 12),
           width=10, height=1, command=hit_me)
b.pack()
window.mainloop()
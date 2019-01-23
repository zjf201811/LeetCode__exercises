#Author:ZJF
from tkinter import *


class ProcessButton:
    m = 1
    n = 1
    def __init__(self):
        window = Tk()
        btOK = Button(window, text="OK", fg="red", command=self.processOK)
        btCancel = Button(window, text="cancel", bg="yellow", command=self.processCancel)
        btOK.pack()
        btCancel.pack()
        window.mainloop()

    def processOK(self):

        print("OK button is clicked%s%s"%(self.m,self.n))
        self.m += 1

    def processCancel(self):

        print("Cancel button is clicked%s" % self.n)
        self.n += 1

ProcessButton()

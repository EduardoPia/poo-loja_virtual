from tkinter import *


window = Tk()

def click():
    ola = Label(window, text = "ola")
    ola.grid(row = 1, column= 0)
    oi = Label(window, text = "oi")
    oi.grid(row = 1, column= 0)
myButton = Button(window, text = "Hello there!", command=click)
myButton.grid(row = 0, column=0)

window.mainloop()

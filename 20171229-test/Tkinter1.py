from tkinter import *


def quit(parent):
    parent.destroy()


window = Tk()
button = Button(window, text='Good-bye', command=lambda: quit(window))
button.pack()

window.mainloop()

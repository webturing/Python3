from tkinter import *


def add(n):
    n.set(n.get() + 1)


window = Tk()
state = IntVar()
state.set(0)
button = Button(window, textvariable=state, command=lambda: add(state))
button.pack()

window.mainloop()

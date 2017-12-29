from tkinter import *


# controller
def click():
    counter.set(counter.get() + 1)


if __name__ == '__main__':
    # initialization
    window = Tk()

    # model
    counter = IntVar()
    counter.set(0)

    # views
    frame = Frame(window)
    frame.pack()

    button = Button(frame, text='click', command=click)
    button.pack()

    label = Label(frame, textvariable=counter)
    label.pack()

    window.mainloop()

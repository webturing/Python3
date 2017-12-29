from tkinter import *


def convert(fahrenheit, celsius):
    celsius.set((fahrenheit.get() - 32) * 5 / 9)


def quit(root):
    root.destroy()


window = Tk()
frame = Frame(window)
frame.pack()
label = Label(frame, text="Please enter the temperature...")
label.pack()
fahrenheit = DoubleVar()
fahrenheit.set(0.0)
entry = Entry(frame, textvariable=fahrenheit)
entry.pack()

celsius = DoubleVar()
label = Label(frame, textvariable=celsius)
button = Button(frame, text='Convert', command=lambda: convert(fahrenheit, celsius))

label.pack()
button.pack()
exit = Button(frame, text='Quit', command=lambda: quit(window))
exit.pack()
window.mainloop()

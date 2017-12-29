from tkinter import *


def count(text):
    data = text.get('0.0', END)
    a, t, c, g = 0, 0, 0, 0
    for char in data:
        if char == 'A':
            a += 1
        if char == 'T':
            t += 1
        if char == 'G':
            g += 1
        if char == 'C':
            c += 1
    counter.set('A:%d T:%d C:%d G:%d' % (a, t, c, g))


window = Tk()
frame = Frame(window)
frame.pack()
text = Text(frame, height=3, width=10)
text.pack()
button = Button(frame, text='Count', command=lambda: count(text))
button.pack()
counter = StringVar()
label = Label(frame, textvariable=counter)
label.pack()

window.mainloop()

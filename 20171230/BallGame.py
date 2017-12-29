# coding=utf-8
'''
Python GUI 之键盘控制事件（移动小球）
'''
from tkinter import *


class MovingBall:
    def __init__(self):
        window = Tk()
        window.title('移动小球')
        self.canvas = Canvas(window, width=200, height=100, bg='white')
        self.x, self.y, self.r = 100, 50, 10
        self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, tags='oval')  # 绘图
        self.canvas.pack()
        self.canvas.bind('<Key>', self.processKey)  # 画布监听键盘事件
        self.canvas.focus_set()  # 返回画布焦点
        window.mainloop()

    def processKey(self, event):
        if event.keysym == 'Up':  # 对应键盘Up
            self.up(event)
        if event.keysym == 'Down':
            self.down(event)
        if event.keysym == 'Left':
            self.left(event)
        if event.keysym == 'Right':
            self.right(event)

    def down(self, event):
        self.canvas.delete('oval')  # 删除原来的圆 GUI中 tags很巧妙灵活 图元绘制在画布上还可以管理~
        if self.y < 100:
            self.y += 10
        else:
            self.y = 0
        self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, tags='oval')

    def up(self, event):
        self.canvas.delete('oval')
        if self.y > 0:
            self.y -= 10
        else:
            self.y = 100
        self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, tags='oval')

    def right(self, event):
        self.canvas.delete('oval')
        if self.x < 200:
            self.x += 10
        else:
            self.x = 0
        self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, tags='oval')

    def left(self, event):
        self.canvas.delete('oval')
        if self.x > 0:
            self.x -= 10
        else:
            self.x = 200
        self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, tags='oval')


MovingBall()  # App Entry

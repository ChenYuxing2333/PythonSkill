#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 23:54
# @Author  : Jason Chan
# @Site    : 
# @File    : 13_图形界面.py
# @Software: PyCharm

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput =Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message','Hello,%s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()
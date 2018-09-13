# -*- coding:utf-8 -*-
from tkinter import *
import easygui as g
import tkinter.messagebox
from eric6.ThirdParty.Pygments.pygments.lexers._vim_builtins import command
class mainwindow:
    def __init__(self):
        self.frame = Tk()
        
        self.textroom = Text(self.frame,height = "30",width = 30)
        self.textlook = Text(self.frame,height = "30",width = 30)
        
        self.botton1 = Button(self.frame,text = "导入文件",width = 20,command = self.buttonListener1)
        self.botton2 = Button(self.frame,text = "提取关键字",width = 20,command = self.buttonListener2)
        self.botton3 = Button(self.frame,text = "情感分析",width = 20,command = self.buttonListener3)
        self.botton4 = Button(self.frame,text = "清空内容",width = 20,command = self.buttonListener4)
        
        self.lable1 = Label(self.frame,text = "输出区")
        self.lable2 = Label(self.frame,text = "输入区")
        self.lable3 = Label(self.frame,text = "")
        self.lable4 = Label(self.frame,text = "")

        
        self.lable1.grid(row = 0,column = 0)
        self.lable2.grid(row = 0,column = 1)
        self.textlook.grid(row = 1,column = 0)
        self.textroom.grid(row = 1,column = 1)
        self.lable3.grid(row = 2,column = 0)
        self.lable4.grid(row = 2,column = 1)
        self.botton1.grid(row = 3,column = 0)
        self.botton2.grid(row = 3,column = 1)
        self.botton3.grid(row = 4,column = 0)
        self.botton4.grid(row = 4,column = 1)
        self.frame.mainloop()
        
        
    def buttonListener1(self):
        str1=g.fileopenbox('选择文件','提示','C:',filetypes = "[*.txt]")
        print(str1)
        kkkk = open(str1).read()
        self.textroom.insert(END,kkkk)
    def buttonListener2(self):
        ttt = g.integerbox(msg = '输入你想要的关键词数目',title = '关键词提取',default = 0,lowerbound = 1, upperbound=100,root=None)
        kkk = self.textroom.get(1.0, END)
        print(kkk)
    def buttonListener3(self):
        kkk = self.textroom.get(1.0, END)
        print(kkk)
    def buttonListener4(self):
        self.textroom.delete(0.0, END)
                    
frame = mainwindow()        
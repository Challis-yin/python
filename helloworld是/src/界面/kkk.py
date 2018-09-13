# -*- coding:utf-8 -*-
import sys
import easygui as g
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from eric6.E5Gui.E5Action import addActions
from PyQt5.Qt import QVBoxLayout


class Example(QMainWindow):
    
    
    def add(self):
        str1=g.fileopenbox('选择文件','提示','C:',filetypes = "[*.txt]")
        print(str1)
        kkkk = open(str1).read()
        self.textEdit.setText(kkkk)
        
    def catch(self):
        ttt = g.integerbox(msg = '输入你想要的关键词数目',title = '关键词提取',default = 0,lowerbound = 1, upperbound=100,root=None)
        kkk = self.textEdit.toPlainText()
        print(kkk)
        
    def found(self):
        kkk = self.textEdit.toPlainText()
        print(kkk)
       
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):              

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
               

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        addAction  = QAction(QIcon('hello.png'), 'Add', self)
        addAction.setShortcut('Ctrl+N')
        addAction.setStatusTip('add files')
        addAction.triggered.connect(self.add)
        catchAction = QAction(QIcon('catch.png'), 'Catch', self)
        catchAction.setShortcut('Ctrl+J')
        catchAction.setStatusTip('Catch keywords')
        catchAction.triggered.connect(self.catch)
        foundAction = QAction(QIcon('found.png'), 'Get', self)
        foundAction.setShortcut('Ctrl+Y')
        foundAction.setStatusTip('Get emotion')
        foundAction.triggered.connect(self.found)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        catchmune = menubar.addMenu('&Catch')
        catchmune.addAction(catchAction)
        fileMenu.addAction(addAction)
        fileMenu.addAction(exitAction)
        catchmune.addAction(foundAction)
        
        toolbar = self.addToolBar('Add')
        toolbar.addAction(addAction)
        toolbar = self.addToolBar('Catch')
        toolbar.addAction(catchAction)
        toolbar = self.addToolBar('Found')
        toolbar.addAction(foundAction)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
       

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')   
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
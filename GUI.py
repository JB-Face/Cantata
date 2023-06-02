'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 20:03:27
LastEditors: JBFace
LastEditTime: 2023-06-02 14:44:57
'''

from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget,QProgressBar,QTabWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Cantata!")

        self.main_layout = QVBoxLayout() 

        self.set_tab()

        self.status_bar()
        self.main_widget = QLabel()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)
    

    def set_tab(self):
        self.tab_layout = QTabWidget()
        self.main_layout.addWidget(self.tab_layout)
        pass

    def main_gui(self):
        self._main_gui = QLabel(text = 'dddddddd')
        return self._main_gui
        pass

    def status_bar(self):

        self._status_bar_text = QLabel(text='Cantata 0.1. have a nice day ')
        self.progress_bar = QProgressBar()

        self.statusBar().addWidget(self._status_bar_text,stretch=9)
        self.statusBar().addWidget(self.progress_bar,stretch=1)


    def set_status_text(self,text):
        self._status_bar_text.setText(text)
        return 0

class GUI():

    def __init__(self) -> None:
        pass
    
    @classmethod
    def main_widgt_layout(cls):
        widget =  QLabel()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        return widget
    
    @classmethod
    def tab_addtab(cls,layout,text,tab = False):
        
        if tab:
             tab_label = QTabWidget()
        else:
            tab_label = QLabel()
        layout.addTab(tab_label,text)
        return tab_label
    
    @classmethod
    def text(cls,text):
        return QLabel(text = text)





        
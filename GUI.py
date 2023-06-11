'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 20:03:27
LastEditors: JBFace
LastEditTime: 2023-06-11 22:36:12
'''

from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout,QFileDialog, QWidget,QProgressBar,QTabWidget,QMessageBox,)
from PySide6.QtCore import QThread,QObject, Signal, Slot
class MainWindow(QMainWindow):

    progress_var = Signal(int)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Cantata!")

        self.main_layout = QVBoxLayout() 

        self.set_tab()

        self.status_bar()
        self.main_widget = QLabel()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)

        self.progress_var.connect(self.update_progress_bar)
    

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
        self.progress_bar.setMaximum(100)
        self.progress_bar.setMinimum(0)

        self.statusBar().addWidget(self._status_bar_text,stretch=9)
        self.statusBar().addWidget(self.progress_bar,stretch=1)


    def set_status_text(self,text,color = 'black'):
        self._status_bar_text.setText(text)
        self._status_bar_text.setStyleSheet("QLabel {color : "+ color+"; }");
        return 0
    
    @Slot(int)
    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def enable_gui(self,bool):
        self.setEnabled(bool)


class GUI():

    def __init__(self) -> None:
        pass
    
    @classmethod
    def main_widgt_layout(cls):
        layout = QVBoxLayout()
        return layout
    
    @classmethod
    def tab_addtab(cls,layout,text,tab = False):
        
        if tab:
             tab_label = QTabWidget()
        else:
            tab_label = QLabel()
        layout.addTab(tab_label,text)
        return tab_label
    
    @classmethod
    def text(cls,text,layout):
        label = QLabel(text = text)
        return layout.addWidget(label)
    
    @classmethod
    def run_button(cls,text,layout,fun):
        button = QPushButton(text)
        layout.addWidget(button)
        button.clicked.connect(fun)
        return button
    

    @classmethod
    def file_select(cls,text,layout):
        select_layout = QHBoxLayout()

        select_text = QLabel(text = text)
        select_target = QLabel(text = '未选择文件')
        select_button = QPushButton(text = '文件选择')

        def open_file():
            path_var = QFileDialog.getExistingDirectory(None,"C:\\Users\\user\\Desktop")
            select_target.setText(str(path_var))

        select_button.clicked.connect(open_file)

        select_layout.addWidget(select_text,stretch=2)
        select_layout.addWidget(select_target,stretch=6)
        select_layout.addWidget(select_button,stretch=2)

        layout.addLayout(select_layout)

        return select_target

    @classmethod
    def string_input(cls,text,layout):
        pass

    @classmethod
    def check_box(cls,text,layout):
        pass







        
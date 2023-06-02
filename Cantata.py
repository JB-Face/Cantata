'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 17:42:01
LastEditors: JBFace
LastEditTime: 2023-06-02 18:22:15
'''
import os
import rich
import sys
from rich.console import Console
from rich.traceback import install
from PySide6.QtWidgets import QApplication

from GUI import MainWindow,GUI
from ini import ini
    
install()
console = Console(tab_size = 16)

global log_gui
log_gui = None

def debug(str,type = '!',):
    if ini.DEBUG:
        console.log(str)
        global log_gui
        if log_gui:
            log_gui.set_status_text(str)
        pass
    else:
        pass


class Cantata():
    def __init__(self) -> None:
        debug('hello!!! Cantata')
        self.tool_class = {}
        self.tab_list_fun = []
        self.app = QApplication(sys.argv)
        pass

    def addTool(self,tool):
        tool_ins = tool()
        if tool.type not in self.tool_class:
            self.tool_class[tool_ins.type] = {}
        self.tool_class[tool_ins.type][tool_ins.name] = tool_ins


    def init_layout(self):
        for i in self.tool_class:
            type_layout = GUI.tab_addtab(self.main_layout,str(i),True)
            for ins in self.tool_class[i]:
                ins_layout = GUI.tab_addtab(type_layout,str(ins))
                ins_layout.setLayout(self.tool_class[i][ins].main_widget)






    def draw(self):        
        self.window = MainWindow()
        global log_gui
        log_gui = self.window
        self.main_layout = self.window.tab_layout

        self.init_layout()

        self.window.resize(400, 400)
        self.window.show()
        debug('buging')
        sys.exit(self.app.exec())


class Tool():
    '''
    msg: 初始化 一个 工具，请加入 ctx中
    param {*}
    return {*}
    LastEditors: JBFace
    '''    
    type: str = 'None'
    name :str =  'None'
    info : str = "None"

    def __init__(self) -> None:
        self.main_widget = GUI.main_widgt_layout()
        self.draw()
        pass

    def draw(self):
        pass

    def execute(self):
        # todo: 实现多线程
        pass

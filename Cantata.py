'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 17:42:01
LastEditors: JBFace
LastEditTime: 2023-06-12 18:30:11
'''
import os
import rich
import sys
from rich.console import Console
from rich.traceback import install
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread,QObject, Signal, Slot

from GUI import MainWindow,GUI
from ini import ini
    
install()
console = Console(tab_size = 16)

global log_gui
log_gui = None

def debug(log,type = '!',):
    if ini.DEBUG:
        console.log(log)
        global log_gui
        if log_gui:
            log_gui.set_status_text(str(log))
        pass
    else:
        pass


class Cantata():
    def __init__(self) -> None:
        debug('hello!!! Cantata')
        self.tool_class = {}
        self.tab_list_fun = []
        self.app = QApplication(sys.argv)

        with open("style.qss", "r") as f:
            _style = f.read()
            self.app.setStyleSheet(_style)

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
                ins_layout.setLayout(self.tool_class[i][ins].parent_layout)






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


class Tool(QThread):
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
        super().__init__()
        self.main_widget = GUI.main_widgt_layout()
        self.parent_layout = GUI.main_widgt_layout()
        self.parent_layout.addLayout(self.main_widget,stretch=8)
        self.infogui = GUI.info(text = self.info,layout=self.parent_layout,stretch=2)

        self.draw()

    def draw(self):
        pass

    def execute(self):
        pass

    # 多线程
    def run(self):
        self.gui_enable()
        self.execute()#执行用户内容
        self.stop()


    def bar_log(self,str,color = 'black'):
        global log_gui
        if log_gui:
            log_gui.set_status_text(str,color)


    def bar_progress(self,int):
        global log_gui
        if log_gui:
            # 需要一个信号进行绑定
            log_gui.progress_var.emit(int)


    def stop(self):
        global log_gui
        if log_gui:
            # 需要一个信号进行绑定
            self.bar_log('完成',color = 'green')
            self.bar_progress(int = 0)
            log_gui.enable_gui(True)

    def gui_enable(self):
        global log_gui
        if log_gui:
            log_gui.enable_gui(False)



    

            
    




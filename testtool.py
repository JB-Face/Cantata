'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 22:26:16
LastEditors: JBFace
LastEditTime: 2023-06-11 23:05:53
'''
from Cantata import Tool,debug
from GUI import GUI
from PySide6.QtCore import QThread, Signal, Qt
class test_sleep(Tool):

    type= '文件工具'
    name ="关键字筛选"
    info = "根据关键词给文件分类存放，将在指定路径建立对应文件夹来存放"

    def draw(self):

        GUI.text('is test',self.main_widget)
        GUI.text('is test2',self.main_widget)
        GUI.text('is test3',self.main_widget)
        GUI.text('is test4',self.main_widget)

        GUI.run_button('run',self.main_widget,self.execute)
        
        # self.main_widget.addWidget() 
    def execute(self):
        pass
class test_debugp(Tool):

    type= '测试工具'
    name ="关键字筛选2"
    info = "根据关键词给文件分类存放，将在指定路径建立对应文件夹来存放"

    def draw(self):
        pass

import time
class test_nuilt_thread(Tool):

    type= '测试工具'
    name ="多线程测试"
    info = "测试多线程的功能是否正常"

    def draw(self):
        GUI.run_button('run',self.main_widget,self.start)

    def execute(self):
        for i in range(100):
            self.bar_log(str(i))
            time.sleep(0.05)
            self.bar_progress(int = i)



       

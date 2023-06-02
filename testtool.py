'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 22:26:16
LastEditors: JBFace
LastEditTime: 2023-06-02 17:44:03
'''
from Cantata import Tool,debug
from GUI import GUI

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
        debug('test_sleep,execute debug')

class test_debugp(Tool):

    type= '测试工具'
    name ="关键字筛选2"
    info = "根据关键词给文件分类存放，将在指定路径建立对应文件夹来存放"

    def draw(self):
        pass
'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-02 17:48:22
LastEditors: JBFace
LastEditTime: 2023-06-12 18:18:06
'''


from Cantata import Tool,debug
from GUI import GUI

import os
import shutil
try:
    from PIL import Image
except  ImportError:
    import pip
    pip.main(["install", "--user", "pillow"])

from Cantata import debug
import time

class textureconver(Tool):
    type ='贴图'
    name ='贴图缩放'
    info ='相对或者绝对缩放贴图分辨率'

    def __init__(self) -> None:
        super().__init__()

        
        

    def draw(self):
        self.file_path = None
        self.file_path = GUI.file_select('选择文件夹',self.main_widget)
        self.check_box = GUI.check_box('相对缩放',self.main_widget)
        self.input = GUI.string_input('缩放大小/比例',self.main_widget)

        self.suffix = GUI.string_input('后缀',self.main_widget)
        GUI.run_button('run',self.main_widget,self.start)
        
        
        # self.main_widget.addWidget() 
    def execute(self):
        path = self.file_path()

        suffix= self.suffix()
        if suffix == '后缀':
            suffix = None 

        self._convertTextureSiez(inpath=path,
                                 size = self.input(),
                                 suffix= suffix,
                                 relatively = self.check_box()
                                 )


        #_convertTextureSiez(inpath=path,size=100,suffix='none',False)

        
    def _convertTextureSiez(self,inpath,size,suffix,relatively = False):
        """修改图像分辨率

        Args:
            inpath (_type_): 包含所有图像路径
            size (_type_): 分辨率大小
            suffix (_type_): 后缀
        """

                #         pass
        _imagelist = ['png','tga','jpg','jpeg','bmp']
        
        def _get_outfile(infile, outfile):    
            if outfile:        
                return outfile        
            dir, suffix = os.path.splitext(infile)
        
        def _resize_image(infile, outfile, x_s=128,relatively = False):    

            im = Image.open(infile)       
            x, y = im.size

            if relatively:
                x_s = float(x_s)
                y_s = int(y*x_s)
                x_s = int(x*x_s)
            else:
                x_s = int(x_s)
                y_s = int(y * x_s / x)   
            
            if y_s<=1:
                return

            out = im.resize((x_s, y_s), Image.ANTIALIAS)       
            outfile = _get_outfile(infile, outfile)       
            out.save(outfile)

        file_list = []
        for root, dirs, files in os.walk(inpath):
            for file in files:
                if file.split('.')[-1] in _imagelist:
                        infile = os.path.join(root,file)
                        out = file.replace('.',str(suffix) + '.')
                        outfile = os.path.join(root,out)
                        d = {
                            'infile' : infile,
                            'outfile': outfile,
                            'size': size,
                            'relatively' : relatively,
                            'name' : file
                        }

                       
                        file_list.append(d)

        maxpro = len(file_list)

        if len(file_list) > 0:
            pro = 100.0/maxpro
            pro_num = 0
            for i in file_list:
                _resize_image(i['infile'],i['outfile'],i['size'],i['relatively'])
                pro_num = pro_num +1
                self.bar_progress(int(pro * pro_num))
                self.bar_log(str(i['name']))
        else:
            self.bar_log('没有贴图处理',color='red')

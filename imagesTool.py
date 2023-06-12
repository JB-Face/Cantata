'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-02 17:48:22
LastEditors: JBFace
LastEditTime: 2023-06-11 23:52:12
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




class textureconver(Tool):
    type ='贴图'
    name ='贴图库转换'
    info ='将Blender贴图库转换为UE格式'

    def __init__(self) -> None:
        super().__init__()

        
        

    def draw(self):
        self.file_path = None
        self.file_path = GUI.file_select('select',self.main_widget)
        self.check_box = GUI.check_box('is check',self.main_widget)
        self.input = GUI.string_input('input',self.main_widget)
        GUI.run_button('run',self.main_widget,self.execute)
        
        
        # self.main_widget.addWidget() 
    def execute(self):
        path = self.file_path()
        debug(path)
        debug(self.check_box())
        debug(self.input())

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

        for root, dirs, files in os.walk(inpath):
            for file in files:
                if file.split('.')[-1] in _imagelist:
                        infile = os.path.join(root,file)
                        out = file.replace('.',str(suffix) + '.')
                        outfile = os.path.join(root,out)
                        _resize_image(infile,outfile,size,relatively)

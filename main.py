'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 17:54:01
LastEditors: JBFace
LastEditTime: 2023-06-12 22:29:09
'''
try:
    import colorama
    from rich.console import Console
    from rich.traceback import install
except  ImportError:
    import pip
    pip.main(["install", "--user", 
    "colorama",
    "rich",    
    ])
    from rich.console import Console
    from rich.traceback import install
    

from Cantata import Cantata
from ini import ini

toolclass = []
debug_class = []
if ini.DEBUG:
    from testtool import test_sleep,test_debugp,test_nuilt_thread,test_gui
    debug_class  =  [
                    test_sleep,
                    test_debugp,
                    test_nuilt_thread,
                    test_gui
                    ]
from imagesTool import textureconver

toolclass = [
textureconver,
]

toolclass = toolclass + debug_class

def main():
    global ctx
    ctx = Cantata()
    for i in toolclass:
        ctx.addTool(i)
    ctx.draw()    

if __name__ == "__main__":
    main()
'''
Descripttion: 
version: 
Author: JBFace
Date: 2023-06-01 17:54:01
LastEditors: JBFace
LastEditTime: 2023-06-02 18:21:30
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

from testtool import test_sleep,test_debugp
from imagesTool import textureconver

toolclass = [
test_sleep,
test_debugp,
textureconver
]

def main():
    global ctx
    ctx = Cantata()
    for i in toolclass:
        ctx.addTool(i)
    ctx.draw()    

if __name__ == "__main__":
    main()
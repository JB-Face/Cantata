pyinstaller --icon=Cantata.ico -F --noconsole main.py

del /s /Q Cantata\
rd Cantata
md Cantata
copy dist\main.exe Cantata\main.exe
copy style.qss Cantata\style.qss
ren Cantata\main.exe Cantata.exe
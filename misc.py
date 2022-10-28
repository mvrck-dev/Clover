import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QFontDatabase

def getfont():

    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '.'))
    ffl = os.path.join(ROOT_DIR, 'rsrc', 'ITCAvantGardeStd.ttf')
    id = QFontDatabase.addApplicationFont(ffl)
    # if id == -1:
    #     print("font not found", id)
    # else:
    #     print("font found", id)
    
    families = QFontDatabase.applicationFontFamilies(id)
    ITC_avant_garde = families[0]
    print(ITC_avant_garde)
    return ITC_avant_garde

getfont()

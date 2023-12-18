# -*- coding: utf-8 -*-
'''
    NextCrypt
    This application is developed using Qt and Python, providing a user-friendly interface for encrypting and decrypting messages using various algorithms such as Caesar and Vigenère.

    Author: Emre Demircan
    Github: emrecpp
    Date: 2023/12/13

'''

import sys, os
sys.path.append(f"Ui{os.sep}img") # otherwise it will cause error because "import images_rc" can't found in Ui file.
import imports
from imports import *
from qfluentwidgets import *
from qframelesswindow import *


from Ui.ui_DialogMain import Ui_DialogMain

class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
    def init(self):
        self.setTitleBar(StandardTitleBar(self))
        imports.main = self
        imports.ui = Ui_DialogMain()
        ui = imports.ui
        ui.setupUi(self)


        from GUIBind import GUIBind
        self.guibind = GUIBind()
        self.guibind.init(window=self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.init()
    window.show()
    sys.exit(app.exec())
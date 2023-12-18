import sys, os

from loguru import logger

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


from Ui.ui_DialogMain import Ui_DialogMain
global ui
ui:Ui_DialogMain = None
global main
main = None # Window of MainGUI



import sys

from PySide6 import QtWidgets
from homeWindow import homeWindow
from auxiliary import create_sets
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



app = QtWidgets.QApplication(sys.argv)
#create_sets('hand_gestures')
window = homeWindow()
window.show()

app.exec()
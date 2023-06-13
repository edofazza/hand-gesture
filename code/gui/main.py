import sys

from PySide6 import QtWidgets
from homeWindow import homeWindow

app = QtWidgets.QApplication(sys.argv)

window = homeWindow()
window.show()

app.exec()
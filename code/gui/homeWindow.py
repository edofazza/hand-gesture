from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_homeWindow import Ui_HomeWindow
from perfWindow import perfWindow
from trainingWindow import trainingWindow
from liveTestWindow import liveTestWindow
from ui_trainingWindow import Ui_TrainingWindow


class homeWindow(QWidget, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.trainButton.clicked.connect(self.training)
        self.perfButton.clicked.connect(self.perfReading)
        self.exitButton.clicked.connect(self.exit)

    def training(self, home_w):
        self.window = trainingWindow()
        self.window.show()
        self.hide()

    def perfReading(self):
        self.window = perfWindow()
        self.window.show()
        self.hide()
    
    def exit(self):
        self.close()
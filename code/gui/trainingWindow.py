from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFileDialog
from ui_trainingWindow import Ui_TrainingWindow
from trainingScratchWindow import trainingScratchWindow

class trainingWindow(QWidget, Ui_TrainingWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.preTrainedNetworkButton.clicked.connect(self.pretrained)
        self.fromScratchButton.clicked.connect(self.scratch)


    def pretrained(self):
        self.window = trainingScratchWindow()
        self.window.show()
        self.hide()

    def scratch(self):
        self.window = trainingScratchWindow()
        self.window.show()
        self.hide()

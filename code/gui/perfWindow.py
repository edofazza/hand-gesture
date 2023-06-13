from PySide6.QtCore import Qt
from ui_perfWindow import Ui_perfWindow

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from models import get_model_layers
from configuration import create_configuration_file
from train_model import test

class perfWindow(QWidget, Ui_perfWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.loadTrainedNetworkButton.clicked.connect(self.loadTrainedNetwork)
        self.plotLossButton.clicked.connect(self.plotLoss)
        self.plotAccuracyButton.clicked.connect(self.plotAccuracy)
        self.accuracyF1Button.clicked.connect(self.accuracyF1)
        self.plotConfusionMatrixButton.clicked.connect(self.plotConfusionMatrix)
        self.cancelButton.clicked.connect(self.cancel)

        gui_test_loader = any
        gui_model = any
        gui_criterion = any
        gui_device = any

        gui_test_loss = any
        gui_test_acc = any
        gui_test_f1 = any
        gui_conf_matrix = any

    def loadTrainedNetwork(self):
        #open the file dialog
        [gui_test_loader, gui_model, gui_criterion, gui_device] = QFileDialog.getOpenFileName(
            self,"Open File","C:/Users/Workstation-1/OneDrive - Scuola Superiore Sant'Anna/DL project/Qt GUI"
            )
        
        #update the label with file directory
        if [gui_test_loader, gui_model, gui_criterion, gui_device]:
            self.trainedNetworkLabel.setText("Filed loaded")

    def plotLoss(self):
        self.close()
    
    def plotAccuracy(self):
        self.close()
    
    def accuracyF1(self):
        self.close()

    def plotConfusionMatrix(self):
        self.close()

    def cancel(self):
        self.close()
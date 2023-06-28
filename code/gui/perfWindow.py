from PySide6.QtCore import Qt
from ui_perfWindow import Ui_perfWindow

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from code.training.models import get_model_layers
from code.utils.configuration import create_configuration_file, load_configuration_file
from code.training.train_model import train_model, test_model
from code.utils.performance import *
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from ui_plotDialog import Ui_plotDialog

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


    def loadTrainedNetwork(self):
        #open the file dialog
        dataFile = QFileDialog.getExistingDirectory(self,"Open File","C:/Users/Workstation-1/OneDrive - Scuola Superiore Sant'Anna/DL project/Qt GUI/models",)
        
        #update the label with file directory
        if dataFile:
            self.trainedNetworkLabel.setText(dataFile)
            prepare_data_for_gui()


    def openPlot(self,path):
        self.window = QDialog()
        self.ui = Ui_plotDialog()
        self.ui.setupUi(self.window)
        plot = QPixmap(path)
        self.ui.plotLabel.setScaledContents(True)
        self.ui.plotLabel.setPixmap(plot)
        self.window.show()
        
    def plotLoss(self):
        path = self.trainedNetworkLabel.text()
        path = path + '/performance/loss_plot.png'
        self.openPlot(path)
    
    def plotAccuracy(self):
        path = self.trainedNetworkLabel.text()
        path = path + '/performance/accuracy_plot.png'
        self.openPlot(path)
    
    def accuracyF1(self):
        path = self.trainedNetworkLabel.text()
        path = path + '/performance/F1_score_plot.png.png'
        self.openPlot(path)

    def plotConfusionMatrix(self):
        path = self.trainedNetworkLabel.text()
        path = path + '/performance/confusion_matrix.png'
        self.openPlot(path)

    def cancel(self):
        self.close()
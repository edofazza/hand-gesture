from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFileDialog
from ui_trainingScratchWindow import Ui_TrainingScratchWindow 
from PySide6.QtMultimedia import (QAudioInput, QCamera, QCameraDevice,
                                  QImageCapture, QMediaCaptureSession,
                                  QMediaDevices, QMediaMetaData,
                                  QMediaRecorder)
from PySide6.QtMultimediaWidgets import QVideoWidget

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from models import get_model_layers
from configuration import create_configuration_file


class trainingScratchWindow(QWidget, Ui_TrainingScratchWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
        self.loadDataButton.clicked.connect(self.loadData)
        self.cancelButton.clicked.connect(self.quit)
        self.confirmButton.clicked.connect(self.confirm)

        self.networkTypeComboBox.addItems(["resnet18", "resnet50", "resnet101", "densenet121",
                                            "vgg16", "inception_v3", "efficientnet_b0"])
        self.ftLayerComboBox.addItems(get_model_layers(self.networkTypeComboBox.itemText(0)))
        self.networkTypeComboBox.currentTextChanged.connect(self.layersList)
        
        self.ftYesRadioButton.toggled.connect(self.fineTuning)
        self.ftNoRadioButton.toggled.connect(self.fineTuning)

        self.hFlitYesRadioButton.toggled.connect(self.horizontalFlip)
        self.hFlitNoRadioButton.toggled.connect(self.horizontalFlip)

        self.linContrastYesRadioButton.toggled.connect(self.linearContrast)
        self.linContrastNoRadioButton.toggled.connect(self.linearContrast)

        self.gBlurYesRadioButton.toggled.connect(self.gaussianBlur)
        self.gBlurNoRadioButton.toggled.connect(self.gaussianBlur)

        self.affineTransYesRadioButton.toggled.connect(self.affineTranfo)
        self.affineTransNoRadioButton.toggled.connect(self.affineTranfo)

        self.jitterYesRadioButton.toggled.connect(self.jitter)
        self.jitterNoRadioButton.toggled.connect(self.jitter)

        self.optSchedulerYesRadioButton.toggled.connect(self.optimizerSchedule)
        self.optSchedulerNoRadioButton.toggled.connect(self.optimizerSchedule)

        
    def loadData(self):
        #open the file dialog
        dataFile = QFileDialog.getOpenFileName(self,"Open File","C:/Users/Workstation-1/OneDrive - Scuola Superiore Sant'Anna/DL project/Qt GUI")
        
        #update the label with file directory
        if dataFile:
            self.dataPathLabel.setText(dataFile[0])

    def fineTuning(self):
        if self.ftYesRadioButton.isChecked():
            self.ftLayerComboBox.setEnabled(True)
        else:
            self.ftLayerComboBox.setDisabled(True)

    def layersList(self):
        self.ftLayerComboBox.clear()
        model = self.networkTypeComboBox.currentText()
        layers = get_model_layers(model)
        self.ftLayerComboBox.addItems(layers)

    def horizontalFlip(self):
        if self.hFlitYesRadioButton.isChecked():
            self.hFlipLineEdit.setEnabled(True)
        else:
            self.hFlipLineEdit.setDisabled(True)

    def linearContrast(self):
        if self.linContrastYesRadioButton.isChecked():
            self.linContrastMinLineEdit.setEnabled(True)
            self.linContrastMaxLineEdit.setEnabled(True)
        else:
            self.linContrastYesRadioButton.setDisabled(True)
            self.linContrastMaxLineEdit.setDisabled(True)

    def gaussianBlur(self):
        if self.gBlurYesRadioButton.isChecked():
            self.gBlurSigMinLineEdit.setEnabled(True)
            self.gBlurSigMaxLineEdit.setEnabled(True)
            self.gBlurKernelLineEdit.setEnabled(True)
        else:
            self.gBlurSigMinLineEdit.setDisabled(True)
            self.gBlurSigMaxLineEdit.setDisabled(True)
            self.gBlurKernelLineEdit.setDisabled(True)

    def affineTranfo(self):
        if self.affineTransYesRadioButton.isChecked():
            self.affineTransProbaLineEdit.setEnabled(True)
            self.affineTransMinLineEdit.setEnabled(True)
            self.affineTransMaxLineEdit.setEnabled(True)
            self.affineTransAngleRotLineEdit.setEnabled(True)
        else:
            self.affineTransProbaLineEdit.setDisabled(True)
            self.affineTransMinLineEdit.setDisabled(True)
            self.affineTransMaxLineEdit.setDisabled(True)
            self.affineTransAngleRotLineEdit.setDisabled(True)

    def jitter(self):
        if self.jitterYesRadioButton.isChecked():
            self.jitterHueLineEdit.setEnabled(True)
            self.jitterMinLineEdit.setEnabled(True)
            self.jitterMaxLineEdit.setEnabled(True)
        else:
            self.jitterHueLineEdit.setDisabled(True)
            self.jitterMinLineEdit.setDisabled(True)
            self.jitterMaxLineEdit.setDisabled(True)

    def optimizerSchedule(self):
        if self.optSchedulerYesRadioButton.isChecked():
            self.schedGammaLineEdit.setEnabled(True)
            self.schedPatienceLineEdit.setEnabled(True)
            self.schedThresholdLineEdit.setEnabled(True)
        else:
            self.schedGammaLineEdit.setDisabled(True)
            self.schedPatienceLineEdit.setDisabled(True)
            self.schedThresholdLineEdit.setDisabled(True)


    def quit(self):
        self.close()

    def confirm(self):
        gui_model_name = self.networkTypeComboBox.currentText()
        gui_finetune_layer = self.ftLayerComboBox.currentText()
        
        # TRAINING PARAMETERS
        gui_batch_size = self.batchSizeLineEdit.text()
        gui_epochs = self.epochsLineEdit.text()
        gui_learning_rate = self.learningRateLineEdit.text()

        if self.optSchedulerYesRadioButton.isChecked():
            gui_optimizer_scheduler = True
        else:
            gui_optimizer_scheduler = False
        gui_scheduler_gamma = self.schedGammaLineEdit.text()
        gui_scheduler_patience = self.schedPatienceLineEdit.text()
        gui_scheduler_threshold = self.schedThresholdLineEdit.text()
        gui_convergence = self.convergenceLineEdit.text()

        # DATA AUGMENTATION PARAMETERS
        if self.hFlitYesRadioButton.isChecked():
            gui_fliplr = True
        else:
            gui_fliplr = False
        gui_fliplr_value = self.hFlipLineEdit.text()

        if self.gBlurYesRadioButton.isChecked():
            gui_gaussian_blur = True
        else:
            gui_gaussian_blur = False
        gui_gaussian_kernel = self.gBlurKernelLineEdit.text()
        gui_sigma_min = self.gBlurSigMinLineEdit.text()
        gui_sigma_max = self.gBlurSigMaxLineEdit.text()

        if self.affineTransYesRadioButton.isChecked():
            gui_affine = True
        else:
            gui_affine = False
        gui_affine_percent = self.affineTransProbaLineEdit.text()
        gui_affine_scale_min = self.affineTransMinLineEdit.text()
        gui_affine_scale_max = self.affineTransMaxLineEdit.text()

        if self.jitterYesRadioButton.isChecked():
            gui_jitter = True
        else:
            gui_jitter = False
        gui_jitter_min = self.jitterMinLineEdit.text()
        gui_jitter_max = self.jitterMaxLineEdit.text()
        gui_jitter_hue = self.jitterHueLineEdit.text()


        create_configuration_file(
        model_name = gui_model_name,
        pretrained_weights=False,
        finetune_layer='fc',
        pretrain_CIFAR=False,
        pretrained_model=False,     # get trained weights
        layers=[3, 3, 3],
        growth_rate=32,
        # TRAINING PARAMETERS
        batch_size = gui_batch_size,
        epochs = gui_epochs,
        dataset_path='hand_gestures',
        learning_rate = gui_learning_rate,
        optimizer_scheduler = gui_optimizer_scheduler,
        scheduler_gamma = gui_scheduler_gamma,
        scheduler_patience = gui_scheduler_patience,
        scheduler_threshold = gui_scheduler_threshold,
        convergence = gui_convergence,
        # DATA AUGMENTATION PARAMETERS
        fliplr = gui_fliplr,
        fliplr_value=gui_fliplr_value,
        gaussian_blur=gui_gaussian_blur,
        gaussian_kernel=gui_gaussian_kernel,
        sigma_min=gui_sigma_min,
        sigma_max=gui_sigma_max,
        affine=gui_affine,
        affine_percent=gui_affine_percent,
        affine_scale_min=gui_affine_scale_min,
        affine_scale_max=gui_affine_scale_max,
        jitter=gui_jitter,
        jitter_min=gui_jitter_min,
        jitter_max=gui_jitter_max,
        jitter_hue=gui_jitter_hue,
        # GENERAL
        seed=42,
)
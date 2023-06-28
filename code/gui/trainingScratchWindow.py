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
from code.training.models import get_model_layers
from code.utils.configuration import create_configuration_file, load_configuration_file
from code.training.train_model import test_model, train_model


class trainingScratchWindow(QWidget, Ui_TrainingScratchWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
        self.loadDataButton.clicked.connect(self.loadData)
        self.cancelButton.clicked.connect(self.quit)
        self.yamlFileButton.clicked.connect(self.createYamlFile)
        self.trainButton.clicked.connect(self.trainNetwork)

        self.networkTypeComboBox.addItems(["resnet18", "resnet50", "resnet101", "densenet121",
                                            "vgg16", "inception_v3", "efficientnet_b0"])
        self.ftLayerComboBox.addItems(get_model_layers(self.networkTypeComboBox.itemText(0)))
        self.networkTypeComboBox.currentTextChanged.connect(self.layersList)
        self.pretrainingComboBox.addItems(["ImageNet", "CIFAR", "My pretrained model"])

        self.customModelYesRadioButton.toggled.connect(self.customModel)
        self.customModelNoRadioButton.toggled.connect(self.customModel)

        self.ftYesRadioButton.toggled.connect(self.fineTuning)
        self.ftNoRadioButton.toggled.connect(self.fineTuning)

        self.pretrainingYesRadioButton.toggled.connect(self.pretraining)
        self.pretrainingNoRadioButton.toggled.connect(self.pretraining   )

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
        dataFile = QFileDialog.getExistingDirectory(self,"Open File","C:/Users/Workstation-1/OneDrive - Scuola Superiore Sant'Anna/DL project/Qt GUI")
        
        #update the label with file directory
        if dataFile:
            self.dataPathLabel.setText(dataFile[0])

    def customModel(self):
        if self.customModelYesRadioButton.isChecked():
            self.customLayersLineEdit.setEnabled(True)
            self.networkTypeComboBox.clear()
            self.networkTypeComboBox.addItems(["custom_resnet", "custom_densenet", "custom_senet"])
            self.ftNoRadioButton.setChecked(True)
            self.finetuningGroupBox.setDisabled(True)
        else:
            self.customLayersLineEdit.setDisabled(True)
            self.networkTypeComboBox.clear()
            self.networkTypeComboBox.addItems(["resnet18", "resnet50", "resnet101", "densenet121",
                                            "vgg16", "inception_v3", "efficientnet_b0"])
            self.finetuningGroupBox.setEnabled(True)

    def fineTuning(self):
        if self.ftYesRadioButton.isChecked():
            self.ftLayerComboBox.setEnabled(True)
        else:
            self.ftLayerComboBox.setDisabled(True)

    def pretraining(self):
        if self.pretrainingYesRadioButton.isChecked():
            self.pretrainingComboBox.setEnabled(True)
        else:
            self.pretrainingComboBox.setDisabled(True)

    def layersList(self):
        if not self.customModelYesRadioButton.isChecked():
            if not self.networkTypeComboBox.count() == 0:
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

    def createYamlFile(self):
        if self.customModelNoRadioButton.isChecked():
            if self.networkTypeComboBox.currentText().startswith('resnet'):
                name = 'resnet'
                n = len(name)
                number = self.networkTypeComboBox.currentText()[n:]
            if self.networkTypeComboBox.currentText().startswith('densenet'):
                name = 'densenet'
                n = len(name)
                number = self.networkTypeComboBox.currentText()[n:]
            if self.networkTypeComboBox.currentText().startswith('vgg'):
                name = 'vgg'
                n = len(name)
                number = self.networkTypeComboBox.currentText()[n:]
            if self.networkTypeComboBox.currentText().startswith('inception'):
                name = 'inception'
                number = self.networkTypeComboBox.currentText()[5:]
            if self.networkTypeComboBox.currentText().startswith('efficientnet'):
                name = 'efficientnet'
                number = self.networkTypeComboBox.currentText()[5:]

            if self.ftYesRadioButton.isChecked():
                gui_finetune_layer = self.ftLayerComboBox.currentText()
                if number.startswith('_'):
                    gui_model_name = name + '_' + gui_finetune_layer + number
                else:
                    gui_model_name = name + '-' + gui_finetune_layer + '-' + number
            else:
                gui_finetune_layer = 'scratch'
                if number.startswith('_'):
                    gui_model_name = name + '_scratch' + number
                else:
                    gui_model_name = name + '-scratch' + '-' + number

        else:
            gui_model_name = self.networkTypeComboBox.currentText()
            gui_finetune_layer = 'scratch'
        
        
        # TRAINING PARAMETERS
        gui_batch_size =  int(self.batchSizeLineEdit.text())
        gui_epochs = int(self.epochsLineEdit.text())
        gui_learning_rate = float(self.learningRateLineEdit.text())

        if self.optSchedulerYesRadioButton.isChecked():
            gui_optimizer_scheduler = True
        else:
            gui_optimizer_scheduler = False
        gui_scheduler_gamma = float(self.schedGammaLineEdit.text())
        gui_scheduler_patience = float(self.schedPatienceLineEdit.text())
        gui_scheduler_threshold = float(self.schedThresholdLineEdit.text())
        gui_convergence = int(self.convergenceLineEdit.text())

        # DATA AUGMENTATION PARAMETERS
        if self.hFlitYesRadioButton.isChecked():
            gui_fliplr = True
        else:
            gui_fliplr = False
        gui_fliplr_value = float(self.hFlipLineEdit.text())

        if self.gBlurYesRadioButton.isChecked():
            gui_gaussian_blur = True
        else:
            gui_gaussian_blur = False
        gui_gaussian_kernel = float(self.gBlurKernelLineEdit.text())
        gui_sigma_min = float(self.gBlurSigMinLineEdit.text())
        gui_sigma_max = float(self.gBlurSigMaxLineEdit.text())

        if self.affineTransYesRadioButton.isChecked():
            gui_affine = True
        else:
            gui_affine = False
        gui_affine_percent = float(self.affineTransProbaLineEdit.text())
        gui_affine_scale_min = float(self.affineTransMinLineEdit.text())
        gui_affine_scale_max = float(self.affineTransMaxLineEdit.text())

        if self.jitterYesRadioButton.isChecked():
            gui_jitter = True
        else:
            gui_jitter = False
        gui_jitter_min = float(self.jitterMinLineEdit.text())
        gui_jitter_max = float(self.jitterMaxLineEdit.text())
        gui_jitter_hue = float(self.jitterHueLineEdit.text())

        if self.pretrainingYesRadioButton.isChecked():
            if self.pretrainingComboBox.currentText() == "ImageNet":
                gui_pretrained_weights = True
                gui_pretrained_CIFAR = False
                gui_pretrained_model = False
            elif self.pretrainingComboBox.currentText() == "CIFAR":
                gui_pretrained_weights = False
                gui_pretrained_CIFAR = True
                gui_pretrained_model = False
            elif self.pretrainingComboBox.currentText() == "My pretrained model":
                gui_pretrained_weights = False
                gui_pretrained_CIFAR = False
                gui_pretrained_model = True
        else:
            gui_pretrained_weights = False
            gui_pretrained_CIFAR = False
            gui_pretrained_model = False

        gui_layers = self.customLayersLineEdit.text()

        if self.customModelYesRadioButton.isChecked():
            x = gui_layers[1]
            print(gui_layers)
            print(x)
            y = gui_layers[4]
            z = gui_layers[7]
            layer = '_' + x + '_' + y +'_' + z
            gui_model_name = gui_model_name + layer
            if self.pretrainingComboBox.currentText() == 'CIFAR':
                gui_model_name = gui_model_name + '_CIFAR'


        create_configuration_file(
        model_name = gui_model_name,
        pretrained_weights = gui_pretrained_weights,
        finetune_layer = gui_finetune_layer,
        pretrain_CIFAR = gui_pretrained_CIFAR,
        pretrained_model = gui_pretrained_model,     # get trained weights
        layers = gui_layers,
        growth_rate=32,
        # TRAINING PARAMETERS
        batch_size = gui_batch_size,
        epochs = gui_epochs,
        dataset_path= self.dataPathLabel.text(),
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
        


    def trainNetwork(self):
        cfg = load_configuration_file('config.yaml')
        cfg['pretrained_model'] = False
        train_model(cfg)
        test_model(cfg)

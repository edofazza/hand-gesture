from PySide6.QtCore import Qt
from ui_perfWindow import Ui_perfWindow

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from models import get_model_layers
from configuration import create_configuration_file, load_configuration_file
from train_model import train_model, test_model
from performance import *
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from ui_plotDialog import Ui_plotDialog


class perfWindow(QDialog, Ui_plotDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
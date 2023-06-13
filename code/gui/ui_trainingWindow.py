# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainingWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TrainingWindow(object):
    def setupUi(self, TrainingWindow):
        if not TrainingWindow.objectName():
            TrainingWindow.setObjectName(u"TrainingWindow")
        TrainingWindow.resize(436, 356)
        self.widget = QWidget(TrainingWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 40, 346, 251))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.preTrainedNetworkButton = QPushButton(self.widget)
        self.preTrainedNetworkButton.setObjectName(u"preTrainedNetworkButton")

        self.verticalLayout.addWidget(self.preTrainedNetworkButton)

        self.fromScratchButton = QPushButton(self.widget)
        self.fromScratchButton.setObjectName(u"fromScratchButton")

        self.verticalLayout.addWidget(self.fromScratchButton)


        self.retranslateUi(TrainingWindow)

        QMetaObject.connectSlotsByName(TrainingWindow)
    # setupUi

    def retranslateUi(self, TrainingWindow):
        TrainingWindow.setWindowTitle(QCoreApplication.translate("TrainingWindow", u"Network training", None))
        self.label.setText(QCoreApplication.translate("TrainingWindow", u"Do you want to use a pretrained network or to train from scratch?", None))
        self.preTrainedNetworkButton.setText(QCoreApplication.translate("TrainingWindow", u"Pretrained network", None))
        self.fromScratchButton.setText(QCoreApplication.translate("TrainingWindow", u"Scratch", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perfWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_perfWindow(object):
    def setupUi(self, perfWindow):
        if not perfWindow.objectName():
            perfWindow.setObjectName(u"perfWindow")
        perfWindow.resize(400, 398)
        self.verticalLayout = QVBoxLayout(perfWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loadTrainedNetworkButton = QPushButton(perfWindow)
        self.loadTrainedNetworkButton.setObjectName(u"loadTrainedNetworkButton")

        self.horizontalLayout.addWidget(self.loadTrainedNetworkButton)

        self.trainedNetworkLabel = QLabel(perfWindow)
        self.trainedNetworkLabel.setObjectName(u"trainedNetworkLabel")

        self.horizontalLayout.addWidget(self.trainedNetworkLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.plotLossButton = QPushButton(perfWindow)
        self.plotLossButton.setObjectName(u"plotLossButton")

        self.gridLayout.addWidget(self.plotLossButton, 0, 0, 1, 1)

        self.plotAccuracyButton = QPushButton(perfWindow)
        self.plotAccuracyButton.setObjectName(u"plotAccuracyButton")

        self.gridLayout.addWidget(self.plotAccuracyButton, 0, 1, 1, 1)

        self.accuracyF1Button = QPushButton(perfWindow)
        self.accuracyF1Button.setObjectName(u"accuracyF1Button")

        self.gridLayout.addWidget(self.accuracyF1Button, 1, 0, 1, 1)

        self.plotConfusionMatrixButton = QPushButton(perfWindow)
        self.plotConfusionMatrixButton.setObjectName(u"plotConfusionMatrixButton")

        self.gridLayout.addWidget(self.plotConfusionMatrixButton, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.cancelButton = QPushButton(perfWindow)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.retranslateUi(perfWindow)

        QMetaObject.connectSlotsByName(perfWindow)
    # setupUi

    def retranslateUi(self, perfWindow):
        perfWindow.setWindowTitle(QCoreApplication.translate("perfWindow", u"Network performance", None))
        self.loadTrainedNetworkButton.setText(QCoreApplication.translate("perfWindow", u"Load trained Network", None))
        self.trainedNetworkLabel.setText(QCoreApplication.translate("perfWindow", u"File :", None))
        self.plotLossButton.setText(QCoreApplication.translate("perfWindow", u"Plot Loss", None))
        self.plotAccuracyButton.setText(QCoreApplication.translate("perfWindow", u"Plot Accuracy", None))
        self.accuracyF1Button.setText(QCoreApplication.translate("perfWindow", u"Accuracy F1", None))
        self.plotConfusionMatrixButton.setText(QCoreApplication.translate("perfWindow", u"Plot Confusion Matrix", None))
        self.cancelButton.setText(QCoreApplication.translate("perfWindow", u"Cancel", None))
    # retranslateUi


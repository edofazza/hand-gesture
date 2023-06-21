# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(325, 386)
        self.horizontalLayout = QHBoxLayout(HomeWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.trainButton = QPushButton(HomeWindow)
        self.trainButton.setObjectName(u"trainButton")

        self.verticalLayout.addWidget(self.trainButton)

        self.perfButton = QPushButton(HomeWindow)
        self.perfButton.setObjectName(u"perfButton")

        self.verticalLayout.addWidget(self.perfButton)

        self.exitButton = QPushButton(HomeWindow)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout.addWidget(self.exitButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"Hand gesture recognition", None))
        self.trainButton.setText(QCoreApplication.translate("HomeWindow", u"Train Network", None))
        self.perfButton.setText(QCoreApplication.translate("HomeWindow", u"Network Performances", None))
        self.exitButton.setText(QCoreApplication.translate("HomeWindow", u"Exit", None))
    # retranslateUi


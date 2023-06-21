# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_plotDialog(object):
    def setupUi(self, plotDialog):
        if not plotDialog.objectName():
            plotDialog.setObjectName(u"plotDialog")
        plotDialog.resize(885, 791)
        self.verticalLayout = QVBoxLayout(plotDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotLabel = QLabel(plotDialog)
        self.plotLabel.setObjectName(u"plotLabel")
        self.plotLabel.setFrameShape(QFrame.Box)

        self.verticalLayout.addWidget(self.plotLabel)


        self.retranslateUi(plotDialog)

        QMetaObject.connectSlotsByName(plotDialog)
    # setupUi

    def retranslateUi(self, plotDialog):
        plotDialog.setWindowTitle(QCoreApplication.translate("plotDialog", u"Dialog", None))
        self.plotLabel.setText("")
    # retranslateUi


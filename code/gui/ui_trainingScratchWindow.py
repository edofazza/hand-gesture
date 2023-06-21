# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainingScratchWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TrainingScratchWindow(object):
    def setupUi(self, TrainingScratchWindow):
        if not TrainingScratchWindow.objectName():
            TrainingScratchWindow.setObjectName(u"TrainingScratchWindow")
        TrainingScratchWindow.resize(841, 816)
        self.dataLabel = QLabel(TrainingScratchWindow)
        self.dataLabel.setObjectName(u"dataLabel")
        self.dataLabel.setGeometry(QRect(20, 0, 201, 24))
        self.finetuningGroupBox = QGroupBox(TrainingScratchWindow)
        self.finetuningGroupBox.setObjectName(u"finetuningGroupBox")
        self.finetuningGroupBox.setGeometry(QRect(20, 130, 91, 80))
        self.finetuningGroupBox.setContextMenuPolicy(Qt.PreventContextMenu)
        self.finetuningGroupBox.setLayoutDirection(Qt.LeftToRight)
        self.finetuningGroupBox.setFlat(True)
        self.finetuningGroupBox.setCheckable(False)
        self.ftYesRadioButton = QRadioButton(self.finetuningGroupBox)
        self.ftYesRadioButton.setObjectName(u"ftYesRadioButton")
        self.ftYesRadioButton.setEnabled(True)
        self.ftYesRadioButton.setGeometry(QRect(20, 30, 89, 20))
        self.ftYesRadioButton.setLayoutDirection(Qt.LeftToRight)
        self.ftNoRadioButton = QRadioButton(self.finetuningGroupBox)
        self.ftNoRadioButton.setObjectName(u"ftNoRadioButton")
        self.ftNoRadioButton.setGeometry(QRect(20, 50, 89, 20))
        self.ftNoRadioButton.setChecked(True)
        self.DataAugmentationFrame = QFrame(TrainingScratchWindow)
        self.DataAugmentationFrame.setObjectName(u"DataAugmentationFrame")
        self.DataAugmentationFrame.setGeometry(QRect(20, 240, 401, 511))
        self.DataAugmentationFrame.setFrameShape(QFrame.Box)
        self.DataAugmentationFrame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.DataAugmentationFrame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(100, 110, 251, 51))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_17 = QLabel(self.layoutWidget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setTextFormat(Qt.AutoText)

        self.horizontalLayout_10.addWidget(self.label_17)

        self.horizontalSpacer_20 = QSpacerItem(48, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)

        self.linContrastMinLineEdit = QLineEdit(self.layoutWidget_3)
        self.linContrastMinLineEdit.setObjectName(u"linContrastMinLineEdit")
        self.linContrastMinLineEdit.setEnabled(False)
        self.linContrastMinLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.linContrastMinLineEdit)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.label_18 = QLabel(self.layoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.label_19 = QLabel(self.layoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_11.addWidget(self.label_19)

        self.horizontalSpacer_21 = QSpacerItem(47, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.linContrastMaxLineEdit = QLineEdit(self.layoutWidget_3)
        self.linContrastMaxLineEdit.setObjectName(u"linContrastMaxLineEdit")
        self.linContrastMaxLineEdit.setEnabled(False)
        self.linContrastMaxLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_11.addWidget(self.linContrastMaxLineEdit)

        self.horizontalSpacer_3 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_11.addWidget(self.label_20)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.layoutWidget_4 = QWidget(self.DataAugmentationFrame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(100, 310, 251, 98))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_21 = QLabel(self.layoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_12.addWidget(self.label_21)

        self.horizontalSpacer_27 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_27)

        self.affineTransProbaLineEdit = QLineEdit(self.layoutWidget_4)
        self.affineTransProbaLineEdit.setObjectName(u"affineTransProbaLineEdit")
        self.affineTransProbaLineEdit.setEnabled(False)
        self.affineTransProbaLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_12.addWidget(self.affineTransProbaLineEdit)

        self.horizontalSpacer_30 = QSpacerItem(33, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_30)

        self.label_22 = QLabel(self.layoutWidget_4)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_12.addWidget(self.label_22)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.label_25 = QLabel(self.layoutWidget_4)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_14.addWidget(self.label_25)

        self.horizontalSpacer_28 = QSpacerItem(49, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_28)

        self.affineTransMinLineEdit = QLineEdit(self.layoutWidget_4)
        self.affineTransMinLineEdit.setObjectName(u"affineTransMinLineEdit")
        self.affineTransMinLineEdit.setEnabled(False)
        self.affineTransMinLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_14.addWidget(self.affineTransMinLineEdit)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.label_26 = QLabel(self.layoutWidget_4)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_14.addWidget(self.label_26)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.label_23 = QLabel(self.layoutWidget_4)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_13.addWidget(self.label_23)

        self.horizontalSpacer_29 = QSpacerItem(47, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_29)

        self.affineTransMaxLineEdit = QLineEdit(self.layoutWidget_4)
        self.affineTransMaxLineEdit.setObjectName(u"affineTransMaxLineEdit")
        self.affineTransMaxLineEdit.setEnabled(False)
        self.affineTransMaxLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_13.addWidget(self.affineTransMaxLineEdit)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.label_24 = QLabel(self.layoutWidget_4)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_13.addWidget(self.label_24)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_26.setContentsMargins(-1, -1, 0, -1)
        self.label_50 = QLabel(self.layoutWidget_4)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_26.addWidget(self.label_50)

        self.affineTransAngleRotLineEdit = QLineEdit(self.layoutWidget_4)
        self.affineTransAngleRotLineEdit.setObjectName(u"affineTransAngleRotLineEdit")
        self.affineTransAngleRotLineEdit.setEnabled(False)
        self.affineTransAngleRotLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_26.addWidget(self.affineTransAngleRotLineEdit)

        self.horizontalSpacer_18 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_18)

        self.label_51 = QLabel(self.layoutWidget_4)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_26.addWidget(self.label_51)


        self.verticalLayout_5.addLayout(self.horizontalLayout_26)

        self.layoutWidget_6 = QWidget(self.DataAugmentationFrame)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(100, 430, 251, 74))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(7)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_24.setContentsMargins(-1, -1, 0, -1)
        self.label_46 = QLabel(self.layoutWidget_6)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_24.addWidget(self.label_46)

        self.horizontalSpacer_31 = QSpacerItem(48, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_31)

        self.jitterHueLineEdit = QLineEdit(self.layoutWidget_6)
        self.jitterHueLineEdit.setObjectName(u"jitterHueLineEdit")
        self.jitterHueLineEdit.setEnabled(False)
        self.jitterHueLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_24.addWidget(self.jitterHueLineEdit)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.label_47 = QLabel(self.layoutWidget_6)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_24.addWidget(self.label_47)


        self.verticalLayout_8.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.layoutWidget_6)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_15.addWidget(self.label_27)

        self.horizontalSpacer_32 = QSpacerItem(48, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_32)

        self.jitterMinLineEdit = QLineEdit(self.layoutWidget_6)
        self.jitterMinLineEdit.setObjectName(u"jitterMinLineEdit")
        self.jitterMinLineEdit.setEnabled(False)
        self.jitterMinLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_15.addWidget(self.jitterMinLineEdit)

        self.horizontalSpacer_7 = QSpacerItem(29, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.label_28 = QLabel(self.layoutWidget_6)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_15.addWidget(self.label_28)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.label_29 = QLabel(self.layoutWidget_6)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_16.addWidget(self.label_29)

        self.horizontalSpacer_33 = QSpacerItem(48, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_33)

        self.jitterMaxLineEdit = QLineEdit(self.layoutWidget_6)
        self.jitterMaxLineEdit.setObjectName(u"jitterMaxLineEdit")
        self.jitterMaxLineEdit.setEnabled(False)
        self.jitterMaxLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_16.addWidget(self.jitterMaxLineEdit)

        self.horizontalSpacer_8 = QSpacerItem(18, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.label_30 = QLabel(self.layoutWidget_6)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_16.addWidget(self.label_30)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.layoutWidget = QWidget(self.DataAugmentationFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 30, 251, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.horizontalSpacer_41 = QSpacerItem(16, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_41)

        self.hFlipLineEdit = QLineEdit(self.layoutWidget)
        self.hFlipLineEdit.setObjectName(u"hFlipLineEdit")
        self.hFlipLineEdit.setEnabled(False)
        self.hFlipLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.hFlipLineEdit)

        self.horizontalSpacer_19 = QSpacerItem(32, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_19)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.layoutWidget1 = QWidget(self.DataAugmentationFrame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 200, 251, 74))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.AutoText)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_24 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_24)

        self.gBlurSigMinLineEdit = QLineEdit(self.layoutWidget1)
        self.gBlurSigMinLineEdit.setObjectName(u"gBlurSigMinLineEdit")
        self.gBlurSigMinLineEdit.setEnabled(False)
        self.gBlurSigMinLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.gBlurSigMinLineEdit)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_22)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.horizontalSpacer_25 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_25)

        self.gBlurSigMaxLineEdit = QLineEdit(self.layoutWidget1)
        self.gBlurSigMaxLineEdit.setObjectName(u"gBlurSigMaxLineEdit")
        self.gBlurSigMaxLineEdit.setEnabled(False)
        self.gBlurSigMaxLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.gBlurSigMaxLineEdit)

        self.horizontalSpacer_23 = QSpacerItem(29, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_23)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(7)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_25.setContentsMargins(-1, -1, 0, -1)
        self.label_48 = QLabel(self.layoutWidget1)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_25.addWidget(self.label_48)

        self.horizontalSpacer_26 = QSpacerItem(18, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_26)

        self.gBlurKernelLineEdit = QLineEdit(self.layoutWidget1)
        self.gBlurKernelLineEdit.setObjectName(u"gBlurKernelLineEdit")
        self.gBlurKernelLineEdit.setEnabled(False)
        self.gBlurKernelLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_25.addWidget(self.gBlurKernelLineEdit)

        self.horizontalSpacer_17 = QSpacerItem(18, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_17)

        self.label_49 = QLabel(self.layoutWidget1)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_25.addWidget(self.label_49)


        self.verticalLayout.addLayout(self.horizontalLayout_25)

        self.layoutWidget2 = QWidget(self.DataAugmentationFrame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(1, 1, 135, 511))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hFlipGroupBox = QGroupBox(self.layoutWidget2)
        self.hFlipGroupBox.setObjectName(u"hFlipGroupBox")
        self.hFlipGroupBox.setFlat(True)
        self.hFlitYesRadioButton = QRadioButton(self.hFlipGroupBox)
        self.hFlitYesRadioButton.setObjectName(u"hFlitYesRadioButton")
        self.hFlitYesRadioButton.setGeometry(QRect(10, 30, 89, 20))
        self.hFlitNoRadioButton = QRadioButton(self.hFlipGroupBox)
        self.hFlitNoRadioButton.setObjectName(u"hFlitNoRadioButton")
        self.hFlitNoRadioButton.setGeometry(QRect(10, 50, 89, 20))
        self.hFlitNoRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.hFlipGroupBox)

        self.linContrastGroupBox = QGroupBox(self.layoutWidget2)
        self.linContrastGroupBox.setObjectName(u"linContrastGroupBox")
        self.linContrastGroupBox.setFlat(True)
        self.linContrastYesRadioButton = QRadioButton(self.linContrastGroupBox)
        self.linContrastYesRadioButton.setObjectName(u"linContrastYesRadioButton")
        self.linContrastYesRadioButton.setGeometry(QRect(10, 30, 89, 20))
        self.linContrastNoRadioButton = QRadioButton(self.linContrastGroupBox)
        self.linContrastNoRadioButton.setObjectName(u"linContrastNoRadioButton")
        self.linContrastNoRadioButton.setGeometry(QRect(10, 50, 89, 20))
        self.linContrastNoRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.linContrastGroupBox)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.gBlurGroupBox = QGroupBox(self.layoutWidget2)
        self.gBlurGroupBox.setObjectName(u"gBlurGroupBox")
        self.gBlurGroupBox.setFlat(True)
        self.gBlurYesRadioButton = QRadioButton(self.gBlurGroupBox)
        self.gBlurYesRadioButton.setObjectName(u"gBlurYesRadioButton")
        self.gBlurYesRadioButton.setGeometry(QRect(10, 30, 89, 20))
        self.gBlurNoRadioButton = QRadioButton(self.gBlurGroupBox)
        self.gBlurNoRadioButton.setObjectName(u"gBlurNoRadioButton")
        self.gBlurNoRadioButton.setGeometry(QRect(10, 50, 89, 20))
        self.gBlurNoRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.gBlurGroupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.affineTransGroupBox = QGroupBox(self.layoutWidget2)
        self.affineTransGroupBox.setObjectName(u"affineTransGroupBox")
        self.affineTransGroupBox.setFlat(True)
        self.affineTransYesRadioButton = QRadioButton(self.affineTransGroupBox)
        self.affineTransYesRadioButton.setObjectName(u"affineTransYesRadioButton")
        self.affineTransYesRadioButton.setGeometry(QRect(10, 30, 89, 20))
        self.affineTransNoRadioButton = QRadioButton(self.affineTransGroupBox)
        self.affineTransNoRadioButton.setObjectName(u"affineTransNoRadioButton")
        self.affineTransNoRadioButton.setGeometry(QRect(10, 50, 89, 20))
        self.affineTransNoRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.affineTransGroupBox)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.jitterGroupBox = QGroupBox(self.layoutWidget2)
        self.jitterGroupBox.setObjectName(u"jitterGroupBox")
        self.jitterGroupBox.setFlat(True)
        self.jitterYesRadioButton = QRadioButton(self.jitterGroupBox)
        self.jitterYesRadioButton.setObjectName(u"jitterYesRadioButton")
        self.jitterYesRadioButton.setGeometry(QRect(10, 30, 89, 20))
        self.jitterNoRadioButton = QRadioButton(self.jitterGroupBox)
        self.jitterNoRadioButton.setObjectName(u"jitterNoRadioButton")
        self.jitterNoRadioButton.setGeometry(QRect(10, 50, 89, 20))
        self.jitterNoRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.jitterGroupBox)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.linContrastGroupBox.raise_()
        self.hFlipGroupBox.raise_()
        self.gBlurGroupBox.raise_()
        self.affineTransGroupBox.raise_()
        self.jitterGroupBox.raise_()
        self.TrainingParametersFrame = QFrame(TrainingScratchWindow)
        self.TrainingParametersFrame.setObjectName(u"TrainingParametersFrame")
        self.TrainingParametersFrame.setGeometry(QRect(450, 240, 361, 511))
        self.TrainingParametersFrame.setFrameShape(QFrame.Box)
        self.TrainingParametersFrame.setFrameShadow(QFrame.Raised)
        self.optSchedulerGroupBox = QGroupBox(self.TrainingParametersFrame)
        self.optSchedulerGroupBox.setObjectName(u"optSchedulerGroupBox")
        self.optSchedulerGroupBox.setGeometry(QRect(10, 320, 133, 81))
        self.optSchedulerGroupBox.setFlat(True)
        self.optSchedulerYesRadioButton = QRadioButton(self.optSchedulerGroupBox)
        self.optSchedulerYesRadioButton.setObjectName(u"optSchedulerYesRadioButton")
        self.optSchedulerYesRadioButton.setGeometry(QRect(10, 30, 89, 20))
        self.optSchedulerNoRadioButton = QRadioButton(self.optSchedulerGroupBox)
        self.optSchedulerNoRadioButton.setObjectName(u"optSchedulerNoRadioButton")
        self.optSchedulerNoRadioButton.setGeometry(QRect(10, 50, 89, 20))
        self.optSchedulerNoRadioButton.setChecked(True)
        self.layoutWidget3 = QWidget(self.TrainingParametersFrame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 70, 301, 221))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_31 = QLabel(self.layoutWidget3)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_17.addWidget(self.label_31)

        self.horizontalSpacer_40 = QSpacerItem(37, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_40)

        self.batchSizeLineEdit = QLineEdit(self.layoutWidget3)
        self.batchSizeLineEdit.setObjectName(u"batchSizeLineEdit")
        self.batchSizeLineEdit.setEnabled(True)
        self.batchSizeLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_17.addWidget(self.batchSizeLineEdit)

        self.horizontalSpacer_9 = QSpacerItem(28, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

        self.label_32 = QLabel(self.layoutWidget3)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_17.addWidget(self.label_32)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_34 = QLabel(self.layoutWidget3)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_18.addWidget(self.label_34)

        self.horizontalSpacer_39 = QSpacerItem(52, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_39)

        self.epochsLineEdit = QLineEdit(self.layoutWidget3)
        self.epochsLineEdit.setObjectName(u"epochsLineEdit")
        self.epochsLineEdit.setEnabled(True)
        self.epochsLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_18.addWidget(self.epochsLineEdit)

        self.horizontalSpacer_10 = QSpacerItem(11, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)

        self.label_35 = QLabel(self.layoutWidget3)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_18.addWidget(self.label_35)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_36 = QLabel(self.layoutWidget3)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_19.addWidget(self.label_36)

        self.horizontalSpacer_38 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_38)

        self.learningRateLineEdit = QLineEdit(self.layoutWidget3)
        self.learningRateLineEdit.setObjectName(u"learningRateLineEdit")
        self.learningRateLineEdit.setEnabled(True)
        self.learningRateLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_19.addWidget(self.learningRateLineEdit)

        self.horizontalSpacer_11 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.label_37 = QLabel(self.layoutWidget3)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_19.addWidget(self.label_37)


        self.verticalLayout_2.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_44 = QLabel(self.layoutWidget3)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_23.addWidget(self.label_44)

        self.horizontalSpacer_37 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_37)

        self.convergenceLineEdit = QLineEdit(self.layoutWidget3)
        self.convergenceLineEdit.setObjectName(u"convergenceLineEdit")
        self.convergenceLineEdit.setEnabled(True)
        self.convergenceLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_23.addWidget(self.convergenceLineEdit)

        self.horizontalSpacer_15 = QSpacerItem(11, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_15)

        self.label_45 = QLabel(self.layoutWidget3)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_23.addWidget(self.label_45)


        self.verticalLayout_2.addLayout(self.horizontalLayout_23)

        self.layoutWidget4 = QWidget(self.TrainingParametersFrame)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 400, 301, 86))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_38 = QLabel(self.layoutWidget4)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_20.addWidget(self.label_38)

        self.horizontalSpacer_34 = QSpacerItem(24, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_34)

        self.schedGammaLineEdit = QLineEdit(self.layoutWidget4)
        self.schedGammaLineEdit.setObjectName(u"schedGammaLineEdit")
        self.schedGammaLineEdit.setEnabled(False)
        self.schedGammaLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_20.addWidget(self.schedGammaLineEdit)

        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.label_39 = QLabel(self.layoutWidget4)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_20.addWidget(self.label_39)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_40 = QLabel(self.layoutWidget4)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_21.addWidget(self.label_40)

        self.horizontalSpacer_35 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_35)

        self.schedPatienceLineEdit = QLineEdit(self.layoutWidget4)
        self.schedPatienceLineEdit.setObjectName(u"schedPatienceLineEdit")
        self.schedPatienceLineEdit.setEnabled(False)
        self.schedPatienceLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_21.addWidget(self.schedPatienceLineEdit)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_13)

        self.label_41 = QLabel(self.layoutWidget4)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_21.addWidget(self.label_41)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_42 = QLabel(self.layoutWidget4)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_22.addWidget(self.label_42)

        self.horizontalSpacer_36 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_36)

        self.schedThresholdLineEdit = QLineEdit(self.layoutWidget4)
        self.schedThresholdLineEdit.setObjectName(u"schedThresholdLineEdit")
        self.schedThresholdLineEdit.setEnabled(False)
        self.schedThresholdLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.schedThresholdLineEdit)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_14)

        self.label_43 = QLabel(self.layoutWidget4)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_22.addWidget(self.label_43)


        self.verticalLayout_9.addLayout(self.horizontalLayout_22)

        self.layoutWidget5 = QWidget(self.TrainingParametersFrame)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 10, 152, 64))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.loadDataButton = QPushButton(self.layoutWidget5)
        self.loadDataButton.setObjectName(u"loadDataButton")

        self.verticalLayout_6.addWidget(self.loadDataButton)

        self.dataPathLabel = QLabel(self.layoutWidget5)
        self.dataPathLabel.setObjectName(u"dataPathLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.dataPathLabel.sizePolicy().hasHeightForWidth())
        self.dataPathLabel.setSizePolicy(sizePolicy)
        self.dataPathLabel.setMinimumSize(QSize(150, 0))

        self.verticalLayout_6.addWidget(self.dataPathLabel)

        self.label_12 = QLabel(TrainingScratchWindow)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 210, 241, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_13 = QLabel(TrainingScratchWindow)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(460, 210, 171, 31))
        self.label_13.setFont(font)
        self.layoutWidget6 = QWidget(TrainingScratchWindow)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(70, 770, 710, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cancelButton = QPushButton(self.layoutWidget6)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_3.addWidget(self.cancelButton)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.yamlFileButton = QPushButton(self.layoutWidget6)
        self.yamlFileButton.setObjectName(u"yamlFileButton")

        self.horizontalLayout_3.addWidget(self.yamlFileButton)

        self.horizontalSpacer_4 = QSpacerItem(23, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.trainButton = QPushButton(self.layoutWidget6)
        self.trainButton.setObjectName(u"trainButton")

        self.horizontalLayout_3.addWidget(self.trainButton)

        self.layoutWidget7 = QWidget(TrainingScratchWindow)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(110, 160, 251, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ftLayerLabel = QLabel(self.layoutWidget7)
        self.ftLayerLabel.setObjectName(u"ftLayerLabel")
        self.ftLayerLabel.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.ftLayerLabel)

        self.ftLayerComboBox = QComboBox(self.layoutWidget7)
        self.ftLayerComboBox.setObjectName(u"ftLayerComboBox")
        self.ftLayerComboBox.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.ftLayerComboBox)

        self.layoutWidget_13 = QWidget(TrainingScratchWindow)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(230, 80, 301, 24))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ftLayerLabel_2 = QLabel(self.layoutWidget_13)
        self.ftLayerLabel_2.setObjectName(u"ftLayerLabel_2")
        self.ftLayerLabel_2.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.ftLayerLabel_2)

        self.networkTypeComboBox = QComboBox(self.layoutWidget_13)
        self.networkTypeComboBox.setObjectName(u"networkTypeComboBox")
        self.networkTypeComboBox.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.networkTypeComboBox)

        self.customModelGroupBox = QGroupBox(TrainingScratchWindow)
        self.customModelGroupBox.setObjectName(u"customModelGroupBox")
        self.customModelGroupBox.setGeometry(QRect(20, 40, 231, 80))
        self.customModelGroupBox.setContextMenuPolicy(Qt.PreventContextMenu)
        self.customModelGroupBox.setLayoutDirection(Qt.LeftToRight)
        self.customModelGroupBox.setFlat(True)
        self.customModelGroupBox.setCheckable(False)
        self.customModelYesRadioButton = QRadioButton(self.customModelGroupBox)
        self.customModelYesRadioButton.setObjectName(u"customModelYesRadioButton")
        self.customModelYesRadioButton.setEnabled(True)
        self.customModelYesRadioButton.setGeometry(QRect(20, 30, 89, 20))
        self.customModelYesRadioButton.setLayoutDirection(Qt.LeftToRight)
        self.customModelNoRadioButton = QRadioButton(self.customModelGroupBox)
        self.customModelNoRadioButton.setObjectName(u"customModelNoRadioButton")
        self.customModelNoRadioButton.setGeometry(QRect(20, 50, 89, 20))
        self.customModelNoRadioButton.setChecked(True)
        self.layoutWidget_2 = QWidget(TrainingScratchWindow)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(560, 80, 251, 24))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.customLayersLineEdit = QLineEdit(self.layoutWidget_2)
        self.customLayersLineEdit.setObjectName(u"customLayersLineEdit")
        self.customLayersLineEdit.setEnabled(False)
        self.customLayersLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.customLayersLineEdit)

        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.layoutWidget_5 = QWidget(TrainingScratchWindow)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(520, 160, 261, 24))
        self.horizontalLayout_27 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.ftLayerLabel_3 = QLabel(self.layoutWidget_5)
        self.ftLayerLabel_3.setObjectName(u"ftLayerLabel_3")
        self.ftLayerLabel_3.setEnabled(True)

        self.horizontalLayout_27.addWidget(self.ftLayerLabel_3)

        self.pretrainingComboBox = QComboBox(self.layoutWidget_5)
        self.pretrainingComboBox.setObjectName(u"pretrainingComboBox")
        self.pretrainingComboBox.setEnabled(False)

        self.horizontalLayout_27.addWidget(self.pretrainingComboBox)

        self.pretrainingGroupBox = QGroupBox(TrainingScratchWindow)
        self.pretrainingGroupBox.setObjectName(u"pretrainingGroupBox")
        self.pretrainingGroupBox.setGeometry(QRect(430, 130, 91, 80))
        self.pretrainingGroupBox.setContextMenuPolicy(Qt.PreventContextMenu)
        self.pretrainingGroupBox.setLayoutDirection(Qt.LeftToRight)
        self.pretrainingGroupBox.setFlat(True)
        self.pretrainingGroupBox.setCheckable(False)
        self.pretrainingYesRadioButton = QRadioButton(self.pretrainingGroupBox)
        self.pretrainingYesRadioButton.setObjectName(u"pretrainingYesRadioButton")
        self.pretrainingYesRadioButton.setEnabled(True)
        self.pretrainingYesRadioButton.setGeometry(QRect(20, 30, 89, 20))
        self.pretrainingYesRadioButton.setLayoutDirection(Qt.LeftToRight)
        self.pretrainingNoRadioButton = QRadioButton(self.pretrainingGroupBox)
        self.pretrainingNoRadioButton.setObjectName(u"pretrainingNoRadioButton")
        self.pretrainingNoRadioButton.setGeometry(QRect(20, 50, 89, 20))
        self.pretrainingNoRadioButton.setChecked(True)
        self.layoutWidget7.raise_()
        self.layoutWidget7.raise_()
        self.finetuningGroupBox.raise_()
        self.TrainingParametersFrame.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.DataAugmentationFrame.raise_()
        self.dataLabel.raise_()
        self.layoutWidget_13.raise_()
        self.customModelGroupBox.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_5.raise_()
        self.pretrainingGroupBox.raise_()

        self.retranslateUi(TrainingScratchWindow)

        QMetaObject.connectSlotsByName(TrainingScratchWindow)
    # setupUi

    def retranslateUi(self, TrainingScratchWindow):
        TrainingScratchWindow.setWindowTitle(QCoreApplication.translate("TrainingScratchWindow", u"Network training", None))
        self.dataLabel.setText(QCoreApplication.translate("TrainingScratchWindow", u"Training on hand gestures dataset", None))
        self.finetuningGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"FineTuning :", None))
        self.ftYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.ftNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.label_17.setText(QCoreApplication.translate("TrainingScratchWindow", u"Min  :", None))
        self.linContrastMinLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0", None))
        self.label_19.setText(QCoreApplication.translate("TrainingScratchWindow", u"Max :", None))
        self.linContrastMaxLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"1.2", None))
        self.label_20.setText(QCoreApplication.translate("TrainingScratchWindow", u"<= 1.2", None))
        self.label_21.setText(QCoreApplication.translate("TrainingScratchWindow", u"Probability :", None))
        self.affineTransProbaLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.8", None))
        self.label_22.setText(QCoreApplication.translate("TrainingScratchWindow", u"[0:1]", None))
        self.label_25.setText(QCoreApplication.translate("TrainingScratchWindow", u"Min :", None))
        self.affineTransMinLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.8", None))
        self.label_26.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0.5", None))
        self.label_23.setText(QCoreApplication.translate("TrainingScratchWindow", u"Max :", None))
        self.affineTransMaxLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"1.2", None))
        self.label_24.setText(QCoreApplication.translate("TrainingScratchWindow", u"<= 1.3", None))
        self.label_50.setText(QCoreApplication.translate("TrainingScratchWindow", u"Rotation angle :", None))
        self.affineTransAngleRotLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0", None))
        self.label_51.setText(QCoreApplication.translate("TrainingScratchWindow", u"[0:359]", None))
        self.label_46.setText(QCoreApplication.translate("TrainingScratchWindow", u"Hue :", None))
        self.jitterHueLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0", None))
        self.label_47.setText(QCoreApplication.translate("TrainingScratchWindow", u"[0:0.5]", None))
        self.label_27.setText(QCoreApplication.translate("TrainingScratchWindow", u"Min  :", None))
        self.jitterMinLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.8", None))
        self.label_28.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0", None))
        self.label_29.setText(QCoreApplication.translate("TrainingScratchWindow", u"Max :", None))
        self.jitterMaxLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"1.2", None))
        self.label_30.setText(QCoreApplication.translate("TrainingScratchWindow", u"<= 1.2", None))
        self.label.setText(QCoreApplication.translate("TrainingScratchWindow", u"Probability :", None))
        self.hFlipLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.5", None))
        self.label_3.setText(QCoreApplication.translate("TrainingScratchWindow", u"[0:1]", None))
        self.label_2.setText(QCoreApplication.translate("TrainingScratchWindow", u"Sigma min :", None))
        self.gBlurSigMinLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.1", None))
        self.label_4.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0.1", None))
        self.label_14.setText(QCoreApplication.translate("TrainingScratchWindow", u"Sigma max :", None))
        self.gBlurSigMaxLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"1", None))
        self.label_5.setText(QCoreApplication.translate("TrainingScratchWindow", u"<= 1", None))
        self.label_48.setText(QCoreApplication.translate("TrainingScratchWindow", u"Kernel size ", None))
        self.gBlurKernelLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"1.2", None))
        self.label_49.setText(QCoreApplication.translate("TrainingScratchWindow", u"<= 1.2", None))
        self.hFlipGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Horizontal flip:", None))
        self.hFlitYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.hFlitNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.linContrastGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Linear Contrast", None))
        self.linContrastYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.linContrastNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.gBlurGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Gaussian blur", None))
        self.gBlurYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.gBlurNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.affineTransGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Affine transformation", None))
        self.affineTransYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.affineTransNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.jitterGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Jitter", None))
        self.jitterYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.jitterNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.optSchedulerGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Optimizer scheduler", None))
        self.optSchedulerYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.optSchedulerNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.label_31.setText(QCoreApplication.translate("TrainingScratchWindow", u"Batch size :", None))
        self.batchSizeLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"1024", None))
        self.label_32.setText(QCoreApplication.translate("TrainingScratchWindow", u"[]", None))
        self.label_34.setText(QCoreApplication.translate("TrainingScratchWindow", u"Epochs :", None))
        self.epochsLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"1000", None))
        self.label_35.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 1", None))
        self.label_36.setText(QCoreApplication.translate("TrainingScratchWindow", u"Learning rate :", None))
        self.learningRateLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.001", None))
        self.label_37.setText(QCoreApplication.translate("TrainingScratchWindow", u">0", None))
        self.label_44.setText(QCoreApplication.translate("TrainingScratchWindow", u"Convergence :", None))
        self.convergenceLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"50", None))
        self.label_45.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0", None))
        self.label_38.setText(QCoreApplication.translate("TrainingScratchWindow", u"Scheduler gamma :", None))
        self.schedGammaLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.2", None))
        self.label_39.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0", None))
        self.label_40.setText(QCoreApplication.translate("TrainingScratchWindow", u"Scheduler patience :", None))
        self.schedPatienceLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"100", None))
        self.label_41.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0", None))
        self.label_42.setText(QCoreApplication.translate("TrainingScratchWindow", u"Scheduler threshold :", None))
        self.schedThresholdLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"0.0001", None))
        self.label_43.setText(QCoreApplication.translate("TrainingScratchWindow", u">= 0", None))
        self.loadDataButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Load Data", None))
        self.dataPathLabel.setText(QCoreApplication.translate("TrainingScratchWindow", u"Path : ", None))
        self.label_12.setText(QCoreApplication.translate("TrainingScratchWindow", u"Data augmentation Parameters", None))
        self.label_13.setText(QCoreApplication.translate("TrainingScratchWindow", u"Training Parameters", None))
        self.cancelButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Cancel", None))
        self.yamlFileButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Create and save the parameter file", None))
        self.trainButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Train the network", None))
        self.ftLayerLabel.setText(QCoreApplication.translate("TrainingScratchWindow", u"From layer :", None))
        self.ftLayerLabel_2.setText(QCoreApplication.translate("TrainingScratchWindow", u"Choose the model :", None))
        self.customModelGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Do you want to create a custom model?", None))
        self.customModelYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.customModelNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
        self.label_6.setText(QCoreApplication.translate("TrainingScratchWindow", u"Custom layers :", None))
        self.customLayersLineEdit.setText(QCoreApplication.translate("TrainingScratchWindow", u"[3, 3, 3]", None))
        self.label_7.setText(QCoreApplication.translate("TrainingScratchWindow", u"(as a list [a, b, c])", None))
        self.ftLayerLabel_3.setText(QCoreApplication.translate("TrainingScratchWindow", u"On the dataset :", None))
        self.pretrainingGroupBox.setTitle(QCoreApplication.translate("TrainingScratchWindow", u"Pretraining:", None))
        self.pretrainingYesRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"Yes", None))
        self.pretrainingNoRadioButton.setText(QCoreApplication.translate("TrainingScratchWindow", u"No", None))
    # retranslateUi


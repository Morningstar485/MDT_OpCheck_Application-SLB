# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Design_3_TestinghqBmZP.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QDialog, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(887, 675)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 26))

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)

        self.frame_15 = QFrame(Dialog)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(41, 41))
        self.label_15.setMaximumSize(QSize(41, 41))
        self.label_15.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.GB8 = QGroupBox(self.frame_17)
        self.GB8.setObjectName(u"GB8")
        self.GB8.setMinimumSize(QSize(210, 0))
        self.GB8.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB8.setCheckable(False)
        self.GB8.setChecked(False)
        self.verticalLayout_21 = QVBoxLayout(self.GB8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.R17 = QRadioButton(self.GB8)
        self.R17.setObjectName(u"R17")
        self.R17.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_21.addWidget(self.R17)

        self.R18 = QRadioButton(self.GB8)
        self.R18.setObjectName(u"R18")
        self.R18.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_21.addWidget(self.R18)


        self.horizontalLayout_9.addWidget(self.GB8)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.CB2 = QCheckBox(self.frame_15)
        self.CB2.setObjectName(u"CB2")
        self.CB2.setEnabled(True)
        self.CB2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.CB2)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_16)

        self.GB9 = QGroupBox(self.frame_18)
        self.GB9.setObjectName(u"GB9")
        self.GB9.setMinimumSize(QSize(210, 0))
        self.GB9.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB9.setCheckable(False)
        self.GB9.setChecked(False)
        self.verticalLayout_22 = QVBoxLayout(self.GB9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.R19 = QRadioButton(self.GB9)
        self.R19.setObjectName(u"R19")
        self.R19.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_22.addWidget(self.R19)

        self.R20 = QRadioButton(self.GB9)
        self.R20.setObjectName(u"R20")
        self.R20.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_22.addWidget(self.R20)


        self.horizontalLayout_10.addWidget(self.GB9)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.CB3 = QCheckBox(self.frame_15)
        self.CB3.setObjectName(u"CB3")
        self.CB3.setEnabled(True)
        self.CB3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.CB3)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.frame_19)
        self.label.setObjectName(u"label")

        self.verticalLayout_9.addWidget(self.label)

        self.comboBox = QComboBox(self.frame_19)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 25))
        self.comboBox.setMaximumSize(QSize(150, 25))

        self.verticalLayout_9.addWidget(self.comboBox)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(41, 41))
        self.label_17.setMaximumSize(QSize(41, 41))
        self.label_17.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_17)

        self.GB10 = QGroupBox(self.frame_20)
        self.GB10.setObjectName(u"GB10")
        self.GB10.setMinimumSize(QSize(210, 0))
        self.GB10.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB10.setCheckable(False)
        self.GB10.setChecked(False)
        self.verticalLayout_23 = QVBoxLayout(self.GB10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.R21 = QRadioButton(self.GB10)
        self.R21.setObjectName(u"R21")
        self.R21.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_23.addWidget(self.R21)

        self.R22 = QRadioButton(self.GB10)
        self.R22.setObjectName(u"R22")
        self.R22.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_23.addWidget(self.R22)


        self.horizontalLayout_11.addWidget(self.GB10)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.CB4 = QCheckBox(self.frame_15)
        self.CB4.setObjectName(u"CB4")
        self.CB4.setEnabled(True)
        self.CB4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.CB4)

        self.CB5 = QCheckBox(self.frame_15)
        self.CB5.setObjectName(u"CB5")
        self.CB5.setEnabled(True)
        self.CB5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.CB5)

        self.GB11 = QGroupBox(self.frame_15)
        self.GB11.setObjectName(u"GB11")
        self.GB11.setMinimumSize(QSize(210, 0))
        self.GB11.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB11.setCheckable(False)
        self.GB11.setChecked(False)
        self.verticalLayout_24 = QVBoxLayout(self.GB11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.R23 = QRadioButton(self.GB11)
        self.R23.setObjectName(u"R23")
        self.R23.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_24.addWidget(self.R23)

        self.R24 = QRadioButton(self.GB11)
        self.R24.setObjectName(u"R24")
        self.R24.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_24.addWidget(self.R24)


        self.verticalLayout_11.addWidget(self.GB11)

        self.frame_23 = QFrame(self.frame_15)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_23)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(41, 41))
        self.label_21.setMaximumSize(QSize(41, 41))
        self.label_21.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.GB12 = QGroupBox(self.frame_23)
        self.GB12.setObjectName(u"GB12")
        self.GB12.setMinimumSize(QSize(210, 0))
        self.GB12.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB12.setCheckable(False)
        self.GB12.setChecked(False)
        self.verticalLayout_26 = QVBoxLayout(self.GB12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.R25 = QRadioButton(self.GB12)
        self.R25.setObjectName(u"R25")
        self.R25.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_26.addWidget(self.R25)

        self.R26 = QRadioButton(self.GB12)
        self.R26.setObjectName(u"R26")
        self.R26.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_26.addWidget(self.R26)


        self.horizontalLayout_14.addWidget(self.GB12)


        self.verticalLayout_11.addWidget(self.frame_23)

        self.CB6 = QCheckBox(self.frame_15)
        self.CB6.setObjectName(u"CB6")
        self.CB6.setEnabled(True)
        self.CB6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.CB6)


        self.gridLayout.addWidget(self.frame_15, 0, 3, 2, 1)

        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_12)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(41, 41))
        self.label_11.setMaximumSize(QSize(41, 41))
        self.label_11.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_11.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_11)

        self.GB1 = QGroupBox(self.frame_12)
        self.GB1.setObjectName(u"GB1")
        self.GB1.setMinimumSize(QSize(190, 0))
        self.GB1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 100px;\n"
"}\n"
"")
        self.GB1.setCheckable(False)
        self.GB1.setChecked(False)
        self.verticalLayout_19 = QVBoxLayout(self.GB1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.R1 = QRadioButton(self.GB1)
        self.R1.setObjectName(u"R1")
        self.R1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_19.addWidget(self.R1)

        self.R2 = QRadioButton(self.GB1)
        self.R2.setObjectName(u"R2")
        self.R2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_19.addWidget(self.R2)


        self.horizontalLayout.addWidget(self.GB1)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(41, 41))
        self.label_4.setMaximumSize(QSize(41, 41))
        self.label_4.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.GB2 = QGroupBox(self.frame_2)
        self.GB2.setObjectName(u"GB2")
        self.GB2.setMinimumSize(QSize(190, 0))
        self.GB2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB2.setCheckable(False)
        self.GB2.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.GB2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.R3 = QRadioButton(self.GB2)
        self.R3.setObjectName(u"R3")
        self.R3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.R3)

        self.R4 = QRadioButton(self.GB2)
        self.R4.setObjectName(u"R4")
        self.R4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.R4)


        self.horizontalLayout_2.addWidget(self.GB2)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.frame)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(180, 25))
        self.lineEdit_1.setMaximumSize(QSize(180, 25))

        self.verticalLayout.addWidget(self.lineEdit_1)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_7)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(41, 41))
        self.label_5.setMaximumSize(QSize(41, 41))
        self.label_5.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.GB3 = QGroupBox(self.frame_4)
        self.GB3.setObjectName(u"GB3")
        self.GB3.setMinimumSize(QSize(210, 0))
        self.GB3.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB3.setCheckable(False)
        self.GB3.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.GB3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.R5 = QRadioButton(self.GB3)
        self.R5.setObjectName(u"R5")
        self.R5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.R5)

        self.R6 = QRadioButton(self.GB3)
        self.R6.setObjectName(u"R6")
        self.R6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.R6)


        self.horizontalLayout_3.addWidget(self.GB3)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.CB1 = QCheckBox(self.frame_7)
        self.CB1.setObjectName(u"CB1")
        self.CB1.setEnabled(True)
        self.CB1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_4.addWidget(self.CB1)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(150, 25))
        self.comboBox_2.setMaximumSize(QSize(150, 25))

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(125, 25))
        self.lineEdit_2.setMaximumSize(QSize(125, 25))

        self.verticalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(41, 41))
        self.label_6.setMaximumSize(QSize(41, 41))
        self.label_6.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.GB4 = QGroupBox(self.frame_5)
        self.GB4.setObjectName(u"GB4")
        self.GB4.setMinimumSize(QSize(210, 0))
        self.GB4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB4.setCheckable(False)
        self.GB4.setChecked(False)
        self.verticalLayout_16 = QVBoxLayout(self.GB4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.R7 = QRadioButton(self.GB4)
        self.R7.setObjectName(u"R7")
        self.R7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.R7)

        self.R8 = QRadioButton(self.GB4)
        self.R8.setObjectName(u"R8")
        self.R8.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.R8)


        self.horizontalLayout_4.addWidget(self.GB4)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 26))

        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.frame_16 = QFrame(Dialog)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_6 = QFrame(self.frame_16)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(41, 41))
        self.label_7.setMaximumSize(QSize(41, 41))
        self.label_7.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.GB5 = QGroupBox(self.frame_6)
        self.GB5.setObjectName(u"GB5")
        self.GB5.setMinimumSize(QSize(210, 0))
        self.GB5.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB5.setCheckable(False)
        self.GB5.setChecked(False)
        self.verticalLayout_17 = QVBoxLayout(self.GB5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.R9 = QRadioButton(self.GB5)
        self.R9.setObjectName(u"R9")
        self.R9.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_17.addWidget(self.R9)

        self.R10 = QRadioButton(self.GB5)
        self.R10.setObjectName(u"R10")
        self.R10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_17.addWidget(self.R10)


        self.horizontalLayout_5.addWidget(self.GB5)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.frame_11 = QFrame(self.frame_16)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(41, 41))
        self.label_10.setMaximumSize(QSize(41, 41))
        self.label_10.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.GB6 = QGroupBox(self.frame_11)
        self.GB6.setObjectName(u"GB6")
        self.GB6.setMinimumSize(QSize(190, 0))
        self.GB6.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB6.setCheckable(False)
        self.GB6.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.GB6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.R11 = QRadioButton(self.GB6)
        self.R11.setObjectName(u"R11")
        self.R11.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.R11)

        self.R12 = QRadioButton(self.GB6)
        self.R12.setObjectName(u"R12")
        self.R12.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.R12)


        self.horizontalLayout_7.addWidget(self.GB6)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_16)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(180, 25))
        self.lineEdit_3.setMaximumSize(QSize(180, 25))

        self.verticalLayout_5.addWidget(self.lineEdit_3)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_16)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(41, 41))
        self.label_8.setMaximumSize(QSize(41, 41))
        self.label_8.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.GB7 = QGroupBox(self.frame_9)
        self.GB7.setObjectName(u"GB7")
        self.GB7.setMinimumSize(QSize(210, 0))
        self.GB7.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.GB7.setCheckable(False)
        self.GB7.setChecked(False)
        self.verticalLayout_18 = QVBoxLayout(self.GB7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.R13 = QRadioButton(self.GB7)
        self.R13.setObjectName(u"R13")
        self.R13.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_18.addWidget(self.R13)

        self.R14 = QRadioButton(self.GB7)
        self.R14.setObjectName(u"R14")
        self.R14.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_18.addWidget(self.R14)


        self.horizontalLayout_6.addWidget(self.GB7)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_21 = QFrame(self.frame_16)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.lineEdit_5 = QLineEdit(self.frame_21)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(125, 25))
        self.lineEdit_5.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_5)


        self.verticalLayout_8.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_22)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_19 = QLabel(self.frame_22)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_10.addWidget(self.label_19)

        self.dateTimeEdit_2 = QDateTimeEdit(self.frame_22)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.verticalLayout_10.addWidget(self.dateTimeEdit_2)


        self.verticalLayout_8.addWidget(self.frame_22)

        self.frame_13 = QFrame(self.frame_16)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.dateTimeEdit = QDateTimeEdit(self.frame_13)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout_6.addWidget(self.dateTimeEdit)


        self.verticalLayout_8.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_16)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.lineEdit_4 = QLineEdit(self.frame_14)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(125, 25))
        self.lineEdit_4.setMaximumSize(QSize(125, 25))

        self.verticalLayout_7.addWidget(self.lineEdit_4)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.gridLayout.addWidget(self.frame_16, 0, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Go Back", None))
        self.label_15.setText("")
        self.GB8.setTitle(QCoreApplication.translate("Dialog", u"Are HT Tools Available?", None))
        self.R17.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R18.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.CB2.setText(QCoreApplication.translate("Dialog", u"Informed PSD/JDL/Base", None))
        self.label_16.setText("")
        self.GB9.setTitle(QCoreApplication.translate("Dialog", u"Is the Solid % > 15%", None))
        self.R19.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R20.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.CB3.setText(QCoreApplication.translate("Dialog", u"Informed PSD/JDL/Base", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Select the Hole Size</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"17.5 Inches", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"12.25 Inches", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"8.5 Inches", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"6 Inches", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select", None))
        self.label_17.setText("")
        self.GB10.setTitle(QCoreApplication.translate("Dialog", u"Is MRSL Available?", None))
        self.R21.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R22.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.CB4.setText(QCoreApplication.translate("Dialog", u"Informed PSD/JDL/Base", None))
        self.CB5.setText(QCoreApplication.translate("Dialog", u"Check 6.125R CT Bonded Packer", None))
        self.GB11.setTitle(QCoreApplication.translate("Dialog", u"What is the Mud Type?", None))
        self.R23.setText(QCoreApplication.translate("Dialog", u"Water Based", None))
        self.R24.setText(QCoreApplication.translate("Dialog", u"Synthetic Oil Based", None))
        self.label_21.setText("")
        self.GB12.setTitle(QCoreApplication.translate("Dialog", u"Is LFA/MIFA Available?", None))
        self.R25.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R26.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.CB6.setText(QCoreApplication.translate("Dialog", u"Informed PSD/JDL/Base", None))
        self.label_11.setText("")
        self.GB1.setTitle(QCoreApplication.translate("Dialog", u"Is the PCP Competency Fulfilled?", None))
        self.R1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_4.setText("")
        self.GB2.setTitle(QCoreApplication.translate("Dialog", u"Has the excemption been raised?", None))
        self.R3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Enter Excemption Sr. No.</span></p></body></html>", None))
        self.label_5.setText("")
        self.GB3.setTitle(QCoreApplication.translate("Dialog", u"Has the excemption been approved?", None))
        self.R5.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R6.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.CB1.setText(QCoreApplication.translate("Dialog", u"Briefing Done with PSD", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Select the Conveyance</span></p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"WL", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"TLC", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("Dialog", u"Select", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Enter Weak Point</span></p></body></html>", None))
        self.label_6.setText("")
        self.GB4.setTitle(QCoreApplication.translate("Dialog", u"Is the Tool Planner Ready?", None))
        self.R7.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R8.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Complete Design & Move to Tool String Declaration", None))
        self.label_7.setText("")
        self.GB5.setTitle(QCoreApplication.translate("Dialog", u"Is MEMS Report Valid?", None))
        self.R9.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R10.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_10.setText("")
        self.GB6.setTitle(QCoreApplication.translate("Dialog", u"Has the excemption been raised?", None))
        self.R11.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R12.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Enter Excemption Sr. No.</span></p></body></html>", None))
        self.label_8.setText("")
        self.GB7.setTitle(QCoreApplication.translate("Dialog", u"Has the excemption been approved?", None))
        self.R13.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.R14.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tool Operation %</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Last OST with Telemetry Check Done in Base</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Expected Rig Up Date and Time</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Expected Well Temperature</span></p></body></html>", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

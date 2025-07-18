from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(657,698)
        self.verticalLayout_9 = QVBoxLayout(Dialog)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_9 = QFrame(Dialog)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_1 = QGroupBox(self.frame_9)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(280, 0))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Radio_Frame_1 = QFrame(self.groupBox_1)
        self.Radio_Frame_1.setObjectName(u"Radio_Frame_1")
        self.Radio_Frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Radio_Frame_1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_1 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_2)


        self.verticalLayout_11.addWidget(self.Radio_Frame_1)


        self.horizontalLayout.addWidget(self.groupBox_1)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(41, 41))
        self.label_12.setMaximumSize(QSize(41, 41))
        self.label_12.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)


        self.horizontalLayout.addWidget(self.frame_12)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(Dialog)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.frame_10)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Radio_Frame_2 = QFrame(self.groupBox_2)
        self.Radio_Frame_2.setObjectName(u"Radio_Frame_2")
        self.Radio_Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Radio_Frame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_3 = QRadioButton(self.Radio_Frame_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.Radio_Frame_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_4)
        self.verticalLayout_13.addWidget(self.Radio_Frame_2)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(41, 41))
        self.label_14.setMaximumSize(QSize(41, 41))
        self.label_14.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_1 = QCheckBox(self.frame)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_1)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.frame_11 = QFrame(Dialog)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_3 = QGroupBox(self.frame_11)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(280, 0))
        self.groupBox_3.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Radio_Frame_3 = QFrame(self.groupBox_3)
        self.Radio_Frame_3.setObjectName(u"Radio_Frame_3")
        self.Radio_Frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Radio_Frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_5 = QRadioButton(self.Radio_Frame_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.Radio_Frame_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_6)


        self.verticalLayout_15.addWidget(self.Radio_Frame_3)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.frame_3 = QFrame(self.frame_11)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_9.addWidget(self.label_17)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_2 = QCheckBox(self.frame_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_2)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_9.addWidget(self.frame_11)

        self.frame_17 = QFrame(Dialog)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_4 = QGroupBox(self.frame_17)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(280, 0))
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.Radio_Frame_4 = QFrame(self.groupBox_4)
        self.Radio_Frame_4.setObjectName(u"Radio_Frame_4")
        self.Radio_Frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Radio_Frame_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.radioButton_7 = QRadioButton(self.Radio_Frame_4)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_18.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.Radio_Frame_4)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_18.addWidget(self.radioButton_8)


        self.verticalLayout_17.addWidget(self.Radio_Frame_4)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.frame_5 = QFrame(self.frame_17)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(41, 41))
        self.label_18.setMaximumSize(QSize(41, 41))
        self.label_18.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_3 = QCheckBox(self.frame_6)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_3)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_19 = QFrame(Dialog)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(280, 0))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_5 = QGroupBox(self.frame_19)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setChecked(False)
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.Radio_Frame_5 = QFrame(self.groupBox_5)
        self.Radio_Frame_5.setObjectName(u"Radio_Frame_5")
        self.Radio_Frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.Radio_Frame_5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.radioButton_9 = QRadioButton(self.Radio_Frame_5)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_20.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.Radio_Frame_5)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_20.addWidget(self.radioButton_10)


        self.verticalLayout_19.addWidget(self.Radio_Frame_5)


        self.horizontalLayout_5.addWidget(self.groupBox_5)

        self.frame_7 = QFrame(self.frame_19)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(41, 41))
        self.label_20.setMaximumSize(QSize(41, 41))
        self.label_20.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_11.addWidget(self.label_21)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_4 = QCheckBox(self.frame_8)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.checkBox_4)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.horizontalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_9.addWidget(self.frame_19)

        self.frame_18 = QFrame(Dialog)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton = QPushButton(self.frame_18)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_10.addWidget(self.pushButton)


        self.verticalLayout_9.addWidget(self.frame_18)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Is EDTA available in with MDT Set?", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Cannot do job without EDTA</span></p><p><span style=\" font-size:16pt; font-style:italic;\">Inform PSD/JDL Urgently</span></p></body></html>", None))
        

        self.frame_12.setVisible(False)  
        self.frame_2.setVisible(False)   
        self.frame_3.setVisible(False)   
        self.frame_5.setVisible(False)   
        self.frame_7.setVisible(False)
        
        self.initialize_progressive_form()
        
        self.setup_progressive_signals()
        
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"MRPP and MRTM with cable, are 2 sets available?", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Inform Base</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"MDT Lifting cap available?", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Inform Base</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"MDT Vertical make up plate available?", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_8.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Inform Base</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Sample draining equipment available?", None))
        self.radioButton_9.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Inform Base</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi
    
    def initialize_progressive_form(self):
        groupboxes_to_disable = [
            self.groupBox_2, self.groupBox_3, self.groupBox_4, self.groupBox_5
        ]
        
        # Disable all groupboxes except the first one
        for groupbox in groupboxes_to_disable:
            groupbox.setEnabled(False)
        
        # Disable push button initially
        self.pushButton.setEnabled(False)
    
    def setup_progressive_signals(self):
        self.radioButton_1.toggled.connect(lambda checked: self.handle_groupbox1_selection() if checked else None)
        self.radioButton_2.toggled.connect(lambda checked: self.handle_groupbox1_selection() if checked else None)
        
        # GroupBox 2 - normal progression with checkbox
        self.radioButton_3.toggled.connect(lambda checked: self.handle_groupbox2_selection() if checked else None)
        self.radioButton_4.toggled.connect(lambda checked: self.handle_groupbox2_selection() if checked else None)
        self.checkBox_1.toggled.connect(lambda: self.check_groupbox2_progression())
        
        # GroupBox 3 - normal progression with checkbox
        self.radioButton_5.toggled.connect(lambda checked: self.handle_groupbox3_selection() if checked else None)
        self.radioButton_6.toggled.connect(lambda checked: self.handle_groupbox3_selection() if checked else None)
        self.checkBox_2.toggled.connect(lambda: self.check_groupbox3_progression())
        
        # GroupBox 4 - normal progression with checkbox
        self.radioButton_7.toggled.connect(lambda checked: self.handle_groupbox4_selection() if checked else None)
        self.radioButton_8.toggled.connect(lambda checked: self.handle_groupbox4_selection() if checked else None)
        self.checkBox_3.toggled.connect(lambda: self.check_groupbox4_progression())
        
        # GroupBox 5 - final groupbox with checkbox
        self.radioButton_9.toggled.connect(lambda checked: self.handle_groupbox5_selection() if checked else None)
        self.radioButton_10.toggled.connect(lambda checked: self.handle_groupbox5_selection() if checked else None)
        self.checkBox_4.toggled.connect(lambda: self.check_groupbox5_progression())
    
    def handle_groupbox1_selection(self):
        
        if self.radioButton_1.isChecked():  # Yes selected
            # Enable next groupbox directly
            self.groupBox_2.setEnabled(True)
        elif self.radioButton_2.isChecked():  # No selected
            # Show warning frame (no checkbox here, just display)
            self.frame_12.setVisible(True)
            # Still enable next groupbox since there's no checkbox to wait for
            self.groupBox_2.setEnabled(True)
    
    def handle_groupbox2_selection(self):
        
        self.frame_2.setVisible(False)
        self.checkBox_1.setChecked(False)
        self.groupBox_3.setEnabled(False)
        self.reset_subsequent_groupboxes(3)
        
        if self.radioButton_3.isChecked():  # Yes selected
            # Enable next groupbox directly
            self.groupBox_3.setEnabled(True)
        elif self.radioButton_4.isChecked():  # No selected
            # Show entire warning frame with checkbox
            self.frame_2.setVisible(True)
    
    def check_groupbox2_progression(self):
        """Check if GroupBox 2 can progress to next"""
        if self.radioButton_4.isChecked() and self.checkBox_1.isChecked():
            # "No" was selected and checkbox is checked
            self.groupBox_3.setEnabled(True)
    
    def handle_groupbox3_selection(self):
        """Handle GroupBox 3 selection"""
        # Reset state
        self.frame_3.setVisible(False)
        self.checkBox_2.setChecked(False)
        self.groupBox_4.setEnabled(False)
        self.reset_subsequent_groupboxes(4)
        
        if self.radioButton_5.isChecked():  # Yes selected
            # Enable next groupbox directly
            self.groupBox_4.setEnabled(True)
        elif self.radioButton_6.isChecked():  # No selected
            # Show entire warning frame with checkbox
            self.frame_3.setVisible(True)
    
    def check_groupbox3_progression(self):
        """Check if GroupBox 3 can progress to next"""
        if self.radioButton_6.isChecked() and self.checkBox_2.isChecked():
            # "No" was selected and checkbox is checked
            self.groupBox_4.setEnabled(True)
    
    def handle_groupbox4_selection(self):
        """Handle GroupBox 4 selection"""
        # Reset state
        self.frame_5.setVisible(False)
        self.checkBox_3.setChecked(False)
        self.groupBox_5.setEnabled(False)
        self.reset_subsequent_groupboxes(5)
        
        if self.radioButton_7.isChecked():  # Yes selected
            # Enable next groupbox directly
            self.groupBox_5.setEnabled(True)
        elif self.radioButton_8.isChecked():  # No selected
            # Show entire warning frame with checkbox
            self.frame_5.setVisible(True)
    
    def check_groupbox4_progression(self):
        """Check if GroupBox 4 can progress to next"""
        if self.radioButton_8.isChecked() and self.checkBox_3.isChecked():
            # "No" was selected and checkbox is checked
            self.groupBox_5.setEnabled(True)
    
    def handle_groupbox5_selection(self):
        """Handle GroupBox 5 selection - final groupbox"""
        # Reset state
        self.frame_7.setVisible(False)
        self.checkBox_4.setChecked(False)
        self.check_form_completion()
        
        if self.radioButton_9.isChecked():  # Yes selected
            # Final groupbox, form can be completed
            self.check_form_completion()
        elif self.radioButton_10.isChecked():  # No selected
            # Show entire warning frame with checkbox
            self.frame_7.setVisible(True)
    
    def check_groupbox5_progression(self):
        """Check if GroupBox 5 progression is complete"""
        self.check_form_completion()
    
    def reset_subsequent_groupboxes(self, from_groupbox):
        """Reset all groupboxes and their states from the specified groupbox onwards"""
        if from_groupbox <= 3:
            self.groupBox_3.setEnabled(False)
            self.radioButton_5.setChecked(False)
            self.radioButton_6.setChecked(False)
            self.frame_3.setVisible(False)
            self.checkBox_2.setChecked(False)
        
        if from_groupbox <= 4:
            self.groupBox_4.setEnabled(False)
            self.radioButton_7.setChecked(False)
            self.radioButton_8.setChecked(False)
            self.frame_5.setVisible(False)
            self.checkBox_3.setChecked(False)
        
        if from_groupbox <= 5:
            self.groupBox_5.setEnabled(False)
            self.radioButton_9.setChecked(False)
            self.radioButton_10.setChecked(False)
            self.frame_7.setVisible(False)
            self.checkBox_4.setChecked(False)
        
        # Always disable button when resetting
        self.pushButton.setEnabled(False)
    
    def check_form_completion(self):
        """Check if the entire form is complete and enable/disable the push button accordingly"""
        # Form is complete when GroupBox 5 has a selection
        if self.radioButton_9.isChecked():
            # "Yes" selected - form complete
            self.pushButton.setEnabled(True)
        elif self.radioButton_10.isChecked() and self.checkBox_4.isChecked():
            # "No" selected and acknowledgment checkbox checked - form complete
            self.pushButton.setEnabled(True)
        else:
            # Form not complete
            self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
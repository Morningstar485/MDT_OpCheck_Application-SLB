from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
 
from utils import resource_path

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1337, 700)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_1 = QCheckBox(self.frame_4)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout_10.addWidget(self.checkBox_1)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_1 = QLabel(self.frame_8)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_2.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.frame_8)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(80, 25))
        self.lineEdit_1.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_1)


        self.horizontalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(80, 25))
        self.lineEdit_2.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.horizontalLayout_9.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_4 = QLineEdit(self.frame_10)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(80, 25))
        self.lineEdit_4.setMaximumSize(QSize(80, 25))

        self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(80, 25))
        self.lineEdit_3.setMaximumSize(QSize(80, 25))

        self.gridLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)

        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.frame)
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


        self.verticalLayout.addWidget(self.frame)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_5 = QLineEdit(self.frame_11)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(80, 25))
        self.lineEdit_5.setMaximumSize(QSize(80, 25))

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 3, 1, 1)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_11)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(80, 25))
        self.lineEdit_8.setMaximumSize(QSize(80, 25))

        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 3, 1, 1)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_11)

        self.frame_20 = QFrame(self.frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(41, 41))
        self.label_14.setMaximumSize(QSize(41, 41))
        self.label_14.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_19.addWidget(self.label_15)


        self.horizontalLayout_8.addWidget(self.frame_20)


        self.verticalLayout.addWidget(self.frame_13)

        self.checkBox_3 = QCheckBox(self.frame_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.groupBox_1 = QGroupBox(self.frame_5)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(215, 0))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.radioButton_1 = QRadioButton(self.groupBox_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.groupBox_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.radioButton_2)


        self.horizontalLayout_12.addWidget(self.groupBox_1)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)


        self.horizontalLayout_12.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(215, 0))
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_4)


        self.horizontalLayout_13.addWidget(self.groupBox_2)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(41, 41))
        self.label_18.setMaximumSize(QSize(41, 41))
        self.label_18.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)


        self.horizontalLayout_13.addWidget(self.frame_15)


        self.verticalLayout.addWidget(self.frame_6)

        self.checkBox_4 = QCheckBox(self.frame_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_16.addWidget(self.label_5)

        self.lineEdit_6 = QLineEdit(self.frame_16)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(80, 25))
        self.lineEdit_6.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_16.addWidget(self.lineEdit_6)


        self.horizontalLayout_15.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_17.addWidget(self.label_6)

        self.lineEdit_7 = QLineEdit(self.frame_17)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(80, 25))
        self.lineEdit_7.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_17.addWidget(self.lineEdit_7)


        self.horizontalLayout_15.addWidget(self.frame_17)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(41, 41))
        self.label_20.setMaximumSize(QSize(41, 41))
        self.label_20.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_18.addWidget(self.label_21)


        self.verticalLayout.addWidget(self.frame_18)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.frame_21 = QFrame(self.groupBox)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_3 = QGroupBox(self.frame_21)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(210, 0))
        self.groupBox_3.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_5 = QRadioButton(self.groupBox_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_6)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.label_24 = QLabel(self.frame_22)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(41, 41))
        self.label_24.setMaximumSize(QSize(41, 41))
        self.label_24.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_22)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_20.addWidget(self.label_25)


        self.horizontalLayout_4.addWidget(self.frame_22)


        self.verticalLayout_3.addWidget(self.frame_21)

        self.frame_19 = QFrame(self.groupBox)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_19)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_2 = QCheckBox(self.frame_19)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_5 = QCheckBox(self.frame_19)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_5)


        self.verticalLayout_3.addWidget(self.frame_19)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_3.addWidget(self.label_28)

        self.frame_24 = QFrame(self.groupBox)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_4 = QGroupBox(self.frame_24)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(210, 0))
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_7 = QRadioButton(self.groupBox_4)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.groupBox_4)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_8)


        self.horizontalLayout_5.addWidget(self.groupBox_4)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_22.setSpacing(15)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.label_29 = QLabel(self.frame_25)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(41, 41))
        self.label_29.setMaximumSize(QSize(41, 41))
        self.label_29.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_29.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_25)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_22.addWidget(self.label_30)


        self.horizontalLayout_5.addWidget(self.frame_25)


        self.verticalLayout_3.addWidget(self.frame_24)

        self.frame_27 = QFrame(self.groupBox)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_27)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_6 = QCheckBox(self.frame_27)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.frame_27)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_7)


        self.verticalLayout_3.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.groupBox)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_31 = QLabel(self.frame_26)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_6.addWidget(self.label_31)

        self.lineEdit_12 = QLineEdit(self.frame_26)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(125, 25))
        self.lineEdit_12.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_6.addWidget(self.lineEdit_12)

        self.label_32 = QLabel(self.frame_26)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_6.addWidget(self.label_32)

        self.lineEdit_11 = QLineEdit(self.frame_26)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(125, 25))
        self.lineEdit_11.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_6.addWidget(self.lineEdit_11)


        self.verticalLayout_3.addWidget(self.frame_26)

        self.frame_23 = QFrame(self.groupBox)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_21.setSpacing(15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.label_26 = QLabel(self.frame_23)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(41, 41))
        self.label_26.setMaximumSize(QSize(41, 41))
        self.label_26.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_26.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_23)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_21.addWidget(self.label_27)


        self.verticalLayout_3.addWidget(self.frame_23)


        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        # Initially disable all controls except checkBox_1
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.radioButton_1.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)
        self.radioButton_5.setEnabled(False)
        self.radioButton_6.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.radioButton_7.setEnabled(False)
        self.radioButton_8.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.checkBox_7.setEnabled(False)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_11.setEnabled(False)
        self.pushButton.setEnabled(False)

        # Hide error frames initially
        self.frame_12.hide()
        self.frame_20.hide()
        self.frame_14.hide()
        self.frame_15.hide()
        self.frame_18.hide()
        self.frame_22.hide()
        self.frame_25.hide()
        self.frame_23.hide()

        # Sequential flow logic
        def reset_from_frame8():
            """Reset all controls from frame8 onwards"""
            self.lineEdit_1.clear()
            self.lineEdit_2.clear()
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            reset_from_frame10()

        def reset_from_frame10():
            """Reset all controls from frame10 onwards"""
            self.lineEdit_4.clear()
            self.lineEdit_3.clear()
            self.lineEdit_5.setEnabled(False)
            self.lineEdit_8.setEnabled(False)
            reset_from_frame11()

        def reset_from_frame11():
            """Reset all controls from frame11 onwards"""
            self.lineEdit_5.clear()
            self.lineEdit_8.clear()
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            reset_from_groupbox1()

        def reset_from_groupbox1():
            """Reset all controls from groupBox_1 onwards"""
            self.radioButton_1.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            self.radioButton_1.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            reset_from_frame7()

        def reset_from_frame7():
            """Reset all controls from frame7 onwards"""
            self.lineEdit_6.setEnabled(False)
            self.lineEdit_7.setEnabled(False)
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            reset_from_groupbox2()

        def reset_from_groupbox2():
            """Reset all controls from groupBox_2 onwards"""
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            reset_from_groupbox3()

        def reset_from_groupbox3():
            """Reset all controls from groupBox_3 onwards"""
            self.radioButton_5.setEnabled(False)
            self.radioButton_6.setEnabled(False)
            self.radioButton_5.setChecked(False)
            self.radioButton_6.setChecked(False)
            self.checkBox_2.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_5.setChecked(False)
            reset_from_groupbox4()

        def reset_from_groupbox4():
            """Reset all controls from groupBox_4 onwards"""
            self.radioButton_7.setEnabled(False)
            self.radioButton_8.setEnabled(False)
            self.radioButton_7.setChecked(False)
            self.radioButton_8.setChecked(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox_7.setEnabled(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.lineEdit_12.setEnabled(False)
            self.lineEdit_11.setEnabled(False)
            self.lineEdit_12.clear()
            self.lineEdit_11.clear()
            self.pushButton.setEnabled(False)

        # 1. CB1 enables frame8 line edits
        def check_checkBox_1():
            if self.checkBox_1.isChecked():
                self.lineEdit_1.setEnabled(True)
                self.lineEdit_2.setEnabled(True)
            else:
                reset_from_frame8()

        self.checkBox_1.toggled.connect(check_checkBox_1)

        # 2. Frame8 line edits (filled) enable frame10 line edits
        def check_frame8_filled():
            if self.lineEdit_1.text().strip() and self.lineEdit_2.text().strip():
                self.lineEdit_4.setEnabled(True)
                self.lineEdit_3.setEnabled(True)
            else:
                reset_from_frame10()

        self.lineEdit_1.textChanged.connect(check_frame8_filled)
        self.lineEdit_2.textChanged.connect(check_frame8_filled)

        # 3. Frame10 line edits (filled) + no frame12 visible enable frame11 line edits
        def check_frame10_and_frame12():
            if (self.lineEdit_4.text().strip() and self.lineEdit_3.text().strip() and 
                not self.frame_12.isVisible()):
                self.lineEdit_5.setEnabled(True)
                self.lineEdit_8.setEnabled(True)
            else:
                reset_from_frame11()

        self.lineEdit_4.textChanged.connect(check_frame10_and_frame12)
        self.lineEdit_3.textChanged.connect(check_frame10_and_frame12)

        # 4. Frame11 line edits (filled) + no frame20 visible enable checkBox_3
        def check_frame11_and_frame20():
            if (self.lineEdit_5.text().strip() and self.lineEdit_8.text().strip() and 
                not self.frame_20.isVisible()):
                self.checkBox_3.setEnabled(True)
            else:
                reset_from_groupbox1()

        self.lineEdit_5.textChanged.connect(check_frame11_and_frame20)
        self.lineEdit_8.textChanged.connect(check_frame11_and_frame20)

        # 5. checkBox_3 checked enables groupBox_1
        def check_checkBox_3():
            if self.checkBox_3.isChecked():
                self.radioButton_1.setEnabled(True)
                self.radioButton_2.setEnabled(True)
            else:
                reset_from_groupbox1()

        self.checkBox_3.toggled.connect(check_checkBox_3)

        # 6. GroupBox_1 selection enables checkBox_4 or groupBox_2
        def check_groupBox_1_for_flow():
            if self.radioButton_1.isChecked():  # Yes
                self.checkBox_4.setEnabled(True)
                # Disable groupBox_2 when Yes is selected
                self.radioButton_3.setEnabled(False)
                self.radioButton_4.setEnabled(False)
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setChecked(False)
                reset_from_groupbox2()
            elif self.radioButton_2.isChecked():  # No
                self.checkBox_4.setEnabled(False)
                self.checkBox_4.setChecked(False)
                reset_from_frame7()
                # Enable groupBox_2 when No is selected
                self.radioButton_3.setEnabled(True)
                self.radioButton_4.setEnabled(True)
            else:
                self.checkBox_4.setEnabled(False)
                self.checkBox_4.setChecked(False)
                self.radioButton_3.setEnabled(False)
                self.radioButton_4.setEnabled(False)
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setChecked(False)
                reset_from_frame7()

        self.radioButton_1.toggled.connect(check_groupBox_1_for_flow)
        self.radioButton_2.toggled.connect(check_groupBox_1_for_flow)

        # 7. checkBox_4 checked enables frame7 line edits
        def check_checkBox_4():
            if self.checkBox_4.isChecked():
                self.lineEdit_6.setEnabled(True)
                self.lineEdit_7.setEnabled(True)
            else:
                reset_from_frame7()

        self.checkBox_4.toggled.connect(check_checkBox_4)

        # 8. Frame7 line edits (filled) + no frame18 visible enable groupBox_3 (both paths)
        def check_frame7_and_frame18():
            if (self.lineEdit_6.text().strip() and self.lineEdit_7.text().strip() and 
                not self.frame_18.isVisible()):
                # Enable groupBox_3 from both paths: GB1 Yes -> CB4 -> frame7 AND GB1 No -> GB2 -> CB4 -> frame7
                self.radioButton_5.setEnabled(True)
                self.radioButton_6.setEnabled(True)
            else:
                reset_from_groupbox3()

        self.lineEdit_6.textChanged.connect(check_frame7_and_frame18)
        self.lineEdit_7.textChanged.connect(check_frame7_and_frame18)

        # 9. GroupBox_2 selection enables checkBox_4 (from GB1 No path)
        def check_groupBox_2_for_flow():
            if self.radioButton_3.isChecked() or self.radioButton_4.isChecked():  # Yes or No
                # Enable checkBox_4 to continue to Frame7
                self.checkBox_4.setEnabled(True)
            else:
                self.checkBox_4.setEnabled(False)
                self.checkBox_4.setChecked(False)
                reset_from_frame7()

        self.radioButton_3.toggled.connect(check_groupBox_2_for_flow)
        self.radioButton_4.toggled.connect(check_groupBox_2_for_flow)

        # 10. GroupBox_3 "Yes" selected enables checkboxes below it (sequential flow)
        def check_groupBox_3_for_flow():
            if self.radioButton_5.isChecked():  # Yes
                self.checkBox_2.setEnabled(True)
                self.checkBox_5.setEnabled(True)
                # Do NOT auto-enable groupBox_4 - wait for checkboxes
            else:
                self.checkBox_2.setEnabled(False)
                self.checkBox_5.setEnabled(False)
                self.checkBox_2.setChecked(False)
                self.checkBox_5.setChecked(False)
                reset_from_groupbox4()

        self.radioButton_5.toggled.connect(check_groupBox_3_for_flow)
        self.radioButton_6.toggled.connect(check_groupBox_3_for_flow)

        # 11. Both checkboxes checked enables groupBox_4 (sequential flow)
        def check_both_checkboxes():
            if self.checkBox_2.isChecked() and self.checkBox_5.isChecked():
                self.radioButton_7.setEnabled(True)
                self.radioButton_8.setEnabled(True)
            else:
                reset_from_groupbox4()

        self.checkBox_2.toggled.connect(check_both_checkboxes)
        self.checkBox_5.toggled.connect(check_both_checkboxes)

        # 12. GroupBox_4 "Yes" selected enables checkboxes below it (sequential flow)
        def check_groupBox_4_for_flow():
            if self.radioButton_7.isChecked():  # Yes
                self.checkBox_6.setEnabled(True)
                self.checkBox_7.setEnabled(True)
                # Do NOT auto-enable line edits - wait for checkboxes
            else:
                self.checkBox_6.setEnabled(False)
                self.checkBox_7.setEnabled(False)
                self.checkBox_6.setChecked(False)
                self.checkBox_7.setChecked(False)
                self.lineEdit_12.setEnabled(False)
                self.lineEdit_11.setEnabled(False)
                self.lineEdit_12.clear()
                self.lineEdit_11.clear()
                self.pushButton.setEnabled(False)

        self.radioButton_7.toggled.connect(check_groupBox_4_for_flow)
        self.radioButton_8.toggled.connect(check_groupBox_4_for_flow)

        # 13. Both checkboxes in groupBox_4 checked enables final line edits (sequential flow)
        def check_final_checkboxes():
            if self.checkBox_6.isChecked() and self.checkBox_7.isChecked():
                self.lineEdit_12.setEnabled(True)
                self.lineEdit_11.setEnabled(True)
            else:
                self.lineEdit_12.setEnabled(False)
                self.lineEdit_11.setEnabled(False)
                self.lineEdit_12.clear()
                self.lineEdit_11.clear()
                self.pushButton.setEnabled(False)

        self.checkBox_6.toggled.connect(check_final_checkboxes)
        self.checkBox_7.toggled.connect(check_final_checkboxes)


        def check_final_edits_and_frame23():
            if (self.lineEdit_12.text().strip() and self.lineEdit_11.text().strip()):
                try:
                    val_12 = float(self.lineEdit_12.text())
                    val_11 = float(self.lineEdit_11.text())
                    # Enable pushButton if both values > 3100 AND frame23 is not visible
                    if val_12 >= 3100 and val_11 >= 3100:
                        self.pushButton.setEnabled(True)
                    else:
                        self.pushButton.setEnabled(False)
                except ValueError:
                    self.pushButton.setEnabled(False)
            else:
                self.pushButton.setEnabled(False)

        self.lineEdit_12.textChanged.connect(check_final_edits_and_frame23)
        self.lineEdit_11.textChanged.connect(check_final_edits_and_frame23)

        # GroupBox 1 - Show frame_14 if "No" is selected
        def check_groupBox_1():
            if self.radioButton_2.isChecked():  # No
                self.frame_14.show()
            else:
                self.frame_14.hide()
        
        self.radioButton_1.toggled.connect(check_groupBox_1)
        self.radioButton_2.toggled.connect(check_groupBox_1)

        # GroupBox 2 - Show frame_15 if "No" is selected
        def check_groupBox_2():
            if self.radioButton_4.isChecked():  # No
                self.frame_15.show()
                self.checkBox_4.setEnabled(False) # Disable checkBox_4 when frame_15 is shown
            else:
                self.frame_15.hide()
        
        self.radioButton_3.toggled.connect(check_groupBox_2)
        self.radioButton_4.toggled.connect(check_groupBox_2)

        # GroupBox 3 - Show frame_22 if "No" is selected
        def check_groupBox_3():
            if self.radioButton_6.isChecked():  # No
                self.frame_22.show()
            else:
                self.frame_22.hide()
        
        self.radioButton_5.toggled.connect(check_groupBox_3)
        self.radioButton_6.toggled.connect(check_groupBox_3)

        # GroupBox 4 - Show frame_25 if "No" is selected
        def check_groupBox_4():
            if self.radioButton_8.isChecked():  # No
                self.frame_25.show()
            else:
                self.frame_25.hide()
        
        self.radioButton_7.toggled.connect(check_groupBox_4)
        self.radioButton_8.toggled.connect(check_groupBox_4)

        # Frame 12 validation - Show if lineEdit_4 > 42.1 OR lineEdit_3 outside 50-95
        def check_frame_12():
            try:
                val_4 = float(self.lineEdit_4.text()) if self.lineEdit_4.text() else 0
                val_3 = float(self.lineEdit_3.text()) if self.lineEdit_3.text() else 0
                
                show_frame = val_4 > 42.1 or not (50 <= val_3 <= 95)
                self.frame_12.setVisible(show_frame)
                # Re-check frame10 flow logic when frame12 visibility changes
                check_frame10_and_frame12()
            except ValueError:
                self.frame_12.hide()
                check_frame10_and_frame12()
        
        self.lineEdit_4.textChanged.connect(check_frame_12)
        self.lineEdit_3.textChanged.connect(check_frame_12)

        # Frame 20 validation - Show if lineEdit_5 > 42.1 OR lineEdit_8 outside 50-95
        def check_frame_20():
            try:
                val_5 = float(self.lineEdit_5.text()) if self.lineEdit_5.text() else 0
                val_8 = float(self.lineEdit_8.text()) if self.lineEdit_8.text() else 0
                
                show_frame = val_5 > 42.1 or not (50 <= val_8 <= 95)
                self.frame_20.setVisible(show_frame)
                # Re-check frame11 flow logic when frame20 visibility changes
                check_frame11_and_frame20()
            except ValueError:
                self.frame_20.hide()
                check_frame11_and_frame20()
        
        self.lineEdit_5.textChanged.connect(check_frame_20)
        self.lineEdit_8.textChanged.connect(check_frame_20)

        # Frame 18 validation - Show if lineEdit_6 < 3100 OR lineEdit_7 < 3100
        def check_frame_18():
            try:
                val_6 = float(self.lineEdit_6.text()) if self.lineEdit_6.text() else 0
                val_7 = float(self.lineEdit_7.text()) if self.lineEdit_7.text() else 0
                
                show_frame = val_6 < 3100 or val_7 < 3100
                self.frame_18.setVisible(show_frame)
                self.adjustSize()  # Adjust dialog size to fit new frame visibility
                # Re-check frame7 flow logic when frame18 visibility changes
                check_frame7_and_frame18()
            except ValueError:
                self.frame_18.hide()
                check_frame7_and_frame18()
        
        self.lineEdit_6.textChanged.connect(check_frame_18)
        self.lineEdit_7.textChanged.connect(check_frame_18)

        # Frame 23 validation - Show if lineEdit_12 < 3100 OR lineEdit_11 < 3100
        def check_frame_23():
            try:
                val_12 = float(self.lineEdit_12.text()) if self.lineEdit_12.text() else 0
                val_11 = float(self.lineEdit_11.text()) if self.lineEdit_11.text() else 0
                
                show_frame = val_12 < 3100 or val_11 < 3100
                self.frame_23.setVisible(show_frame)
                # Re-check final edits flow logic when frame23 visibility changes
                check_final_edits_and_frame23()
            except ValueError:
                self.frame_23.hide()
                check_final_edits_and_frame23()
        
        self.lineEdit_12.textChanged.connect(check_frame_23)
        self.lineEdit_11.textChanged.connect(check_frame_23)

        self.pushButton.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Close ADV with 10 ft..lb TORQUE ONLY", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Initial Set Line Pressure</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Initial Hydraulic Pressure</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">SG Temperature</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">SG Pressure</span></p></body></html>", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Check Calibration File</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">CQG Temperature</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">CQG Pressure</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Check Calibration File</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Set the Probe", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Set Probe: Solenoid Status Changing", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Try Changing Solenoid</span></p><p><span style=\" font-size:16pt; font-style:italic;\">Energize and Denergize Manually</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Is the updated Status as Charging?", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Power Recycle</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Set the Proble Again", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraulic Pressure</span></p></body></html>", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Pressure must be above 3100 Psi. Please Investigate</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Performing the Pretests", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Pretest 1</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Is the Volumetric 10cc @60cc/min", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Check solenoid dithering before pretest and </span></p><p><span style=\" font-size:14pt; font-style:italic;\">hydraulic motor running and any physical leaks</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"PTVOL is 10 \u00b1 0.5 cc", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"MRHY PMPVOL reads between 65 and 80 cc", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Pretest 2</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Is the Volumetric 15 cc @ 30 cc/min", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_8.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Check solenoid dithering before pretest and </span></p><p><span style=\" font-size:14pt; font-style:italic;\">hydraulic motor running and any physical leaks</span></p></body></html>", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"PTVOL is 10 \u00b1 0.5 cc", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"MRHY PMPVOL reads between 65 and 80 cc", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraulic Pressure</span></p></body></html>", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">The pressure should be more than 3100 Psi</span></p><p><span style=\" font-size:16pt; font-style:italic;\">Please investigate</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
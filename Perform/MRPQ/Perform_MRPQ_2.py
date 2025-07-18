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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1106, 500)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.groupBox)
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

        self.checkBox_1 = QCheckBox(self.groupBox)
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

        self.groupBox_1 = QGroupBox(self.groupBox)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(190, 0))
        self.groupBox_1.setMaximumSize(QSize(10000000, 16777215))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
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


        self.verticalLayout.addWidget(self.groupBox_1)

        self.frame_12 = QFrame(self.groupBox)
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


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(80, 25))
        self.lineEdit_3.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.horizontalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(80, 25))
        self.lineEdit_4.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_5.addWidget(self.lineEdit_4)


        self.horizontalLayout_10.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.frame_38 = QFrame(Dialog)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_38)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_5 = QCheckBox(self.frame_38)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.checkBox_5)

        self.frame_24 = QFrame(self.frame_38)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_24)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_20 = QLabel(self.frame_24)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_5.addWidget(self.label_20)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.label_21 = QLabel(self.frame_26)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_22.addWidget(self.label_21)

        self.lineEdit_11 = QLineEdit(self.frame_26)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(80, 25))
        self.lineEdit_11.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_22.addWidget(self.lineEdit_11)


        self.horizontalLayout_21.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.label_24 = QLabel(self.frame_27)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_23.addWidget(self.label_24)

        self.lineEdit_12 = QLineEdit(self.frame_27)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(80, 25))
        self.lineEdit_12.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_23.addWidget(self.lineEdit_12)


        self.horizontalLayout_21.addWidget(self.frame_27)


        self.verticalLayout_5.addWidget(self.frame_25)

        self.frame_28 = QFrame(self.frame_24)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.label_25 = QLabel(self.frame_28)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(41, 41))
        self.label_25.setMaximumSize(QSize(41, 41))
        self.label_25.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_28)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_24.addWidget(self.label_26)


        self.verticalLayout_5.addWidget(self.frame_28)


        self.verticalLayout_8.addWidget(self.frame_24)

        self.checkBox_4 = QCheckBox(self.frame_38)
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

        self.frame_19 = QFrame(self.frame_38)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_19)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_18.addWidget(self.label_14)

        self.lineEdit_9 = QLineEdit(self.frame_21)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(80, 25))
        self.lineEdit_9.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_18.addWidget(self.lineEdit_9)


        self.horizontalLayout_17.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_19.addWidget(self.label_15)

        self.lineEdit_10 = QLineEdit(self.frame_22)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(80, 25))
        self.lineEdit_10.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_19.addWidget(self.lineEdit_10)


        self.horizontalLayout_17.addWidget(self.frame_22)


        self.verticalLayout_6.addWidget(self.frame_20)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.label_22 = QLabel(self.frame_23)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(41, 41))
        self.label_22.setMaximumSize(QSize(41, 41))
        self.label_22.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_22.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_20.addWidget(self.label_23)


        self.verticalLayout_6.addWidget(self.frame_23)


        self.verticalLayout_8.addWidget(self.frame_19)

        self.checkBox_6 = QCheckBox(self.frame_38)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.checkBox_6)

        self.frame_29 = QFrame(self.frame_38)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_29)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.frame_29)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(180, 0))
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


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_25.setSpacing(15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.label_27 = QLabel(self.frame_30)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(41, 41))
        self.label_27.setMaximumSize(QSize(41, 41))
        self.label_27.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_30)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_25.addWidget(self.label_28)


        self.horizontalLayout.addWidget(self.frame_30)


        self.verticalLayout_8.addWidget(self.frame_29)

        self.frame_33 = QFrame(self.frame_38)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.label_32 = QLabel(self.frame_34)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_28.addWidget(self.label_32)

        self.lineEdit_13 = QLineEdit(self.frame_34)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(80, 25))
        self.lineEdit_13.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_28.addWidget(self.lineEdit_13)


        self.horizontalLayout_27.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.label_33 = QLabel(self.frame_35)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_29.addWidget(self.label_33)

        self.lineEdit_14 = QLineEdit(self.frame_35)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(80, 25))
        self.lineEdit_14.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_29.addWidget(self.lineEdit_14)


        self.horizontalLayout_27.addWidget(self.frame_35)


        self.verticalLayout_8.addWidget(self.frame_33)

        self.frame_36 = QFrame(self.frame_38)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_30.setSpacing(15)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.label_34 = QLabel(self.frame_36)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(41, 41))
        self.label_34.setMaximumSize(QSize(41, 41))
        self.label_34.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_34.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_36)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_30.addWidget(self.label_35)


        self.verticalLayout_8.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_38)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_31.setSpacing(15)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 0, -1, 0)
        self.label_36 = QLabel(self.frame_37)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(41, 41))
        self.label_36.setMaximumSize(QSize(41, 41))
        self.label_36.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_37)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_31.addWidget(self.label_37)


        self.verticalLayout_8.addWidget(self.frame_37)

        self.frame_31 = QFrame(self.frame_38)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_31)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.label_29 = QLabel(self.frame_32)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(31, 31))
        self.label_29.setMaximumSize(QSize(31, 31))
        self.label_29.setPixmap(QPixmap(resource_path("Icons/Info.png")))
        self.label_29.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_32)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_26.addWidget(self.label_30)


        self.verticalLayout_7.addWidget(self.frame_32)

        self.label_31 = QLabel(self.frame_31)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_7.addWidget(self.label_31)


        self.verticalLayout_8.addWidget(self.frame_31)


        self.gridLayout.addWidget(self.frame_38, 0, 1, 2, 1)

        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.checkBox_2 = QCheckBox(self.frame_7)
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

        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.lineEdit_7 = QLineEdit(self.frame_16)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(80, 25))
        self.lineEdit_7.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_14.addWidget(self.lineEdit_7)


        self.horizontalLayout_13.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.frame_17)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(80, 25))
        self.lineEdit_8.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_15.addWidget(self.lineEdit_8)


        self.horizontalLayout_13.addWidget(self.frame_17)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_16.addWidget(self.label_17)


        self.verticalLayout_3.addWidget(self.frame_18)


        self.verticalLayout_4.addWidget(self.frame)

        self.checkBox_3 = QCheckBox(self.frame_7)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_3)

        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.frame_13)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(80, 25))
        self.lineEdit_5.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_6.addWidget(self.lineEdit_5)


        self.horizontalLayout_11.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.frame_14)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(80, 25))
        self.lineEdit_6.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_8.addWidget(self.lineEdit_6)


        self.horizontalLayout_11.addWidget(self.frame_14)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(41, 41))
        self.label_18.setMaximumSize(QSize(41, 41))
        self.label_18.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)


        self.verticalLayout_2.addWidget(self.frame_15)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)

        self.frame_32 = QFrame(Dialog)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_2 = QPushButton(self.frame_32)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_26.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_32)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_26.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.frame_32, 2, 0, 1, 2)


        self.retranslateUi(Dialog)

        # Initially disable all controls except the first two line edits
        self.checkBox_1.setEnabled(False)
        self.radioButton_1.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_12.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_10.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_14.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.pushButton.setEnabled(False)

        # Hide error frames initially
        self.frame_12.hide()
        self.frame_18.hide()
        self.frame_15.hide()
        self.frame_28.hide()
        self.frame_23.hide()
        self.frame_30.hide()
        self.frame_36.hide()
        self.frame_37.hide()

        QMetaObject.connectSlotsByName(Dialog)
        
        # Connect signals for sequential validation
        self.lineEdit_1.textChanged.connect(self.check_initial_line_edits)
        self.lineEdit_2.textChanged.connect(self.check_initial_line_edits)
        self.checkBox_1.stateChanged.connect(self.check_checkbox_1_for_groupbox)
        self.radioButton_1.toggled.connect(self.check_groupbox_1_selection)
        self.radioButton_2.toggled.connect(self.check_groupbox_1_selection)
        self.lineEdit_3.textChanged.connect(self.check_line_edits_3_4)
        self.lineEdit_4.textChanged.connect(self.check_line_edits_3_4)
        self.checkBox_2.stateChanged.connect(self.check_checkbox_2_for_line_edits)
        self.lineEdit_7.textChanged.connect(self.check_line_edits_7_8)
        self.lineEdit_8.textChanged.connect(self.check_line_edits_7_8)
        self.checkBox_3.stateChanged.connect(self.check_checkbox_3_for_line_edits)
        self.lineEdit_5.textChanged.connect(self.check_line_edits_5_6)
        self.lineEdit_6.textChanged.connect(self.check_line_edits_5_6)
        # Frame_38 workflow connections
        self.checkBox_5.stateChanged.connect(self.check_checkbox_5_for_line_edits_frame38)
        self.lineEdit_11.textChanged.connect(self.check_line_edits_11_12_frame38)
        self.lineEdit_12.textChanged.connect(self.check_line_edits_11_12_frame38)
        self.checkBox_4.stateChanged.connect(self.check_checkbox_4_for_line_edits)
        self.lineEdit_9.textChanged.connect(self.check_line_edits_9_10)
        self.lineEdit_10.textChanged.connect(self.check_line_edits_9_10)
        self.checkBox_6.stateChanged.connect(self.check_checkbox_6_for_groupbox2)
        self.radioButton_3.toggled.connect(self.check_groupbox_2_selection)
        self.radioButton_4.toggled.connect(self.check_groupbox_2_selection)
        self.lineEdit_13.textChanged.connect(self.check_line_edits_13_14)
        self.lineEdit_14.textChanged.connect(self.check_line_edits_13_14)
        self.checkBox_6.stateChanged.connect(self.check_checkbox_6_for_groupbox2)
        self.radioButton_3.toggled.connect(self.check_groupbox_2_selection)
        self.radioButton_4.toggled.connect(self.check_groupbox_2_selection)
        self.lineEdit_13.textChanged.connect(self.check_line_edits_13_14)
        self.lineEdit_14.textChanged.connect(self.check_line_edits_13_14)

        self.pushButton.hide()
        self.pushButton_2.hide()
    # setupUi

    def check_initial_line_edits(self):
        """Check if initial resistivity and temperature have numerical values"""
        try:
            val1 = float(self.lineEdit_1.text()) if self.lineEdit_1.text().strip() else None
            val2 = float(self.lineEdit_2.text()) if self.lineEdit_2.text().strip() else None
            
            if val1 is not None and val2 is not None:
                self.checkBox_1.setEnabled(True)
            else:
                self.checkBox_1.setEnabled(False)
                self.checkBox_1.setChecked(False)
        except ValueError:
            self.checkBox_1.setEnabled(False)
            self.checkBox_1.setChecked(False)

    def check_checkbox_1_for_groupbox(self):
        """Enable groupBox_1 when checkBox_1 is checked"""
        if self.checkBox_1.isChecked():
            self.radioButton_1.setEnabled(True)
            self.radioButton_2.setEnabled(True)
        else:
            self.radioButton_1.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            self.radioButton_1.setChecked(False)
            self.radioButton_2.setChecked(False)
            # Reset subsequent controls
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.frame_12.hide()
            # Reset frame_7 controls
            self.checkBox_2.setEnabled(False)
            self.checkBox_2.setChecked(False)

    def check_groupbox_1_selection(self):
        """Handle Yes/No selection in groupBox_1"""
        if self.radioButton_2.isChecked():  # Yes selected
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.frame_12.hide()
        elif self.radioButton_1.isChecked():  # No selected
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.frame_12.show()
            # Reset subsequent controls in frame_7
            self.checkBox_2.setEnabled(False)
            self.checkBox_2.setChecked(False)

    def check_line_edits_3_4(self):
        """Check if line edits 3 and 4 have numerical values to enable checkBox_2 in frame_7"""
        try:
            val3 = float(self.lineEdit_3.text()) if self.lineEdit_3.text().strip() else None
            val4 = float(self.lineEdit_4.text()) if self.lineEdit_4.text().strip() else None
            
            if val3 is not None and val4 is not None:
                self.checkBox_2.setEnabled(True)
            else:
                self.checkBox_2.setEnabled(False)
                self.checkBox_2.setChecked(False)
        except ValueError:
            self.checkBox_2.setEnabled(False)
            self.checkBox_2.setChecked(False)

    def check_checkbox_2_for_line_edits(self):
        """Enable line edits 7 and 8 when checkBox_2 is checked"""
        if self.checkBox_2.isChecked():
            self.lineEdit_7.setEnabled(True)
            self.lineEdit_8.setEnabled(True)
        else:
            self.lineEdit_7.setEnabled(False)
            self.lineEdit_8.setEnabled(False)
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.frame_18.hide()
            # Reset subsequent controls in frame_7
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            # Reset frame_38 controls
            self.checkBox_5.setEnabled(False)
            self.checkBox_5.setChecked(False)

    def check_line_edits_7_8(self):
        """Check if line edits 7 and 8 have values >= 3100 to show next checkbox or error frame"""
        try:
            val7 = float(self.lineEdit_7.text()) if self.lineEdit_7.text().strip() else None
            val8 = float(self.lineEdit_8.text()) if self.lineEdit_8.text().strip() else None
            
            if val7 is not None and val8 is not None:
                if val7 >= 3100 and val8 >= 3100:
                    self.checkBox_3.setEnabled(True)
                    self.frame_18.hide()
                else:
                    self.checkBox_3.setEnabled(False)
                    self.checkBox_3.setChecked(False)
                    self.frame_18.show()
            else:
                self.checkBox_3.setEnabled(False)
                self.checkBox_3.setChecked(False)
                self.frame_18.hide()
        except ValueError:
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.frame_18.hide()

    def check_checkbox_3_for_line_edits(self):
        """Enable line edits 5 and 6 when checkBox_3 is checked"""
        if self.checkBox_3.isChecked():
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
        else:
            self.lineEdit_5.setEnabled(False)
            self.lineEdit_6.setEnabled(False)
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.frame_15.hide()
            # Reset all frame_38 controls
            self.checkBox_5.setEnabled(False)
            self.checkBox_5.setChecked(False)
            self.lineEdit_11.setEnabled(False)
            self.lineEdit_12.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.lineEdit_9.setEnabled(False)
            self.lineEdit_10.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox_6.setChecked(False)
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            self.lineEdit_13.setEnabled(False)
            self.lineEdit_14.setEnabled(False)
            self.pushButton.setEnabled(False)

    def check_line_edits_5_6(self):
        """Check if line edits 5 and 6 have values >= 3100 to show checkBox_5 or error frame"""
        try:
            val5 = float(self.lineEdit_5.text()) if self.lineEdit_5.text().strip() else None
            val6 = float(self.lineEdit_6.text()) if self.lineEdit_6.text().strip() else None
            
            if val5 is not None and val6 is not None:
                if val5 >= 3100 and val6 >= 3100:
                    self.checkBox_5.setEnabled(True)
                    self.frame_15.hide()
                else:
                    self.checkBox_5.setEnabled(False)
                    self.checkBox_5.setChecked(False)
                    self.frame_15.show()
            else:
                self.checkBox_5.setEnabled(False)
                self.checkBox_5.setChecked(False)
                self.frame_15.hide()
        except ValueError:
            self.checkBox_5.setEnabled(False)
            self.checkBox_5.setChecked(False)
            self.frame_15.hide()

    def check_checkbox_5_for_line_edits_frame38(self):
        """Enable line edits 11 and 12 when checkBox_5 is checked"""
        if self.checkBox_5.isChecked():
            self.lineEdit_11.setEnabled(True)
            self.lineEdit_12.setEnabled(True)
        else:
            self.lineEdit_11.setEnabled(False)
            self.lineEdit_12.setEnabled(False)
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
            self.frame_28.hide()
            # Reset all subsequent controls
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.lineEdit_9.setEnabled(False)
            self.lineEdit_10.setEnabled(False)
            self.checkBox_6.setEnabled(False)
            self.checkBox_6.setChecked(False)
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            self.lineEdit_13.setEnabled(False)
            self.lineEdit_14.setEnabled(False)
            self.pushButton.setEnabled(False)

    def check_line_edits_11_12_frame38(self):
        """Check if line edits 11 and 12 have values >= 3100 to show checkBox_4 or error frame"""
        try:
            val11 = float(self.lineEdit_11.text()) if self.lineEdit_11.text().strip() else None
            val12 = float(self.lineEdit_12.text()) if self.lineEdit_12.text().strip() else None
            
            if val11 is not None and val12 is not None:
                if val11 >= 3100 and val12 >= 3100:
                    self.checkBox_4.setEnabled(True)
                    self.frame_28.hide()
                else:
                    self.checkBox_4.setEnabled(False)
                    self.checkBox_4.setChecked(False)
                    self.frame_28.show()
            else:
                self.checkBox_4.setEnabled(False)
                self.checkBox_4.setChecked(False)
                self.frame_28.hide()
        except ValueError:
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.frame_28.hide()

    def check_checkbox_4_for_line_edits(self):
        """Enable line edits 9 and 10 when checkBox_4 is checked"""
        if self.checkBox_4.isChecked():
            self.lineEdit_9.setEnabled(True)
            self.lineEdit_10.setEnabled(True)
        else:
            self.lineEdit_9.setEnabled(False)
            self.lineEdit_10.setEnabled(False)
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.frame_23.hide()
            # Reset subsequent controls
            self.checkBox_6.setEnabled(False)
            self.checkBox_6.setChecked(False)
            # Reset groupBox_2 and final controls
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            self.lineEdit_13.setEnabled(False)
            self.lineEdit_14.setEnabled(False)
            self.pushButton.setEnabled(False)

    def check_line_edits_9_10(self):
        """Check if line edits 9 and 10 have values >= 3100 to show checkBox_6 or error frame"""
        try:
            val9 = float(self.lineEdit_9.text()) if self.lineEdit_9.text().strip() else None
            val10 = float(self.lineEdit_10.text()) if self.lineEdit_10.text().strip() else None
            
            if val9 is not None and val10 is not None:
                if val9 >= 3100 and val10 >= 3100:
                    self.checkBox_6.setEnabled(True)
                    self.frame_23.hide()
                else:
                    self.checkBox_6.setEnabled(False)
                    self.checkBox_6.setChecked(False)
                    self.frame_23.show()
            else:
                self.checkBox_6.setEnabled(False)
                self.checkBox_6.setChecked(False)
                self.frame_23.hide()
        except ValueError:
            self.checkBox_6.setEnabled(False)
            self.checkBox_6.setChecked(False)
            self.frame_23.hide()

    def check_checkbox_6_for_groupbox2(self):
        """Enable groupBox_2 when checkBox_6 is checked"""
        if self.checkBox_6.isChecked():
            self.radioButton_3.setEnabled(True)
            self.radioButton_4.setEnabled(True)
        else:
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            # Reset subsequent controls
            self.lineEdit_13.setEnabled(False)
            self.lineEdit_14.setEnabled(False)
            self.frame_30.hide()
            self.frame_36.hide()
            self.frame_37.hide()
            self.pushButton.setEnabled(False)

    def check_groupbox_2_selection(self):
        """Handle Yes/No selection in groupBox_2"""
        if self.radioButton_3.isChecked():  # Yes selected
            self.lineEdit_13.setEnabled(True)
            self.lineEdit_14.setEnabled(True)
            self.frame_30.hide()
        elif self.radioButton_4.isChecked():  # No selected
            self.lineEdit_13.setEnabled(False)
            self.lineEdit_14.setEnabled(False)
            self.lineEdit_13.clear()
            self.lineEdit_14.clear()
            self.frame_30.show()
            # Reset subsequent controls and hide error frames
            self.frame_36.hide()
            self.frame_37.hide()
            self.pushButton.setEnabled(False)

    def check_line_edits_13_14(self):
        """Check if line edits 13 and 14 have values >= 3100 to enable push button or show specific error frames"""
        try:
            val13 = float(self.lineEdit_13.text()) if self.lineEdit_13.text().strip() else None
            val14 = float(self.lineEdit_14.text()) if self.lineEdit_14.text().strip() else None
            
            # Reset all error frames first
            self.frame_36.hide()
            self.frame_37.hide()
            self.pushButton.setEnabled(False)
            
            if val13 is not None and val14 is not None:
                # Check specific conditions for error frames
                if val13 < 3100:
                    self.frame_36.show()
                if val14 < 3100:
                    self.frame_37.show()
                
                # Enable push button only if both values are >= 3100
                if val13 >= 3100 and val14 >= 3100:
                    self.pushButton.setEnabled(True)
            else:
                # If either field is empty, hide error frames but don't enable button
                self.frame_36.hide()
                self.frame_37.hide()
                
        except ValueError:
            # If invalid input, hide error frames and disable button
            self.frame_36.hide()
            self.frame_37.hide()
            self.pushButton.setEnabled(False)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Resistivity Cell Check", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Initial Resistivity</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Initial Temperature</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Pour Warm water with Salt solution in probe", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Resistivity value changes?", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Please flush flowline with air and troubleshoot</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">New Resistivity</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">New Temperature</span></p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Opened BYPASS valves", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Confirm solenoid status</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraulic Pressure</span></p></body></html>", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">The pressure should be more than 3100 Psi</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Closed ISO valves", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Confirm solenoid status</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraulic Pressure</span></p></body></html>", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">The pressure should be more than 3100 Psi</span></p></body></html>", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Put MPMP jig on Probe and connect waterline with shop Air(~100psi)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Both Mini Flowline leak Ok", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Investigate and replace the </span></p><p><span style=\" font-size:16pt; font-style:italic;\">mini flowline socket/joint</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">SG Pressure</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">CQG Pressure</span></p></body></html>", None))
        self.label_34.setText("")
        self.label_35.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Check SFT Bottle Air Pressure and Check Calibration</span></p></body></html>", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Check SFT Bottle Air Pressure</span></p><p><span style=\" font-size:16pt; font-style:italic;\">Check &quot;Snubber&quot; in Snubber Port</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Note</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">For checking Snubber Port, first remove SFT hose </span></p><p><span style=\" font-size:12pt;\">and probe and bleed the pressure from MPMP jig</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Perform MRPQ ISO valves function test for all MRPQs</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Opened ISO (Sample and Guard) valves", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Confirm solenoid status</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraulic Pressure</span></p></body></html>", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">The pressure should be more than 3100 Psi</span></p><p><span style=\" font-size:16pt; font-style:italic;\">Please investigate</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Closed Bypass (Inner and Outer) valves", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Confirm solenoid status</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraulic Pressure</span></p></body></html>", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">The pressure should be more than 3100 Psi</span></p><p><span style=\" font-size:16pt; font-style:italic;\">Please investigate</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Back", None))
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
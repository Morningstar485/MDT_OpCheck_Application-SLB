from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1148, 737)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_30 = QFrame(Dialog)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_30)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_32)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.checkBox_1 = QCheckBox(self.frame_32)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_18.addWidget(self.checkBox_1)


        self.verticalLayout_16.addWidget(self.frame_32)

        self.frame_3 = QFrame(self.frame_30)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(41, 41))
        self.label_4.setMaximumSize(QSize(41, 41))
        self.label_4.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame_6)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_16.addWidget(self.frame_3)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_31)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_2 = QLabel(self.frame_31)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_17.addWidget(self.label_2)


        self.verticalLayout_16.addWidget(self.frame_31)

        self.frame_4 = QFrame(self.frame_30)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(41, 41))
        self.label_7.setMaximumSize(QSize(41, 41))
        self.label_7.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)


        self.verticalLayout_16.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_30)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_1 = QLabel(self.frame_11)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_7.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.frame_11)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(80, 25))
        self.lineEdit_1.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_7.addWidget(self.lineEdit_1)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.frame_11)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(80, 25))
        self.lineEdit_2.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_7.addWidget(self.lineEdit_2)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit_3 = QLineEdit(self.frame_11)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(80, 25))
        self.lineEdit_3.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addWidget(self.frame_11)


        self.verticalLayout_16.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_30)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.verticalLayout_4.addWidget(self.checkBox_3)

        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.lineEdit_4 = QLineEdit(self.frame_12)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(80, 25))
        self.lineEdit_4.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_8.addWidget(self.lineEdit_4)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.lineEdit_5 = QLineEdit(self.frame_12)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(80, 25))
        self.lineEdit_5.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_8.addWidget(self.lineEdit_5)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.lineEdit_6 = QLineEdit(self.frame_12)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(80, 25))
        self.lineEdit_6.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_8.addWidget(self.lineEdit_6)


        self.verticalLayout_4.addWidget(self.frame_12)


        self.verticalLayout_16.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame_30)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_4 = QCheckBox(self.frame_5)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_4)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.lineEdit_7 = QLineEdit(self.frame_13)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(80, 25))
        self.lineEdit_7.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_9.addWidget(self.lineEdit_7)

        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.lineEdit_8 = QLineEdit(self.frame_13)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(80, 25))
        self.lineEdit_8.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_9.addWidget(self.lineEdit_8)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.lineEdit_9 = QLineEdit(self.frame_13)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(80, 25))
        self.lineEdit_9.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_9.addWidget(self.lineEdit_9)


        self.verticalLayout_5.addWidget(self.frame_13)


        self.verticalLayout_16.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.frame_30)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_5 = QCheckBox(self.frame_8)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_5)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.lineEdit_10 = QLineEdit(self.frame_14)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(80, 25))
        self.lineEdit_10.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_10.addWidget(self.lineEdit_10)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.lineEdit_11 = QLineEdit(self.frame_14)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(80, 25))
        self.lineEdit_11.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_10.addWidget(self.lineEdit_11)

        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.lineEdit_12 = QLineEdit(self.frame_14)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(80, 25))
        self.lineEdit_12.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_10.addWidget(self.lineEdit_12)


        self.verticalLayout_6.addWidget(self.frame_14)


        self.verticalLayout_16.addWidget(self.frame_8)

        self.frame_28 = QFrame(self.frame_30)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_28)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.checkBox_13 = QCheckBox(self.frame_28)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setEnabled(True)
        self.checkBox_13.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.checkBox_13)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_40 = QLabel(self.frame_29)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_18.addWidget(self.label_40)

        self.lineEdit_34 = QLineEdit(self.frame_29)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setMinimumSize(QSize(80, 25))
        self.lineEdit_34.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_18.addWidget(self.lineEdit_34)

        self.label_41 = QLabel(self.frame_29)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_18.addWidget(self.label_41)

        self.lineEdit_35 = QLineEdit(self.frame_29)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setMinimumSize(QSize(80, 25))
        self.lineEdit_35.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_18.addWidget(self.lineEdit_35)

        self.label_42 = QLabel(self.frame_29)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_18.addWidget(self.label_42)

        self.lineEdit_36 = QLineEdit(self.frame_29)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setMinimumSize(QSize(80, 25))
        self.lineEdit_36.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_18.addWidget(self.lineEdit_36)


        self.verticalLayout_15.addWidget(self.frame_29)


        self.verticalLayout_16.addWidget(self.frame_28)


        self.horizontalLayout.addWidget(self.frame_30)

        self.frame_27 = QFrame(Dialog)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_27)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_27)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.checkBox_6 = QCheckBox(self.frame_9)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_7.addWidget(self.checkBox_6)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_11.addWidget(self.label_19)

        self.lineEdit_13 = QLineEdit(self.frame_15)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(80, 25))
        self.lineEdit_13.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_11.addWidget(self.lineEdit_13)

        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_11.addWidget(self.label_20)

        self.lineEdit_14 = QLineEdit(self.frame_15)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(80, 25))
        self.lineEdit_14.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_11.addWidget(self.lineEdit_14)

        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_11.addWidget(self.label_21)

        self.lineEdit_15 = QLineEdit(self.frame_15)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(80, 25))
        self.lineEdit_15.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_11.addWidget(self.lineEdit_15)


        self.verticalLayout_7.addWidget(self.frame_15)


        self.verticalLayout_14.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_27)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_7 = QCheckBox(self.frame_10)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.checkBox_7)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_12.addWidget(self.label_22)

        self.lineEdit_16 = QLineEdit(self.frame_16)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(80, 25))
        self.lineEdit_16.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_16)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_12.addWidget(self.label_23)

        self.lineEdit_17 = QLineEdit(self.frame_16)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(80, 25))
        self.lineEdit_17.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_17)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_12.addWidget(self.label_24)

        self.lineEdit_18 = QLineEdit(self.frame_16)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(80, 25))
        self.lineEdit_18.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_18)


        self.verticalLayout_8.addWidget(self.frame_16)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.frame_17 = QFrame(self.frame_27)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_8 = QCheckBox(self.frame_17)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setEnabled(True)
        self.checkBox_8.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_9.addWidget(self.checkBox_8)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_25 = QLabel(self.frame_18)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_13.addWidget(self.label_25)

        self.lineEdit_19 = QLineEdit(self.frame_18)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(80, 25))
        self.lineEdit_19.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_19)

        self.label_26 = QLabel(self.frame_18)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_13.addWidget(self.label_26)

        self.lineEdit_20 = QLineEdit(self.frame_18)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(80, 25))
        self.lineEdit_20.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_20)

        self.label_27 = QLabel(self.frame_18)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_13.addWidget(self.label_27)

        self.lineEdit_21 = QLineEdit(self.frame_18)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(80, 25))
        self.lineEdit_21.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_21)


        self.verticalLayout_9.addWidget(self.frame_18)


        self.verticalLayout_14.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_27)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_19)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_9 = QCheckBox(self.frame_19)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setEnabled(True)
        self.checkBox_9.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_10.addWidget(self.checkBox_9)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_28 = QLabel(self.frame_20)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_14.addWidget(self.label_28)

        self.lineEdit_22 = QLineEdit(self.frame_20)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(80, 25))
        self.lineEdit_22.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_14.addWidget(self.lineEdit_22)

        self.label_29 = QLabel(self.frame_20)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_14.addWidget(self.label_29)

        self.lineEdit_23 = QLineEdit(self.frame_20)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(80, 25))
        self.lineEdit_23.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_14.addWidget(self.lineEdit_23)

        self.label_30 = QLabel(self.frame_20)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_14.addWidget(self.label_30)

        self.lineEdit_24 = QLineEdit(self.frame_20)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(80, 25))
        self.lineEdit_24.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_14.addWidget(self.lineEdit_24)


        self.verticalLayout_10.addWidget(self.frame_20)


        self.verticalLayout_14.addWidget(self.frame_19)

        self.frame_21 = QFrame(self.frame_27)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_21)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.checkBox_10 = QCheckBox(self.frame_21)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setEnabled(True)
        self.checkBox_10.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.checkBox_10)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_31 = QLabel(self.frame_22)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_15.addWidget(self.label_31)

        self.lineEdit_25 = QLineEdit(self.frame_22)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(80, 25))
        self.lineEdit_25.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_15.addWidget(self.lineEdit_25)

        self.label_32 = QLabel(self.frame_22)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_15.addWidget(self.label_32)

        self.lineEdit_26 = QLineEdit(self.frame_22)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(80, 25))
        self.lineEdit_26.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_15.addWidget(self.lineEdit_26)

        self.label_33 = QLabel(self.frame_22)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_15.addWidget(self.label_33)

        self.lineEdit_27 = QLineEdit(self.frame_22)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(80, 25))
        self.lineEdit_27.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_15.addWidget(self.lineEdit_27)


        self.verticalLayout_11.addWidget(self.frame_22)


        self.verticalLayout_14.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_27)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_23)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.checkBox_11 = QCheckBox(self.frame_23)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setEnabled(True)
        self.checkBox_11.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.checkBox_11)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_34 = QLabel(self.frame_24)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_16.addWidget(self.label_34)

        self.lineEdit_28 = QLineEdit(self.frame_24)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setMinimumSize(QSize(80, 25))
        self.lineEdit_28.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_16.addWidget(self.lineEdit_28)

        self.label_35 = QLabel(self.frame_24)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_16.addWidget(self.label_35)

        self.lineEdit_29 = QLineEdit(self.frame_24)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setMinimumSize(QSize(80, 25))
        self.lineEdit_29.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_16.addWidget(self.lineEdit_29)

        self.label_36 = QLabel(self.frame_24)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_16.addWidget(self.label_36)

        self.lineEdit_30 = QLineEdit(self.frame_24)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setMinimumSize(QSize(80, 25))
        self.lineEdit_30.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_16.addWidget(self.lineEdit_30)


        self.verticalLayout_12.addWidget(self.frame_24)


        self.verticalLayout_14.addWidget(self.frame_23)

        self.frame_25 = QFrame(self.frame_27)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_25)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.checkBox_12 = QCheckBox(self.frame_25)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setEnabled(True)
        self.checkBox_12.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.checkBox_12)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_37 = QLabel(self.frame_26)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_17.addWidget(self.label_37)

        self.lineEdit_31 = QLineEdit(self.frame_26)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setMinimumSize(QSize(80, 25))
        self.lineEdit_31.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_17.addWidget(self.lineEdit_31)

        self.label_38 = QLabel(self.frame_26)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_17.addWidget(self.label_38)

        self.lineEdit_32 = QLineEdit(self.frame_26)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setMinimumSize(QSize(80, 25))
        self.lineEdit_32.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_17.addWidget(self.lineEdit_32)

        self.label_39 = QLabel(self.frame_26)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_17.addWidget(self.label_39)

        self.lineEdit_33 = QLineEdit(self.frame_26)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMinimumSize(QSize(80, 25))
        self.lineEdit_33.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_17.addWidget(self.lineEdit_33)


        self.verticalLayout_13.addWidget(self.frame_26)


        self.verticalLayout_14.addWidget(self.frame_25)

        self.pushButton_next = QPushButton(self.frame_27)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.verticalLayout_14.addWidget(self.pushButton_next)


        self.horizontalLayout.addWidget(self.frame_27)


        self.retranslateUi(Dialog)
        
        # Initialize form state
        self.initialize_form()
        
        # Connect signals for sequential validation
        self.checkBox_1.toggled.connect(self.check_checkbox_1)
        self.checkBox_2.toggled.connect(self.check_checkbox_2)
        self.lineEdit_1.textChanged.connect(self.check_checkbox_2_line_edits)
        self.lineEdit_2.textChanged.connect(self.check_checkbox_2_line_edits)
        self.lineEdit_3.textChanged.connect(self.check_checkbox_2_line_edits)
        self.checkBox_3.toggled.connect(self.check_checkbox_3)
        self.lineEdit_4.textChanged.connect(self.check_checkbox_3_line_edits)
        self.lineEdit_5.textChanged.connect(self.check_checkbox_3_line_edits)
        self.lineEdit_6.textChanged.connect(self.check_checkbox_3_line_edits)
        self.checkBox_4.toggled.connect(self.check_checkbox_4)
        self.lineEdit_7.textChanged.connect(self.check_checkbox_4_line_edits)
        self.lineEdit_8.textChanged.connect(self.check_checkbox_4_line_edits)
        self.lineEdit_9.textChanged.connect(self.check_checkbox_4_line_edits)
        self.checkBox_5.toggled.connect(self.check_checkbox_5)
        self.lineEdit_10.textChanged.connect(self.check_checkbox_5_line_edits)
        self.lineEdit_11.textChanged.connect(self.check_checkbox_5_line_edits)
        self.lineEdit_12.textChanged.connect(self.check_checkbox_5_line_edits)
        self.checkBox_13.toggled.connect(self.check_checkbox_13)
        self.lineEdit_34.textChanged.connect(self.check_checkbox_13_line_edits)
        self.lineEdit_35.textChanged.connect(self.check_checkbox_13_line_edits)
        self.lineEdit_36.textChanged.connect(self.check_checkbox_13_line_edits)
        
        # Right column connections
        self.checkBox_6.toggled.connect(self.check_checkbox_6)
        self.lineEdit_13.textChanged.connect(self.check_checkbox_6_line_edits)
        self.lineEdit_14.textChanged.connect(self.check_checkbox_6_line_edits)
        self.lineEdit_15.textChanged.connect(self.check_checkbox_6_line_edits)
        self.checkBox_7.toggled.connect(self.check_checkbox_7)
        self.lineEdit_16.textChanged.connect(self.check_checkbox_7_line_edits)
        self.lineEdit_17.textChanged.connect(self.check_checkbox_7_line_edits)
        self.lineEdit_18.textChanged.connect(self.check_checkbox_7_line_edits)
        self.checkBox_8.toggled.connect(self.check_checkbox_8)
        self.lineEdit_19.textChanged.connect(self.check_checkbox_8_line_edits)
        self.lineEdit_20.textChanged.connect(self.check_checkbox_8_line_edits)
        self.lineEdit_21.textChanged.connect(self.check_checkbox_8_line_edits)
        self.checkBox_9.toggled.connect(self.check_checkbox_9)
        self.lineEdit_22.textChanged.connect(self.check_checkbox_9_line_edits)
        self.lineEdit_23.textChanged.connect(self.check_checkbox_9_line_edits)
        self.lineEdit_24.textChanged.connect(self.check_checkbox_9_line_edits)
        self.checkBox_10.toggled.connect(self.check_checkbox_10)
        self.lineEdit_25.textChanged.connect(self.check_checkbox_10_line_edits)
        self.lineEdit_26.textChanged.connect(self.check_checkbox_10_line_edits)
        self.lineEdit_27.textChanged.connect(self.check_checkbox_10_line_edits)
        self.checkBox_11.toggled.connect(self.check_checkbox_11)
        self.lineEdit_28.textChanged.connect(self.check_checkbox_11_line_edits)
        self.lineEdit_29.textChanged.connect(self.check_checkbox_11_line_edits)
        self.lineEdit_30.textChanged.connect(self.check_checkbox_11_line_edits)
        self.checkBox_12.toggled.connect(self.check_checkbox_12)
        self.lineEdit_31.textChanged.connect(self.check_checkbox_12_line_edits)
        self.lineEdit_32.textChanged.connect(self.check_checkbox_12_line_edits)
        self.lineEdit_33.textChanged.connect(self.check_checkbox_12_line_edits)

        self.pushButton_next.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    
    def initialize_form(self):
        """Initialize the form to its starting state"""
        # Disable all controls except the first checkbox
        self.checkBox_2.setEnabled(False)
        self.frame_11.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.frame_12.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.frame_13.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.frame_14.setEnabled(False)
        self.checkBox_13.setEnabled(False)
        self.frame_29.setEnabled(False)
        
        # Right column
        self.checkBox_6.setEnabled(False)
        self.frame_15.setEnabled(False)
        self.checkBox_7.setEnabled(False)
        self.frame_16.setEnabled(False)
        self.checkBox_8.setEnabled(False)
        self.frame_18.setEnabled(False)
        self.checkBox_9.setEnabled(False)
        self.frame_20.setEnabled(False)
        self.checkBox_10.setEnabled(False)
        self.frame_22.setEnabled(False)
        self.checkBox_11.setEnabled(False)
        self.frame_24.setEnabled(False)
        self.checkBox_12.setEnabled(False)
        self.frame_26.setEnabled(False)
        
        self.pushButton_next.setEnabled(False)
        
        # Clear all inputs
        self.clear_all_inputs()
    
    def clear_all_inputs(self):
        """Clear all line edits and uncheck all checkboxes except the first"""
        # Keep checkBox_1 enabled, clear others
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_13.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        
        # Clear all line edits
        for i in range(1, 37):
            line_edit = getattr(self, f'lineEdit_{i}', None)
            if line_edit:
                line_edit.clear()
    
    # Left column validation functions
    def check_checkbox_1(self):
        """Check first checkbox and enable second checkbox"""
        if self.checkBox_1.isChecked():
            self.checkBox_2.setEnabled(True)
        else:
            # Reset all subsequent controls
            self.checkBox_2.setEnabled(False)
            self.reset_from_checkbox_2()
    
    def check_checkbox_2(self):
        """Check second checkbox and enable its line edits"""
        if self.checkBox_2.isChecked():
            self.frame_11.setEnabled(True)
        else:
            self.frame_11.setEnabled(False)
            self.reset_from_checkbox_3()  # Only reset subsequent controls, not this one
    
    def check_checkbox_2_line_edits(self):
        """Check if all line edits for checkbox 2 are filled"""
        if (self.checkBox_2.isChecked() and 
            self.lineEdit_1.text().strip() and 
            self.lineEdit_2.text().strip() and 
            self.lineEdit_3.text().strip()):
            self.checkBox_3.setEnabled(True)
        else:
            self.checkBox_3.setEnabled(False)
            self.reset_from_checkbox_3()
    
    def check_checkbox_3(self):
        """Check third checkbox and enable its line edits"""
        if self.checkBox_3.isChecked():
            self.frame_12.setEnabled(True)
        else:
            self.frame_12.setEnabled(False)
            self.reset_from_checkbox_4()  # Only reset subsequent controls, not this one
    
    def check_checkbox_3_line_edits(self):
        """Check if all line edits for checkbox 3 are filled"""
        if (self.checkBox_3.isChecked() and 
            self.lineEdit_4.text().strip() and 
            self.lineEdit_5.text().strip() and 
            self.lineEdit_6.text().strip()):
            self.checkBox_4.setEnabled(True)
        else:
            self.checkBox_4.setEnabled(False)
            self.reset_from_checkbox_4()
    
    def check_checkbox_4(self):
        """Check fourth checkbox and enable its line edits"""
        if self.checkBox_4.isChecked():
            self.frame_13.setEnabled(True)
        else:
            self.frame_13.setEnabled(False)
            self.reset_from_checkbox_5()  # Only reset subsequent controls, not this one
    
    def check_checkbox_4_line_edits(self):
        """Check if all line edits for checkbox 4 are filled"""
        if (self.checkBox_4.isChecked() and 
            self.lineEdit_7.text().strip() and 
            self.lineEdit_8.text().strip() and 
            self.lineEdit_9.text().strip()):
            self.checkBox_5.setEnabled(True)
        else:
            self.checkBox_5.setEnabled(False)
            self.reset_from_checkbox_5()
    
    def check_checkbox_5(self):
        """Check fifth checkbox and enable its line edits"""
        if self.checkBox_5.isChecked():
            self.frame_14.setEnabled(True)
        else:
            self.frame_14.setEnabled(False)
            self.reset_from_checkbox_13()  # Only reset subsequent controls, not this one
    
    def check_checkbox_5_line_edits(self):
        """Check if all line edits for checkbox 5 are filled"""
        if (self.checkBox_5.isChecked() and 
            self.lineEdit_10.text().strip() and 
            self.lineEdit_11.text().strip() and 
            self.lineEdit_12.text().strip()):
            self.checkBox_13.setEnabled(True)
        else:
            self.checkBox_13.setEnabled(False)
            self.reset_from_checkbox_13()
    
    def check_checkbox_13(self):
        """Check checkbox 13 and enable its line edits"""
        if self.checkBox_13.isChecked():
            self.frame_29.setEnabled(True)
        else:
            self.frame_29.setEnabled(False)
            self.reset_from_checkbox_6()  # Only reset subsequent controls, not this one
    
    def check_checkbox_13_line_edits(self):
        """Check if all line edits for checkbox 13 are filled"""
        if (self.checkBox_13.isChecked() and 
            self.lineEdit_34.text().strip() and 
            self.lineEdit_35.text().strip() and 
            self.lineEdit_36.text().strip()):
            self.checkBox_6.setEnabled(True)
        else:
            self.checkBox_6.setEnabled(False)
            self.reset_from_checkbox_6()
    
    # Right column validation functions
    def check_checkbox_6(self):
        """Check checkbox 6 and enable its line edits"""
        if self.checkBox_6.isChecked():
            self.frame_15.setEnabled(True)
        else:
            self.frame_15.setEnabled(False)
            self.reset_from_checkbox_7()  # Only reset subsequent controls, not this one
    
    def check_checkbox_6_line_edits(self):
        """Check if all line edits for checkbox 6 are filled"""
        if (self.checkBox_6.isChecked() and 
            self.lineEdit_13.text().strip() and 
            self.lineEdit_14.text().strip() and 
            self.lineEdit_15.text().strip()):
            self.checkBox_7.setEnabled(True)
        else:
            self.checkBox_7.setEnabled(False)
            self.reset_from_checkbox_7()
    
    def check_checkbox_7(self):
        """Check checkbox 7 and enable its line edits"""
        if self.checkBox_7.isChecked():
            self.frame_16.setEnabled(True)
        else:
            self.frame_16.setEnabled(False)
            self.reset_from_checkbox_8()  # Only reset subsequent controls, not this one
    
    def check_checkbox_7_line_edits(self):
        """Check if all line edits for checkbox 7 are filled"""
        if (self.checkBox_7.isChecked() and 
            self.lineEdit_16.text().strip() and 
            self.lineEdit_17.text().strip() and 
            self.lineEdit_18.text().strip()):
            self.checkBox_8.setEnabled(True)
        else:
            self.checkBox_8.setEnabled(False)
            self.reset_from_checkbox_8()
    
    def check_checkbox_8(self):
        """Check checkbox 8 and enable its line edits"""
        if self.checkBox_8.isChecked():
            self.frame_18.setEnabled(True)
        else:
            self.frame_18.setEnabled(False)
            self.reset_from_checkbox_9()  # Only reset subsequent controls, not this one
    
    def check_checkbox_8_line_edits(self):
        """Check if all line edits for checkbox 8 are filled"""
        if (self.checkBox_8.isChecked() and 
            self.lineEdit_19.text().strip() and 
            self.lineEdit_20.text().strip() and 
            self.lineEdit_21.text().strip()):
            self.checkBox_9.setEnabled(True)
        else:
            self.checkBox_9.setEnabled(False)
            self.reset_from_checkbox_9()
    
    def check_checkbox_9(self):
        """Check checkbox 9 and enable its line edits"""
        if self.checkBox_9.isChecked():
            self.frame_20.setEnabled(True)
        else:
            self.frame_20.setEnabled(False)
            self.reset_from_checkbox_10()  # Only reset subsequent controls, not this one
    
    def check_checkbox_9_line_edits(self):
        """Check if all line edits for checkbox 9 are filled"""
        if (self.checkBox_9.isChecked() and 
            self.lineEdit_22.text().strip() and 
            self.lineEdit_23.text().strip() and 
            self.lineEdit_24.text().strip()):
            self.checkBox_10.setEnabled(True)
        else:
            self.checkBox_10.setEnabled(False)
            self.reset_from_checkbox_10()
    
    def check_checkbox_10(self):
        """Check checkbox 10 and enable its line edits"""
        if self.checkBox_10.isChecked():
            self.frame_22.setEnabled(True)
        else:
            self.frame_22.setEnabled(False)
            self.reset_from_checkbox_11()  # Only reset subsequent controls, not this one
    
    def check_checkbox_10_line_edits(self):
        """Check if all line edits for checkbox 10 are filled"""
        if (self.checkBox_10.isChecked() and 
            self.lineEdit_25.text().strip() and 
            self.lineEdit_26.text().strip() and 
            self.lineEdit_27.text().strip()):
            self.checkBox_11.setEnabled(True)
        else:
            self.checkBox_11.setEnabled(False)
            self.reset_from_checkbox_11()
    
    def check_checkbox_11(self):
        """Check checkbox 11 and enable its line edits"""
        if self.checkBox_11.isChecked():
            self.frame_24.setEnabled(True)
        else:
            self.frame_24.setEnabled(False)
            self.reset_from_checkbox_12()  # Only reset subsequent controls, not this one
    
    def check_checkbox_11_line_edits(self):
        """Check if all line edits for checkbox 11 are filled"""
        if (self.checkBox_11.isChecked() and 
            self.lineEdit_28.text().strip() and 
            self.lineEdit_29.text().strip() and 
            self.lineEdit_30.text().strip()):
            self.checkBox_12.setEnabled(True)
        else:
            self.checkBox_12.setEnabled(False)
            self.reset_from_checkbox_12()
    
    def check_checkbox_12(self):
        """Check checkbox 12 and enable its line edits"""
        if self.checkBox_12.isChecked():
            self.frame_26.setEnabled(True)
        else:
            self.frame_26.setEnabled(False)
            # No subsequent controls to reset for the last checkbox
            self.pushButton_next.setEnabled(False)
    
    def check_checkbox_12_line_edits(self):
        """Check if all line edits for checkbox 12 are filled"""
        if (self.checkBox_12.isChecked() and 
            self.lineEdit_31.text().strip() and 
            self.lineEdit_32.text().strip() and 
            self.lineEdit_33.text().strip()):
            self.pushButton_next.setEnabled(True)
        else:
            self.pushButton_next.setEnabled(False)
    
    # Reset functions for cascading cleanup - only handle enablement, preserve user choices
    def reset_from_checkbox_2(self):
        """Reset all controls from checkbox 2 onwards - only disable, don't clear"""
        self.frame_11.setEnabled(False)
        self.reset_from_checkbox_3()
    
    def reset_from_checkbox_3(self):
        """Reset all controls from checkbox 3 onwards - only disable, don't clear"""
        self.checkBox_3.setEnabled(False)
        self.frame_12.setEnabled(False)
        self.reset_from_checkbox_4()
    
    def reset_from_checkbox_4(self):
        """Reset all controls from checkbox 4 onwards - only disable, don't clear"""
        self.checkBox_4.setEnabled(False)
        self.frame_13.setEnabled(False)
        self.reset_from_checkbox_5()
    
    def reset_from_checkbox_5(self):
        """Reset all controls from checkbox 5 onwards - only disable, don't clear"""
        self.checkBox_5.setEnabled(False)
        self.frame_14.setEnabled(False)
        self.reset_from_checkbox_13()
    
    def reset_from_checkbox_13(self):
        """Reset all controls from checkbox 13 onwards - only disable, don't clear"""
        self.checkBox_13.setEnabled(False)
        self.frame_29.setEnabled(False)
        self.reset_from_checkbox_6()
    
    def reset_from_checkbox_6(self):
        """Reset all controls from checkbox 6 onwards (right column) - only disable, don't clear"""
        self.checkBox_6.setEnabled(False)
        self.frame_15.setEnabled(False)
        self.reset_from_checkbox_7()
    
    def reset_from_checkbox_7(self):
        """Reset all controls from checkbox 7 onwards - only disable, don't clear"""
        self.checkBox_7.setEnabled(False)
        self.frame_16.setEnabled(False)
        self.reset_from_checkbox_8()
    
    def reset_from_checkbox_8(self):
        """Reset all controls from checkbox 8 onwards - only disable, don't clear"""
        self.checkBox_8.setEnabled(False)
        self.frame_18.setEnabled(False)
        self.reset_from_checkbox_9()
    
    def reset_from_checkbox_9(self):
        """Reset all controls from checkbox 9 onwards - only disable, don't clear"""
        self.checkBox_9.setEnabled(False)
        self.frame_20.setEnabled(False)
        self.reset_from_checkbox_10()
    
    def reset_from_checkbox_10(self):
        """Reset all controls from checkbox 10 onwards - only disable, don't clear"""
        self.checkBox_10.setEnabled(False)
        self.frame_22.setEnabled(False)
        self.reset_from_checkbox_11()
    
    def reset_from_checkbox_11(self):
        """Reset all controls from checkbox 11 onwards - only disable, don't clear"""
        self.checkBox_11.setEnabled(False)
        self.frame_24.setEnabled(False)
        self.reset_from_checkbox_12()
    
    def reset_from_checkbox_12(self):
        """Reset all controls from checkbox 12 onwards - only disable, don't clear"""
        self.checkBox_12.setEnabled(False)
        self.frame_26.setEnabled(False)
        self.pushButton_next.setEnabled(False)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Set in Constant Speed mode", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Caution</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic;\">Wait till water comes out of the open restrictor, carefully monitor </span><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic; color:#231f20;\">the </span></p><p><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic; color:#231f20;\">hydraulic pressure not to increase (if it does stop the pump immediately)</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">After 2 Strokes</span></p></body></html>", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Caution</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic; color:#231f20;\">Current Limit for a single MRPO is 8.5A [MREL] and 8A [Legacy]</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -500 and set Restrictor - 1000psi (3Strokes)", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -500 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -500 and set Restrictor - 2000psi (3Strokes)", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1000 and set Restrictor - 2000psi (3Strokes)", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_13.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1000 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_40.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1000 and set Restrictor - 1000psi (3Strokes)", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1500 and set Restrictor - 1000psi (3Strokes)", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1500 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -1500 and set Restrictor - 2000psi (3Strokes)", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -2000 and set Restrictor - 2000psi (3Strokes)", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -2000 and set Restrictor - 1500psi (3Strokes)", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.checkBox_12.setText(QCoreApplication.translate("Dialog", u"Set speed RPM -2000 and set Restrictor - 1000psi (3Strokes)", None))
        self.label_37.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">HPRESS</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PO Motor Current</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Stroke Time</span></p></body></html>", None))
        self.pushButton_next.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

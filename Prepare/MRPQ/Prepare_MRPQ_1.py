from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

from utils import resource_path

class  Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(935, 731)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.groupBox_1 = QGroupBox(self.frame)
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


        self.verticalLayout_2.addWidget(self.groupBox_1)

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


        self.verticalLayout_2.addWidget(self.frame_12)

        self.checkBox_1 = QCheckBox(self.frame)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(False)  # Initially disabled until gauge calibration selection
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
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

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_6)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(41, 41))
        self.label_7.setMaximumSize(QSize(41, 41))
        self.label_7.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.checkBox_6 = QCheckBox(self.frame_4)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_6)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_8 = QFrame(Dialog)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_2 = QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(280, 0))
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout_2.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout_2.addWidget(self.radioButton_5)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.comboBox = QComboBox(self.frame_8)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 25))
        self.comboBox.setMaximumSize(QSize(10000000, 25))

        self.verticalLayout_6.addWidget(self.comboBox)

        self.checkBox_8 = QCheckBox(self.frame_8)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_8.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_8)

        self.checkBox_7 = QCheckBox(self.frame_8)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_7)

        self.groupBox_3 = QGroupBox(self.frame_8)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(280, 0))
        self.groupBox_3.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_6 = QRadioButton(self.groupBox_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.groupBox_3)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.groupBox_3)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.groupBox_3)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_9)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.checkBox_9 = QCheckBox(self.frame_8)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_9.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_9)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(330, 160))
        self.label_10.setMaximumSize(QSize(330, 160))
        self.label_10.setPixmap(QPixmap(resource_path("Icons/Img_21.png")))
        self.label_10.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_10)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(41, 41))
        self.label_14.setMaximumSize(QSize(41, 41))
        self.label_14.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_14.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_14)

        self.groupBox_4 = QGroupBox(self.frame_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(230, 0))
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_10 = QRadioButton(self.groupBox_4)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.groupBox_4)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_11)


        self.horizontalLayout.addWidget(self.groupBox_4)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.checkBox_10 = QCheckBox(self.frame_8)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setEnabled(False)  # Initially disabled for progressive workflow
        self.checkBox_10.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_10)


        self.gridLayout.addWidget(self.frame_8, 0, 1, 1, 1)

        # Initialize visibility and progressive form
        self.initialize_visibility()
        self.initialize_progressive_form()
        self.connect_signals()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Finish and Move Forward", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Please download MRPQ Configuration from InTouch</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Open InTouch", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Is Valid SG/CQG/QZD gauge calibration available?", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Download from Maximo</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Checked that the flowline and hydraulic stabbers are \n"
" the correct pressure for the job", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"The stabber or receiver is set properly with a blank plug\n"
"depending on the position of the module in the toolstring", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"The CQG is flushed", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Check the Snubber and Plug installed </span></p><p><span style=\" font-size:12pt; font-weight:700;\">correctly to enable CQG reading</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Plug stamped \u201cP\u201d  installed in Port plug", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Snubber Stamped \u201cS\u201d installed in Snubber port", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Warning</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">If Swapped the CQG cannot read the flowline </span></p><p><span style=\" font-size:11pt;\">pressure, it will always remain at atmospheric pressue</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Check that sensor ports match the program</span></p></body></html>", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Warning</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Resistivity cell must always be installed in the Sensor Port 1</span></p></body></html>", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Which cell is put in Sensor Port 2", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Dummy", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"DV Rod", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"H2S Coupon", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Probe", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"MPMP", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"MPEP", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"MRLD", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"MRSD", None))

        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Please remove guard flowline socket and joint", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Install 100238610 Plug for MRPQ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Installing Anchoring Piston According to Hole Size", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"17.5 In - MRSL", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"12.25 In - MRLH", None))
        self.radioButton_8.setText(QCoreApplication.translate("Dialog", u"8.5 In - STD Piston (SRTP)", None))
        self.radioButton_9.setText(QCoreApplication.translate("Dialog", u"6 In - STD Piston (SRTP) with inner piston\n"
"locked with B030664 Retaining ring", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"Check ISO valve, Bypass valve\n"
"Screw Out till the truarc ring from Hydraulic side", None))
        self.label_10.setText("")
        self.label_14.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"MRPQ probe jig available in RB?", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_11.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"Can't check SG Pressure without jig \n"
"and sync pumping. Inform Base", None))
    # retranslateUi

    def initialize_visibility(self):
        """Initialize visibility of conditional frames and labels"""
        # Hide frames that should be conditionally visible
        self.frame_12.hide()  # Warning frame for gauge calibration   # Warning frame for CQG reading
        # self.frame_4.hide()   # Warning frame for resistivity cell
        self.label_14.hide()  # Risk icon for probe jig
        self.checkBox_7.hide()  # Hide checkbox_7 initially, show only for MRLD

    def initialize_progressive_form(self):
        """Initialize the progressive form with sequential workflow"""
        # Left side - sequential enabling (wait for groupBox_1 selection first)
        self.checkBox_1.setEnabled(False)  # Wait for gauge calibration selection
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        
        # Right side - sequential enabling
        self.groupBox_2.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.checkBox_8.setEnabled(False)
        self.checkBox_7.setEnabled(False)
        self.groupBox_3.setEnabled(False)
        self.checkBox_9.setEnabled(False)
        self.groupBox_4.setEnabled(False)
        self.checkBox_10.setEnabled(False)
        
        # Final button disabled initially
        self.pushButton.setEnabled(False)
        
        # InTouch button always available
        self.pushButton_2.setEnabled(True)

    def connect_signals(self):
        """Connect signals for progressive workflow and visibility logic"""
        # Radio button signals for visibility and enabling first checkbox
        self.radioButton_1.toggled.connect(self.handle_gauge_calibration_yes)
        self.radioButton_2.toggled.connect(self.handle_gauge_calibration)
        self.radioButton_11.toggled.connect(self.handle_probe_jig)
        
        # Checkbox signals for visibility
        # self.checkBox_3.stateChanged.connect(self.handle_checkbox3_visibility)
        self.checkBox_5.stateChanged.connect(self.handle_checkbox5_visibility)
        
        # Progressive workflow signals - left side
        self.checkBox_1.stateChanged.connect(self.handle_checkbox1)
        self.checkBox_2.stateChanged.connect(self.handle_checkbox2)
        self.checkBox_3.stateChanged.connect(self.handle_checkbox3)
        self.checkBox_4.stateChanged.connect(self.handle_checkbox4)
        self.checkBox_5.stateChanged.connect(self.handle_checkbox5)
        self.checkBox_6.stateChanged.connect(self.handle_checkbox6)
        
        # Progressive workflow signals - right side
        self.radioButton_3.toggled.connect(self.check_groupbox2_completion)
        self.radioButton_4.toggled.connect(self.check_groupbox2_completion)
        self.radioButton_5.toggled.connect(self.check_groupbox2_completion)
        self.comboBox.currentTextChanged.connect(self.handle_combobox)
        self.checkBox_8.stateChanged.connect(self.handle_checkbox8)
        self.checkBox_7.stateChanged.connect(self.handle_checkbox7)
        self.radioButton_6.toggled.connect(self.check_groupbox3_completion)
        self.radioButton_7.toggled.connect(self.check_groupbox3_completion)
        self.radioButton_8.toggled.connect(self.check_groupbox3_completion)
        self.radioButton_9.toggled.connect(self.check_groupbox3_completion)
        self.checkBox_9.stateChanged.connect(self.handle_checkbox9)
        self.radioButton_10.toggled.connect(self.check_groupbox4_completion)
        self.radioButton_11.toggled.connect(self.check_groupbox4_completion)
        self.checkBox_10.stateChanged.connect(self.handle_checkbox10)

    # Visibility handlers
    def handle_gauge_calibration_yes(self, checked):
        """Handle 'Yes' selection for gauge calibration - enable first checkbox"""
        if checked:
            self.checkBox_1.setEnabled(True)

    def handle_gauge_calibration(self, checked):
        """Show/hide frame_12 based on 'No' selection for gauge calibration and enable first checkbox"""
        self.frame_12.setVisible(checked)  # Show when "No" is selected
        if checked:
            self.checkBox_1.setEnabled(False)

    def handle_probe_jig(self, checked):
        """Show/hide label_14 based on 'No' selection for probe jig"""
        self.label_14.setVisible(checked)  # Show when "No" is selected

    def handle_checkbox5_visibility(self, state):
        
        pass 

    # Progressive workflow handlers - Left side
    def handle_checkbox1(self, state):
        """Handle checkbox 1 - enable checkbox 2"""
        if state == 2:
            self.checkBox_2.setEnabled(True)
        else:
            self.reset_availability_from_checkbox2()

    def handle_checkbox2(self, state):
        """Handle checkbox 2 - enable checkbox 3"""
        if state == 2:
            self.checkBox_3.setEnabled(True)
        else:
            self.reset_availability_from_checkbox3()

    def handle_checkbox3(self, state):
        """Handle checkbox 3 - enable checkbox 4"""
        if state == 2:
            self.checkBox_4.setEnabled(True)
        else:
            self.reset_availability_from_checkbox4()

    def handle_checkbox4(self, state):
        """Handle checkbox 4 - enable checkbox 5"""
        if state == 2:
            self.checkBox_5.setEnabled(True)
        else:
            self.reset_availability_from_checkbox5()

    def handle_checkbox5(self, state):
        """Handle checkbox 5 - enable checkbox 6"""
        if state == 2:
            self.checkBox_6.setEnabled(True)
        else:
            self.reset_availability_from_checkbox6()

    def handle_checkbox6(self, state):
        """Handle checkbox 6 - enable right side"""
        if state == 2:
            self.groupBox_2.setEnabled(True)
        else:
            self.reset_availability_right_side()

    # Progressive workflow handlers - Right side
    def check_groupbox2_completion(self):
        """Check if groupBox_2 has a selection and enable comboBox"""
        if self.radioButton_3.isChecked() or self.radioButton_4.isChecked() or self.radioButton_5.isChecked():
            self.comboBox.setEnabled(True)
        else:
            self.reset_availability_from_combobox()

    def handle_combobox(self, text):
        """Handle comboBox selection - enable checkbox 8 and update text based on probe type"""
        if text != "Select Probe":
            # Update checkbox_8 text based on probe selection
            if text in ["MPMP", "MPEP"]:
                self.checkBox_8.setText("Check the Packer According to Hole Size")
            elif text in ["MRLD", "MRSD"]:
                self.checkBox_8.setText("Remove the guard flowline socket and joint")
            
            # Show/hide checkbox_7 based on probe selection
            if text == "MRLD":
                self.checkBox_7.show()
            else:
                self.checkBox_7.hide()
            
            self.checkBox_8.setEnabled(True)
        else:
            self.reset_availability_from_checkbox8()

    def handle_checkbox8(self, state):
        """Handle checkbox 8 - enable next step based on checkbox_7 visibility"""
        if state == 2:
            # If checkbox_7 is visible (MRLD selected), enable it
            if self.checkBox_7.isVisible():
                self.checkBox_7.setEnabled(True)
            else:
                # If checkbox_7 is hidden (MPMP, MPEP, MRSD), skip to groupBox_3
                self.groupBox_3.setEnabled(True)
        else:
            if self.checkBox_7.isVisible():
                self.reset_availability_from_checkbox7()
            else:
                self.reset_availability_from_groupbox3()

    def handle_checkbox7(self, state):
        """Handle checkbox 7 - enable groupBox 3"""
        if state == 2:
            self.groupBox_3.setEnabled(True)
        else:
            self.reset_availability_from_groupbox3()

    def check_groupbox3_completion(self):
        """Check if groupBox_3 has a selection and enable checkbox 9"""
        if (self.radioButton_6.isChecked() or self.radioButton_7.isChecked() or 
            self.radioButton_8.isChecked() or self.radioButton_9.isChecked()):
            self.checkBox_9.setEnabled(True)
        else:
            self.reset_availability_from_checkbox9()

    def handle_checkbox9(self, state):
        """Handle checkbox 9 - enable groupBox 4"""
        if state == 2:
            self.groupBox_4.setEnabled(True)
        else:
            self.reset_availability_from_groupbox4()

    def check_groupbox4_completion(self):
        """Check if groupBox_4 has a selection and enable final elements"""
        if self.radioButton_10.isChecked():
            # If "Yes" selected, skip checkbox 10 and enable finish button
            self.checkBox_10.setEnabled(False)
            self.pushButton.setEnabled(True)
        elif self.radioButton_11.isChecked():
            # If "No" selected, enable checkbox 10
            self.checkBox_10.setEnabled(True)
            self.pushButton.setEnabled(False)
        else:
            self.checkBox_10.setEnabled(False)
            self.pushButton.setEnabled(False)

    def handle_checkbox10(self, state):
        """Handle checkbox 10 - enable finish button"""
        if state == 2:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    # Availability reset methods - disable elements but preserve user choices
    def reset_availability_from_checkbox2(self):
        """Reset availability from checkbox 2 onwards without clearing values"""
        self.checkBox_2.setEnabled(False)
        self.reset_availability_from_checkbox3()

    def reset_availability_from_checkbox3(self):
        """Reset availability from checkbox 3 onwards without clearing values"""
        self.checkBox_3.setEnabled(False)
        self.reset_availability_from_checkbox4()

    def reset_availability_from_checkbox4(self):
        """Reset availability from checkbox 4 onwards without clearing values"""
        self.checkBox_4.setEnabled(False)
        self.reset_availability_from_checkbox5()

    def reset_availability_from_checkbox5(self):
        """Reset availability from checkbox 5 onwards without clearing values"""
        self.checkBox_5.setEnabled(False)
        self.reset_availability_from_checkbox6()

    def reset_availability_from_checkbox6(self):
        """Reset availability from checkbox 6 onwards without clearing values"""
        self.checkBox_6.setEnabled(False)
        self.reset_availability_right_side()

    def reset_availability_right_side(self):
        """Reset availability of all right side elements without clearing values"""
        self.groupBox_2.setEnabled(False)
        self.reset_availability_from_combobox()

    def reset_availability_from_combobox(self):
        """Reset availability from comboBox onwards without clearing values"""
        self.comboBox.setEnabled(False)
        self.checkBox_7.hide()  # Hide checkbox_7 when resetting from combobox
        self.reset_availability_from_checkbox8()

    def reset_availability_from_checkbox8(self):
        """Reset availability from checkbox 8 onwards without clearing values"""
        self.checkBox_8.setEnabled(False)
        # Only reset checkbox_7 if it's visible, otherwise directly reset groupbox3
        if self.checkBox_7.isVisible():
            self.reset_availability_from_checkbox7()
        else:
            self.reset_availability_from_groupbox3()

    def reset_availability_from_checkbox7(self):
        """Reset availability from checkbox 7 onwards without clearing values"""
        self.checkBox_7.setEnabled(False)
        self.reset_availability_from_groupbox3()

    def reset_availability_from_groupbox3(self):
        """Reset availability from groupBox 3 onwards without clearing values"""
        self.groupBox_3.setEnabled(False)
        self.reset_availability_from_checkbox9()

    def reset_availability_from_checkbox9(self):
        """Reset availability from checkbox 9 onwards without clearing values"""
        self.checkBox_9.setEnabled(False)
        self.reset_availability_from_groupbox4()

    def reset_availability_from_groupbox4(self):
        """Reset availability from groupBox 4 onwards without clearing values"""
        self.groupBox_4.setEnabled(False)
        self.checkBox_10.setEnabled(False)
        self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
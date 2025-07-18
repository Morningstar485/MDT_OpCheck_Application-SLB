# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MRPC_UI_11noJKXA.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(695, 479)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_1 = QCheckBox(self.frame_2)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_3.addWidget(self.checkBox_1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(600, 150))
        self.label_2.setMaximumSize(QSize(500, 100))
        self.label_2.setPixmap(QPixmap(resource_path("Icons/Img_20.png")))
        self.label_2.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.verticalLayout.addWidget(self.checkBox_2)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.retranslateUi(Form)

        self.checkBox_2.setEnabled(False)  # Initially disabled, will be enabled by the wizard
        self.label_4.hide()

        self.checkBox_1.toggled.connect(self.checkBox_2.setEnabled)
        self.checkBox_2.toggled.connect(self.label_4.setVisible)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Set the A10 Switch to TW-STD</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("Form", u"Please Pull the MRPC Housing and disconnect wire connection\n"
"at upper head and do ET-1 before installing Housing", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Line 6 (sonde power), 20, 21 (main power) through MDT string is used for MIFA, MRBA and any </span></p><p><span style=\" font-size:11pt; font-weight:700;\">other non-MDT connected below. When none of these tools presents in the string, all the lines </span></p><p><span style=\" font-size:11pt; font-weight:700;\">should be disconnected to avoid noise and signal interference to other lines.</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Again do the ET-1 after installing Housing and check the Lines", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Please Move Back and Check Resistivity Again</span></p></body></html>", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
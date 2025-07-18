from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from utils import resource_path
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(613, 366)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.checkBox_1 = QCheckBox(Dialog)
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

        self.checkBox_2 = QCheckBox(Dialog)
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

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(31, 31))
        self.label_6.setMaximumSize(QSize(31, 31))
        self.label_6.setPixmap(QPixmap(resource_path("Icons/Info.png")))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_4)

        self.checkBox_3 = QCheckBox(Dialog)
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

        self.checkBox_4 = QCheckBox(Dialog)
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

        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_6)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Please download MRHY Configuration from InTouch</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Open InTouch", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Checked the hydraulic plugs/stabbers are in the correct location \n"
"for the HY/PS/PQ configuration and are of the correct type", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Checked that ADV is closed by turning right valve needle with 10 ft.lbs torque", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">DO NOT torque the ADV over 10 ft.lbs.Torque values over the specification </span></p><p><span style=\" font-size:12pt;\">can crack the drain valve seat causing the in ability to build up pressure</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Make sure the compensator pistons are clean and not stuck", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Oil level is full when three (3) springs can be seen", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
        
        # Initialize progressive form
        self.initialize_progressive_form()
        
        # Setup signals
        self.setup_progressive_signals()
        
        # Connect InTouch button to open URL
        self.pushButton_2.clicked.connect(self.open_intouch_url)
    # retranslateUi

    def open_intouch_url(self):
        """Open the InTouch URL in the default web browser"""
        url = QUrl("https://intouchsupport.com/index.cfm?event=content.preview&contentId=7108128&FromRefPage=Y")
        QDesktopServices.openUrl(url)
    
    def initialize_progressive_form(self):
        """Initialize the progressive form - hide and disable elements until previous steps are completed"""
        self.checkBox_2.setEnabled(False)
        # self.frame_4.setVisible(False)  # Hide info frame initially
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.pushButton.setEnabled(False)
    
    def setup_progressive_signals(self):
        """Setup signal connections for progressive form logic"""
        self.checkBox_1.toggled.connect(lambda: self.handle_checkbox1())
        self.checkBox_2.toggled.connect(lambda: self.handle_checkbox2())
        self.checkBox_3.toggled.connect(lambda: self.handle_checkbox3())
        self.checkBox_4.toggled.connect(lambda: self.handle_checkbox4())
    
    def handle_checkbox1(self):
        """Handle checkbox 1 - enables checkbox 2"""
        if self.checkBox_1.isChecked():
            self.checkBox_2.setEnabled(True)
            self.frame_4.setVisible(True)
        else:
            # Reset subsequent elements
            self.checkBox_2.setEnabled(False)
            self.checkBox_2.setChecked(False)
            self.frame_4.setVisible(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.pushButton.setEnabled(False)
    
    def handle_checkbox2(self):
        """Handle checkbox 2 - shows info frame and enables checkbox 3"""
        if self.checkBox_2.isChecked():
              # Show info frame
            self.checkBox_3.setEnabled(True)
        else:
            # Reset subsequent elements
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.pushButton.setEnabled(False)
    
    def handle_checkbox3(self):
        """Handle checkbox 3 - enables checkbox 4"""
        if self.checkBox_3.isChecked():
            self.checkBox_4.setEnabled(True)
        else:
            # Reset subsequent elements
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.pushButton.setEnabled(False)
    
    def handle_checkbox4(self):
        """Handle checkbox 4 - enables push button"""
        if self.checkBox_4.isChecked():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
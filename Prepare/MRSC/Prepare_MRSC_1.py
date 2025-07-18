from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(519, 645)
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

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.groupBox_6 = QGroupBox(Dialog)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Radio_Frame_1 = QFrame(self.groupBox_6)
        self.Radio_Frame_1.setObjectName(u"Radio_Frame_1")
        self.Radio_Frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Radio_Frame_1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
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

        self.radioButton_3 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_3)


        self.verticalLayout_11.addWidget(self.Radio_Frame_1)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(Dialog)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Radio_Frame_2 = QFrame(self.groupBox_7)
        self.Radio_Frame_2.setObjectName(u"Radio_Frame_2")
        self.Radio_Frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Radio_Frame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
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

        self.radioButton_5 = QRadioButton(self.Radio_Frame_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_5)


        self.verticalLayout_13.addWidget(self.Radio_Frame_2)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.frame_12 = QFrame(Dialog)
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

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Radio_Frame_3 = QFrame(self.groupBox_2)
        self.Radio_Frame_3.setObjectName(u"Radio_Frame_3")
        self.Radio_Frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Radio_Frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
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

        self.radioButton_7 = QRadioButton(self.Radio_Frame_3)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_7)


        self.verticalLayout_15.addWidget(self.Radio_Frame_3)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.frame_13 = QFrame(Dialog)
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


        self.verticalLayout.addWidget(self.frame_13)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_5)

        self.retranslateUi(Dialog)
        
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Please download MDT MRSC Configuration from InTouch</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Open InTouch", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Select the type of preparation of MRSC ", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Low Shock", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Water Receptacle", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Exit Port", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Is the exit screen filter available?", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Ask for the filter from Base</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Check that the piston is on the top position, against the retaining ring</span></p><p><span style=\" font-size:12pt;\">If not, this is an indication that the oil level is low and needs to be filled</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Is the Oil level Full?", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Please fill up the oil</span></p></body></html>", None))
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
        url = QUrl("https://intouchsupport.com/index.cfm?event=content.preview&contentId=7104273&FromRefPage=Y")
        QDesktopServices.openUrl(url)
    
    def initialize_progressive_form(self):
        """Initialize the progressive form - hide and disable elements until previous steps are completed"""
        # Disable subsequent groupboxes
        self.groupBox_7.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        
        # Hide warning frames initially
        self.frame_12.setVisible(False)  # Frame below groupBox_7
        self.frame_13.setVisible(False)  # Frame below groupBox_2
        
        # Hide instruction label above groupBox_2
        # self.label_3.setVisible(False)
        
        # Disable push button
        self.pushButton.setEnabled(False)
    
    def setup_progressive_signals(self):
        """Setup signal connections for progressive form logic"""
        # First groupbox (MRSC type selection)
        self.radioButton_1.toggled.connect(lambda: self.handle_groupbox6_selection())
        self.radioButton_2.toggled.connect(lambda: self.handle_groupbox6_selection())
        self.radioButton_3.toggled.connect(lambda: self.handle_groupbox6_selection())
        
        # Second groupbox (exit screen filter)
        self.radioButton_4.toggled.connect(lambda: self.handle_groupbox7_selection())
        self.radioButton_5.toggled.connect(lambda: self.handle_groupbox7_selection())
        
        # Third groupbox (oil level)
        self.radioButton_6.toggled.connect(lambda: self.handle_groupbox2_selection())
        self.radioButton_7.toggled.connect(lambda: self.handle_groupbox2_selection())
    
    def handle_groupbox6_selection(self):
        """Handle first groupbox selection (MRSC type)"""
        # Reset all subsequent elements
        self.reset_subsequent_elements()
        
        if self.radioButton_1.isChecked() or self.radioButton_2.isChecked():
            # Option 1 (Low Shock) or 2 (Water Receptacle) selected
            # Skip groupBox_7, go directly to groupBox_2
            # self.label_3.setVisible(True)  # Show instruction label
            self.groupBox_2.setEnabled(True)  # Enable oil level groupbox
        elif self.radioButton_3.isChecked():
            # Option 3 (Exit Port) selected
            # Enable groupBox_7 (exit screen filter)
            self.groupBox_7.setEnabled(True)
    
    def handle_groupbox7_selection(self):
        """Handle second groupbox selection (exit screen filter)"""
        # Reset oil level groupbox
        self.groupBox_2.setEnabled(False)
        self.label_3.setVisible(False)
        self.frame_13.setVisible(False)
        self.radioButton_6.setChecked(False)
        self.radioButton_7.setChecked(False)
        self.pushButton.setEnabled(False)
        
        if self.radioButton_4.isChecked():
            # "Yes" selected - enable oil level groupbox
            self.label_3.setVisible(True)
            self.groupBox_2.setEnabled(True)
            self.frame_12.setVisible(False)  # Hide warning frame
        elif self.radioButton_5.isChecked():
            # "No" selected - show warning frame
            self.frame_12.setVisible(True)
            # Don't enable oil level groupbox yet
    
    def handle_groupbox2_selection(self):
        """Handle third groupbox selection (oil level)"""
        if self.radioButton_6.isChecked():
            # "Yes" selected - enable push button
            self.frame_13.setVisible(False)  # Hide warning frame
            self.pushButton.setEnabled(True)
        elif self.radioButton_7.isChecked():
            # "No" selected - show warning frame
            self.frame_13.setVisible(True)
            self.pushButton.setEnabled(False)
    
    def reset_subsequent_elements(self):
        """Reset all subsequent elements to initial state"""
        # Disable groupboxes
        self.groupBox_7.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        
        # Hide frames
        self.frame_12.setVisible(False)
        self.frame_13.setVisible(False)
        # self.label_3.setVisible(False)
        
        # Clear selections
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        self.radioButton_6.setChecked(False)
        self.radioButton_7.setChecked(False)
        
        # Disable push button
        self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
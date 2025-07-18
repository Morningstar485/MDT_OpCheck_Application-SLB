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

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(517, 391)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_5)

        self.groupBox_1 = QGroupBox(Dialog)
        self.groupBox_1.setObjectName(u"groupBox_1")
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


        self.verticalLayout.addWidget(self.groupBox_1)

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

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_6)


        self.retranslateUi(Dialog)

        self.pushButton_2.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Set the MRPO to run in the In/Out mode", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Remove the drain plug (H217193)", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Verify that the manual 3-way flowline valve is set for IN/OUT operations", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Check Configuration from InTouch", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Is the exit screen filter available?", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Please raise requirement from base</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Next", None))
        
        # Initialize progressive form
        self.initialize_progressive_form()
        
        # Setup signals
        self.setup_progressive_signals()
        
        # Connect InTouch button to open URL
        self.pushButton.clicked.connect(self.open_link)
    # retranslateUi
    def open_link(self):
        """Open InTouch URL - this button is always available"""
        QDesktopServices.openUrl(QUrl("https://intouchsupport.com/index.cfm?event=content.preview&contentId=7033048&FromRefPage=Y"))

    def initialize_progressive_form(self):
        """Initialize the progressive form - disable elements until previous steps are completed"""
        # Disable subsequent elements
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.groupBox_1.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        
        # Hide warning elements initially
        self.frame_12.setVisible(False)
        self.frame.setVisible(False)
        
        # InTouch button stays enabled (not part of progressive algorithm)
    
    def setup_progressive_signals(self):
        """Setup signal connections for progressive form logic"""
        # Sequential checkboxes
        self.checkBox_1.toggled.connect(lambda: self.handle_checkbox1())
        self.checkBox_2.toggled.connect(lambda: self.handle_checkbox2())
        self.checkBox_3.toggled.connect(lambda: self.handle_checkbox3())
        
        # Radio button selections for filter availability
        self.radioButton_1.toggled.connect(lambda: self.handle_groupbox_selection())
        self.radioButton_2.toggled.connect(lambda: self.handle_groupbox_selection())
        
        # Final acknowledgment checkbox
        self.checkBox_4.toggled.connect(lambda: self.handle_checkbox4())
    
    def handle_checkbox1(self):
        """Handle checkbox 1 - enables checkbox 2"""
        if self.checkBox_1.isChecked():
            self.checkBox_2.setEnabled(True)
        else:
            # Reset subsequent elements
            self.checkBox_2.setEnabled(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.groupBox_1.setEnabled(False)
            self.radioButton_1.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.frame_12.setVisible(False)
            self.frame.setVisible(False)
            self.checkBox_4.setChecked(False)
            self.pushButton_2.setEnabled(False)
    
    def handle_checkbox2(self):
        """Handle checkbox 2 - enables checkbox 3"""
        if self.checkBox_2.isChecked():
            self.checkBox_3.setEnabled(True)
        else:
            # Reset subsequent elements
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.groupBox_1.setEnabled(False)
            self.radioButton_1.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.frame_12.setVisible(False)
            self.frame.setVisible(False)
            self.checkBox_4.setChecked(False)
            self.pushButton_2.setEnabled(False)
    
    def handle_checkbox3(self):
        """Handle checkbox 3 - enables groupbox"""
        if self.checkBox_3.isChecked():
            self.groupBox_1.setEnabled(True)
        else:
            # Reset subsequent elements
            self.groupBox_1.setEnabled(False)
            self.radioButton_1.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.frame_12.setVisible(False)
            self.frame.setVisible(False)
            self.checkBox_4.setChecked(False)
            self.pushButton_2.setEnabled(False)
    
    def handle_groupbox_selection(self):
        """Handle filter availability groupbox selection"""
        # Reset warning and acknowledgment elements
        self.frame_12.setVisible(False)
        self.frame.setVisible(False)
        self.checkBox_4.setChecked(False)
        self.pushButton_2.setEnabled(False)
        
        if self.radioButton_1.isChecked():
            # "Yes" selected - enable final button directly
            self.pushButton_2.setEnabled(True)
        elif self.radioButton_2.isChecked():
            # "No" selected - show warning and acknowledgment checkbox
            self.frame_12.setVisible(True)
            self.frame.setVisible(True)
    
    def handle_checkbox4(self):
        """Handle final acknowledgment checkbox"""
        if self.checkBox_4.isChecked() and self.radioButton_2.isChecked():
            # Acknowledgment checkbox checked when "No" was selected
            self.pushButton_2.setEnabled(True)
        elif not self.checkBox_4.isChecked() and self.radioButton_2.isChecked():
            # Acknowledgment checkbox unchecked when "No" was selected
            self.pushButton_2.setEnabled(False)

    # Note: InTouch button is always available for user convenience
    # Progressive algorithm only controls the "Next" button through checkbox sequence and yes/no question

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
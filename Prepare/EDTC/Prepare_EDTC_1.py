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
        Dialog.resize(390, 309)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.verticalLayout_2.addWidget(self.checkBox_1)

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
        self.radioButton_9 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.Radio_Frame_1)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_10)

        self.verticalLayout_11.addWidget(self.Radio_Frame_1)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.frame_14 = QFrame(Dialog)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(41, 41))
        self.label_14.setMaximumSize(QSize(41, 41))
        self.label_14.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame = QFrame(Dialog)
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


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.retranslateUi(Dialog)

        self.pushButton.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Check EDTC code for MDT\n"
"Need EDTC-B for the MDT job", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Is the Gamma Ray Jig Available?", None))
        self.radioButton_9.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Please inform PSD/JDL/Foreman</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
        
        # Hide warning elements initially
        self.frame_14.setVisible(False)
        self.frame.setVisible(False)
        
        # Initialize progressive form
        self.initialize_progressive_form()
        
        # Setup signals
        self.setup_progressive_signals()
    # retranslateUi

    def initialize_progressive_form(self):
        """Initialize the progressive form - disable groupbox and button until first checkbox is checked"""
        self.groupBox_6.setEnabled(False)
        self.pushButton.setEnabled(False)
    
    def setup_progressive_signals(self):
        """Setup signal connections for progressive form logic"""
        # First checkbox enables the groupbox
        self.checkBox_1.toggled.connect(lambda: self.check_first_checkbox())
        
        # Radio button selections
        self.radioButton_9.toggled.connect(lambda checked: self.handle_groupbox_selection() if checked else None)
        self.radioButton_10.toggled.connect(lambda checked: self.handle_groupbox_selection() if checked else None)
        
        # Second checkbox for completion
        self.checkBox_2.toggled.connect(lambda: self.check_completion())
    
    def check_first_checkbox(self):
        """Enable groupbox when first checkbox is checked"""
        if self.checkBox_1.isChecked():
            self.groupBox_6.setEnabled(True)
        else:
            self.groupBox_6.setEnabled(False)
            self.pushButton.setEnabled(False)
            # Reset groupbox state
            self.radioButton_9.setChecked(False)
            self.radioButton_10.setChecked(False)
            self.frame_14.setVisible(False)
            self.frame.setVisible(False)
            self.checkBox_2.setChecked(False)
    
    def handle_groupbox_selection(self):
        """Handle radio button selection in groupbox"""
        # Reset warning state
        self.frame_14.setVisible(False)
        self.frame.setVisible(False)
        self.checkBox_2.setChecked(False)
        self.pushButton.setEnabled(False)
        
        if self.radioButton_9.isChecked():  # Yes selected
            # No warning needed, form is complete - enable button
            self.pushButton.setEnabled(True)
        elif self.radioButton_10.isChecked():  # No selected
            # Show warning and acknowledgment checkbox
            self.frame_14.setVisible(True)
            self.frame.setVisible(True)
    
    def check_completion(self):
        """Check if form completion requirements are met"""
        if self.radioButton_10.isChecked() and self.checkBox_2.isChecked():
            # "No" was selected and acknowledgment checkbox is checked - form complete
            self.pushButton.setEnabled(True)
        elif self.radioButton_10.isChecked() and not self.checkBox_2.isChecked():
            # "No" was selected but acknowledgment checkbox not checked yet
            self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
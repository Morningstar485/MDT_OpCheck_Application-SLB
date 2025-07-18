from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(314, 300)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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


        self.verticalLayout_3.addWidget(self.groupBox_1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.comboBox)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(31, 31))
        self.label_6.setMaximumSize(QSize(31, 31))
        self.label_6.setPixmap(QPixmap(resource_path("Icons/Info.png")))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)


        self.verticalLayout_3.addWidget(self.frame_4)

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


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.retranslateUi(Dialog)

        # Initialize progressive form
        self.initialize_progressive_form()
        
        # Setup signals
        self.setup_progressive_signals()

        self.pushButton.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def initialize_progressive_form(self):
        """Initialize the progressive form - disable elements until previous steps are completed"""
        # Disable subsequent elements
        self.comboBox.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        
        # Hide info frame initially (this can stay as hide/show)
        self.frame_4.setVisible(False)
    
    def setup_progressive_signals(self):
        """Setup signal connections for progressive form logic"""
        # Radio button selections for purpose
        self.radioButton_1.toggled.connect(lambda: self.handle_purpose_selection())
        self.radioButton_2.toggled.connect(lambda: self.handle_purpose_selection())
        
        # ComboBox selection
        self.comboBox.currentIndexChanged.connect(self.handle_combobox_selection)
        
        # Radio button selections for mode
        self.radioButton_5.toggled.connect(lambda: self.handle_mode_selection())
        self.radioButton_6.toggled.connect(lambda: self.handle_mode_selection())
    
    def handle_purpose_selection(self):
        """Handle MRPO purpose selection"""
        if self.radioButton_1.isChecked() or self.radioButton_2.isChecked():
            # Either Sample Side or Guard Side selected - enable combobox
            self.comboBox.setEnabled(True)
            # Reset combobox to default selection
            self.comboBox.setCurrentIndex(0)
        else:
            # No selection - disable subsequent elements
            self.comboBox.setEnabled(False)
            self.comboBox.setCurrentIndex(0)
            self.groupBox_2.setEnabled(False)
            self.frame_4.setVisible(False)
            self.pushButton.setEnabled(False)
            # Clear radio button selections
            self.radioButton_5.setChecked(False)
            self.radioButton_6.setChecked(False)
    
    def handle_combobox_selection(self):
        """Handle DU selection from combobox"""
        idx = self.comboBox.currentIndex()
        
        if idx == 0:
            # Default "Select DU" - disable subsequent elements
            self.groupBox_2.setEnabled(False)
            self.frame_4.setVisible(False)
            self.pushButton.setEnabled(False)
            # Clear radio button selections
            self.radioButton_5.setChecked(False)
            self.radioButton_6.setChecked(False)
        elif idx == 4:
            # XXP selected - show info frame and enable mode selection
            self.frame_4.setVisible(True)
            self.groupBox_2.setEnabled(True)
        else:
            # STD, HP, or XP selected - hide info frame and enable mode selection
            self.frame_4.setVisible(False)
            self.groupBox_2.setEnabled(True)
    
    def handle_mode_selection(self):
        """Handle mode selection"""
        if self.radioButton_5.isChecked() or self.radioButton_6.isChecked():
            # Either UP/DOWN or IN/OUT selected - enable push button
            self.pushButton.setEnabled(True)
        else:
            # No mode selected - disable push button
            self.pushButton.setEnabled(False)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Select MRPO Purpose", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Sample Side", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Guard Side", None))  # Fixed typo: "Gaurd" -> "Guard"
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select DU", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"STD", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"HP", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"XP", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"XXP", None))

        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Note</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Please check the XXP stabber : MRDU-XX </span></p><p><span style=\" font-size:11pt;\">Stabber (100275502) and O-rings </span></p><p><span style=\" font-size:11pt;\">(B013113 (SP3) ,100739726 (XP3)) are </span></p><p><span style=\" font-size:11pt;\">different compared to all other 3 MRDU's</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Select Mode", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"UP/DOWN", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"IN/OUT", None))
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
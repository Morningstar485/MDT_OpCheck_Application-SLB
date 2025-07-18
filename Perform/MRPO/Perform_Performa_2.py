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
        Dialog.resize(587, 459)
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

        self.checkBox_5 = QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
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


        self.verticalLayout.addWidget(self.groupBox_2)

        self.checkBox_6 = QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_6)

        self.frame_28 = QFrame(Dialog)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_28)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_back = QPushButton(self.frame_28)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout.addWidget(self.pushButton_back)

        self.pushButton_finish = QPushButton(self.frame_28)
        self.pushButton_finish.setObjectName(u"pushButton_finish")

        self.horizontalLayout.addWidget(self.pushButton_finish)


        self.verticalLayout.addWidget(self.frame_28)

        self.frame_28.hide()


        self.retranslateUi(Dialog)
        
        # Initialize form state
        self.initialize_form()
        
        # Connect signals for sequential validation
        self.checkBox_1.toggled.connect(self.check_checkbox_1)
        self.checkBox_2.toggled.connect(self.check_checkbox_2)
        self.checkBox_3.toggled.connect(self.check_checkbox_3)
        self.checkBox_4.toggled.connect(self.check_checkbox_4)
        self.radioButton_2.toggled.connect(self.check_groupbox_1_selection)
        self.radioButton_1.toggled.connect(self.check_groupbox_1_selection)
        self.checkBox_5.toggled.connect(self.check_checkbox_5)
        self.radioButton_3.toggled.connect(self.check_groupbox_2_selection)
        self.radioButton_4.toggled.connect(self.check_groupbox_2_selection)
        self.checkBox_6.toggled.connect(self.check_checkbox_6)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    
    def initialize_form(self):
        """Initialize the form to its starting state"""
        # Hide error frame and checkbox 6 initially
        self.frame_12.hide()
        self.checkBox_6.hide()
        
        # Disable all controls except the first checkbox
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.groupBox_1.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.pushButton_finish.setEnabled(False)
        
        # Clear all selections
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_1.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
    
    def check_checkbox_1(self):
        """Check first checkbox and enable second checkbox"""
        if self.checkBox_1.isChecked():
            self.checkBox_2.setEnabled(True)
        else:
            # Reset all subsequent controls
            self.checkBox_2.setEnabled(False)
            self.reset_from_checkbox_2()
    
    def check_checkbox_2(self):
        """Check second checkbox and enable third checkbox"""
        if self.checkBox_2.isChecked():
            self.checkBox_3.setEnabled(True)
        else:
            self.checkBox_3.setEnabled(False)
            self.reset_from_checkbox_3()
    
    def check_checkbox_3(self):
        """Check third checkbox and enable fourth checkbox"""
        if self.checkBox_3.isChecked():
            self.checkBox_4.setEnabled(True)
        else:
            self.checkBox_4.setEnabled(False)
            self.reset_from_checkbox_4()
    
    def check_checkbox_4(self):
        """Check fourth checkbox and enable first group box"""
        if self.checkBox_4.isChecked():
            self.groupBox_1.setEnabled(True)
        else:
            self.groupBox_1.setEnabled(False)
            self.reset_from_groupbox_1()
    
    def check_groupbox_1_selection(self):
        """Check first group box selection and handle Yes/No logic"""
        if self.radioButton_2.isChecked():  # No selected
            self.frame_12.hide()  # Hide error frame
            self.checkBox_5.setEnabled(True)
        elif self.radioButton_1.isChecked():  # Yes selected
            self.frame_12.show()  # Show error frame
            # Stop logic progression when Yes (leak present) is selected
            self.checkBox_5.setEnabled(False)
            self.groupBox_2.setEnabled(False)
            self.checkBox_6.hide()
            self.pushButton_finish.setEnabled(False)
            # Reset subsequent selections
            self.checkBox_5.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            self.checkBox_6.setChecked(False)
    
    def check_checkbox_5(self):
        """Check fifth checkbox and enable second group box"""
        if self.checkBox_5.isChecked():
            self.groupBox_2.setEnabled(True)
        else:
            self.groupBox_2.setEnabled(False)
            self.reset_from_groupbox_2()
    
    def check_groupbox_2_selection(self):
        """Check second group box selection and handle Yes/No logic"""
        if self.radioButton_3.isChecked():  # Yes selected - HPRESS is between 0-200 Psi
            self.checkBox_6.show()  # Show checkbox 6
            self.checkBox_6.setEnabled(True)
            self.pushButton_finish.setEnabled(False)  # Wait for checkbox 6 to be checked
        elif self.radioButton_4.isChecked():  # No selected - HPRESS is not in range
            self.checkBox_6.hide()  # Hide checkbox 6
            self.checkBox_6.setEnabled(False)
            self.checkBox_6.setChecked(False)
            self.pushButton_finish.setEnabled(True)  # Directly enable push button
    
    def check_checkbox_6(self):
        """Check sixth checkbox and enable push button"""
        if self.checkBox_6.isChecked():
            self.pushButton_finish.setEnabled(True)
        else:
            self.pushButton_finish.setEnabled(False)
    
    # Reset functions for cascading cleanup - only handle enablement, preserve user choices
    def reset_from_checkbox_2(self):
        """Reset all controls from checkbox 2 onwards - only disable, don't clear"""
        self.checkBox_3.setEnabled(False)
        self.reset_from_checkbox_3()
    
    def reset_from_checkbox_3(self):
        """Reset all controls from checkbox 3 onwards - only disable, don't clear"""
        self.checkBox_4.setEnabled(False)
        self.reset_from_checkbox_4()
    
    def reset_from_checkbox_4(self):
        """Reset all controls from checkbox 4 onwards - only disable, don't clear"""
        self.groupBox_1.setEnabled(False)
        self.reset_from_groupbox_1()
    
    def reset_from_groupbox_1(self):
        """Reset all controls from group box 1 onwards - only disable, don't clear"""
        self.frame_12.hide()  # Always hide error frame when resetting
        self.checkBox_5.setEnabled(False)
        self.reset_from_checkbox_5()
    
    def reset_from_checkbox_5(self):
        """Reset all controls from checkbox 5 onwards - only disable, don't clear"""
        self.groupBox_2.setEnabled(False)
        self.reset_from_groupbox_2()
    
    def reset_from_groupbox_2(self):
        """Reset all controls from group box 2 onwards - only disable, don't clear"""
        self.checkBox_6.hide()  # Always hide checkbox 6 when resetting
        self.checkBox_6.setEnabled(False)
        self.pushButton_finish.setEnabled(False)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Open the restrictors [Pressure zero on Restrictor]", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Reduce the pump speed to 500 rpm", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Close the Bottom exit port seal valve in the MRSC and stop the\n"
"pump when Pump Output Pressure (PMPPRES) reaches 2000 psi", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Check for pressure drop and leaks on the seal valves and in the MRSC", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Are there any leaks ppresent?", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Investigate Leak</span></p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Reverse toggle bit the MRPO twice to prevent any hydraulic pressure to be stored'", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Is HPRESS between 0-200 Psi", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Open MRSC seal valve and check counter 130 +- 8", None))
        self.pushButton_back.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.pushButton_finish.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
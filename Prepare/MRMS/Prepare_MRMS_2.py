from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1018, 430)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_1 = QCheckBox(self.frame_7)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_1)

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

        self.verticalLayout_6.addWidget(self.checkBox_2)

        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(410, 270))
        self.label.setMaximumSize(QSize(410, 270))
        self.label.setPixmap(QPixmap(resource_path("Icons/Img_16.png")))
        self.label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(41, 41))
        self.label_12.setMaximumSize(QSize(41, 41))
        self.label_12.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_12.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_12)

        self.groupBox_1 = QGroupBox(self.frame_2)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(400, 0))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_1 = QRadioButton(self.groupBox_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.groupBox_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_2)


        self.horizontalLayout.addWidget(self.groupBox_1)


        self.verticalLayout.addWidget(self.frame_2)

        self.checkBox_3 = QCheckBox(self.frame)
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

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(41, 41))
        self.label_13.setMaximumSize(QSize(41, 41))
        self.label_13.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_13)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(400, 0))
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_4)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout.addWidget(self.frame_3)

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

        self.verticalLayout.addWidget(self.checkBox_4)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)


        self.retranslateUi(Dialog)
        
        # Initialize sequential logic
        self.setup_sequential_logic()

        self.pushButton.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Confirm that the MPSRs have installed the blank upper head stabber\n"
"(H433948), blank lower head plug (H708126) and plug nut (H708127)", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Make sure that the blank crossover plug (H730718) and stabber\n"
"(100281268) are available for each bottle, to be installed before rig up", None))
        self.label.setText("")
        self.label_12.setText("")
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Check MRMS Exit port adaptor available in SFT-275 for the Opcheck", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Informed Base", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">For Preparation of Low Shock Sampling, refer InTouch</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Open InTouch", None))
        self.label_13.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Is the Exo washer available?", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Informed Base and Raised the Requirement", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Finish and Move to Next", None))
    # retranslateUi

    def setup_sequential_logic(self):
        """Initialize the sequential logic for the dialog"""
        # Initially disable all elements except checkBox_1
        self.checkBox_2.setEnabled(False)
        self.groupBox_1.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.pushButton.setEnabled(False)
        
        # Keep "Open InTouch" button always enabled
        self.pushButton_2.setEnabled(True)
        
        # Hide risk icons initially
        self.label_12.setVisible(False)
        self.label_13.setVisible(False)
        
        # Connect signals for sequential logic
        self.checkBox_1.stateChanged.connect(self.handle_checkbox1)
        self.checkBox_2.stateChanged.connect(self.handle_checkbox2)
        self.radioButton_1.toggled.connect(self.handle_groupbox1_selection)
        self.radioButton_2.toggled.connect(self.handle_groupbox1_selection)
        self.checkBox_3.stateChanged.connect(self.handle_checkbox3)
        self.radioButton_3.toggled.connect(self.handle_groupbox2_selection)
        self.radioButton_4.toggled.connect(self.handle_groupbox2_selection)
        self.checkBox_4.stateChanged.connect(self.handle_checkbox4)
    
    def handle_checkbox1(self):
        """CB1 checked → enable CB2"""
        if self.checkBox_1.isChecked():
            self.checkBox_2.setEnabled(True)
        else:
            # Reset everything if CB1 is unchecked
            self.checkBox_2.setEnabled(False)
            self.checkBox_2.setChecked(False)
            self.reset_from_groupbox1()
    
    def handle_checkbox2(self):
        """CB2 checked → enable GB1"""
        if self.checkBox_2.isChecked():
            self.groupBox_1.setEnabled(True)
        else:
            # Reset everything from GB1 onwards
            self.reset_from_groupbox1()
    
    def handle_groupbox1_selection(self):
        """GB1 selection: Yes → GB2, No → CB3"""
        if self.radioButton_1.isChecked():  # Yes selected
            # Enable GB2 directly
            self.groupBox_2.setEnabled(True)
            # Disable CB3 path
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            # label_12 visibility matches CB3 enablement
            self.label_12.setVisible(False)
        elif self.radioButton_2.isChecked():  # No selected
            # Enable CB3, disable GB2 until CB3 is checked
            self.checkBox_3.setEnabled(True)
            # label_12 visibility matches CB3 enablement
            self.label_12.setVisible(True)
            self.groupBox_2.setEnabled(False)
            self.reset_from_groupbox2()
        else:
            # No selection, reset from GB1
            self.reset_from_groupbox1()
    
    def handle_checkbox3(self):
        """CB3 checked → enable GB2 (only when No was selected in GB1)"""
        if self.checkBox_3.isChecked() and self.radioButton_2.isChecked():
            self.groupBox_2.setEnabled(True)
        else:
            # Reset from GB2
            self.reset_from_groupbox2()
    
    def handle_groupbox2_selection(self):
        """GB2 selection: Yes → pushButton, No → CB4"""
        if self.radioButton_3.isChecked():  # Yes selected
            # Enable pushButton directly
            self.pushButton.setEnabled(True)
            # Disable CB4 path
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            # label_13 visibility matches CB4 enablement
            self.label_13.setVisible(False)
        elif self.radioButton_4.isChecked():  # No selected
            # Enable CB4, disable pushButton until CB4 is checked
            self.checkBox_4.setEnabled(True)
            # label_13 visibility matches CB4 enablement
            self.label_13.setVisible(True)
            self.pushButton.setEnabled(False)
        else:
            # No selection, reset from GB2
            self.reset_from_groupbox2()
    
    def handle_checkbox4(self):
        """CB4 checked → enable pushButton (only when No was selected in GB2)"""
        if self.checkBox_4.isChecked() and self.radioButton_4.isChecked():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
    
    def reset_from_groupbox1(self):
        """Reset all elements from GB1 onwards"""
        self.groupBox_1.setEnabled(False)
        self.radioButton_1.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setChecked(False)
        # label_12 visibility matches CB3 enablement
        self.label_12.setVisible(False)
        self.reset_from_groupbox2()
    
    def reset_from_groupbox2(self):
        """Reset all elements from GB2 onwards"""
        self.groupBox_2.setEnabled(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setChecked(False)
        # label_13 visibility matches CB4 enablement
        self.label_13.setVisible(False)
        self.pushButton.setEnabled(False)
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(608, 448)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Radio_Frame_4 = QFrame(self.groupBox_4)
        self.Radio_Frame_4.setObjectName(u"Radio_Frame_4")
        self.Radio_Frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Radio_Frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Radio_Frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.radioButton_10 = QRadioButton(self.Radio_Frame_4)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.Radio_Frame_4)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_8.addWidget(self.radioButton_11)


        self.verticalLayout_7.addWidget(self.Radio_Frame_4)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.verticalLayout_4.addWidget(self.checkBox_1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(570, 130))
        self.label.setMaximumSize(QSize(570, 130))
        self.label.setPixmap(QPixmap(resource_path("Icons/Img_22.png")))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_2 = QCheckBox(self.frame_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_2)


        self.verticalLayout_2.addWidget(self.frame_3)

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


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"22-Socket Pin", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"No damage at surface", None))
        self.radioButton_11.setText(QCoreApplication.translate("Dialog", u"Rederessed/Replaced damaged parts", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Drain Plug is installed", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Rest all resistances are &gt; 20M</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"All the resistances are according to guide", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
        
        self.initialize_progressive_form()

        self.setup_progressive_signals()
    # retranslateUi

    def initialize_progressive_form(self):
        """Initialize the progressive form - disable elements until previous steps are completed"""
        self.frame_2.setEnabled(False)  # Disable first checkbox
        self.frame.setEnabled(False)    # Disable image frame
        self.frame_3.setEnabled(False)  # Disable second checkbox
        self.pushButton.setEnabled(False)  # Disable push button
    
    def setup_progressive_signals(self):
        """Setup signal connections for progressive form logic"""
        # Radio button selections enable first checkbox
        self.radioButton_10.toggled.connect(self.handle_groupbox_selection)
        self.radioButton_11.toggled.connect(self.handle_groupbox_selection)
        
        # First checkbox enables image frame
        self.checkBox_1.toggled.connect(self.handle_first_checkbox)
        
        # Second checkbox enables push button
        self.checkBox_2.toggled.connect(self.handle_second_checkbox)
    
    def handle_groupbox_selection(self):
        """Handle groupbox radio button selection"""
        # In a radio button group, once a selection is made, one will always be selected
        # unless manually cleared by code, so the else branch may rarely execute
        if self.radioButton_10.isChecked() or self.radioButton_11.isChecked():
            # Any radio button selected - enable first checkbox
            self.frame_2.setEnabled(True)
        else:
            # No radio button selected - reset the entire form progression
            self.frame_2.setEnabled(False)
            self.frame.setEnabled(False)
            self.frame_3.setEnabled(False)
            self.pushButton.setEnabled(False)
            
            # Reset checkbox states
            if self.checkBox_1.isChecked():
                self.checkBox_1.setChecked(False)
            if self.checkBox_2.isChecked():
                self.checkBox_2.setChecked(False)
    
    def handle_first_checkbox(self):
        """Handle first checkbox selection"""
        if self.checkBox_1.isChecked():
            # First checkbox checked - enable image frame first
            self.frame.setEnabled(True)
            # Then enable the second checkbox frame
            self.frame_3.setEnabled(True)
        else:
            # First checkbox unchecked - disable subsequent elements
            self.frame.setEnabled(False)
            self.frame_3.setEnabled(False)
            self.pushButton.setEnabled(False)
            # Reset second checkbox state
            self.checkBox_2.setChecked(False)
    
    def handle_second_checkbox(self):
        """Handle second checkbox selection"""
        if self.checkBox_2.isChecked():
            # Second checkbox checked - enable push button
            self.pushButton.setEnabled(True)
        else:
            # Second checkbox unchecked - disable push button
            self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(562, 392)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(80, 25))
        self.lineEdit_2.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_5.addWidget(self.lineEdit_2)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(80, 25))
        self.lineEdit_4.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_6.addWidget(self.lineEdit_4)


        self.horizontalLayout_11.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_18 = QFrame(Dialog)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(41, 41))
        self.label_20.setMaximumSize(QSize(41, 41))
        self.label_20.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_18.addWidget(self.label_21)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_1 = QCheckBox(self.groupBox)
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

        self.groupBox_1 = QGroupBox(self.groupBox)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
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


        self.verticalLayout.addWidget(self.groupBox_1)

        self.checkBox_4 = QCheckBox(self.groupBox)
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

        self.checkBox_3 = QCheckBox(self.groupBox)
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


        self.verticalLayout_2.addWidget(self.groupBox)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        # Initially disable all controls except the first checkbox
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.checkBox_1.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_1.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.pushButton.setEnabled(False)

        # Hide error frame and checkBox_4 initially
        self.frame_18.hide()
        self.checkBox_4.hide()

        # Connect signals for sequential validation
        self.checkBox_2.stateChanged.connect(self.check_checkbox_2_for_line_edits)
        self.lineEdit_2.textChanged.connect(self.check_line_edits_2_4)
        self.lineEdit_4.textChanged.connect(self.check_line_edits_2_4)
        self.checkBox_1.stateChanged.connect(self.check_checkbox_1_for_groupbox)
        self.radioButton_2.toggled.connect(self.check_groupbox_1_selection)
        self.radioButton_1.toggled.connect(self.check_groupbox_1_selection)
        self.checkBox_4.stateChanged.connect(self.check_checkbox_4_for_checkbox_3)
        self.checkBox_3.stateChanged.connect(self.check_checkbox_3_for_button)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def check_checkbox_2_for_line_edits(self):
        """Enable line edits when checkBox_2 is checked"""
        if self.checkBox_2.isChecked():
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
        else:
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            self.frame_18.hide()
            # Reset subsequent controls
            self.checkBox_1.setEnabled(False)
            self.checkBox_1.setChecked(False)

    def check_line_edits_2_4(self):
        """Check if line edits 2 and 4 have values >= 3100 to enable checkBox_1 or show error frame"""
        try:
            val2 = float(self.lineEdit_2.text()) if self.lineEdit_2.text().strip() else None
            val4 = float(self.lineEdit_4.text()) if self.lineEdit_4.text().strip() else None
            
            if val2 is not None and val4 is not None:
                if val2 >= 3100 and val4 >= 3100:
                    self.checkBox_1.setEnabled(True)
                    self.frame_18.hide()
                else:
                    self.checkBox_1.setEnabled(False)
                    self.checkBox_1.setChecked(False)
                    self.frame_18.show()
            else:
                self.checkBox_1.setEnabled(False)
                self.checkBox_1.setChecked(False)
                self.frame_18.hide()
        except ValueError:
            self.checkBox_1.setEnabled(False)
            self.checkBox_1.setChecked(False)
            self.frame_18.hide()

    def check_checkbox_1_for_groupbox(self):
        """Enable groupBox_1 when checkBox_1 is checked"""
        if self.checkBox_1.isChecked():
            self.radioButton_2.setEnabled(True)
            self.radioButton_1.setEnabled(True)
        else:
            self.radioButton_2.setEnabled(False)
            self.radioButton_1.setEnabled(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_1.setChecked(False)
            # Reset subsequent controls
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_4.hide()
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.pushButton.setEnabled(False)

    def check_groupbox_1_selection(self):
        """Handle Yes/No selection in groupBox_1"""
        if self.radioButton_1.isChecked():  # Yes selected
            self.checkBox_4.hide()
            self.checkBox_4.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_3.setEnabled(True)
        elif self.radioButton_2.isChecked():  # No selected
            self.checkBox_4.show()
            self.checkBox_4.setEnabled(True)
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.pushButton.setEnabled(False)

    def check_checkbox_4_for_checkbox_3(self):
        """Enable checkBox_3 when checkBox_4 is checked (only for No path)"""
        if self.checkBox_4.isChecked():
            self.checkBox_3.setEnabled(True)
        else:
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.pushButton.setEnabled(False)

    def check_checkbox_3_for_button(self):
        """Enable push button when checkBox_3 is checked"""
        if self.checkBox_3.isChecked():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Opened the ISO Valve", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Set Line Pressure</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hydraulic Pressure</span></p></body></html>", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Pressure must be above 3100 Psi</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Checking the Pump Functionality", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Connect the bottle fill tank to the probe barrel", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Are you using MPMP", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Connect two bottles to each of the air \n"
"adapter (100298189, 150 psi rating) inlets", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Install the restrictor into the top/bottom exit port,\n"
"and then confirm that the restrictor is open", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Finish", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
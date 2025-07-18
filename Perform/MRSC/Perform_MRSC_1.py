from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(617, 517)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 25))
        self.comboBox.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(41, 41))
        self.label_23.setMaximumSize(QSize(41, 41))
        self.label_23.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_23)

        self.checkBox_1 = QCheckBox(self.frame_5)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 20px; /* Larger text */\n"
"	font-weight: bold;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.horizontalLayout_5.addWidget(self.checkBox_1)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 0))
        self.lineEdit_6.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_6)


        self.verticalLayout.addWidget(self.frame)

        self.frame_15 = QFrame(Dialog)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(41, 41))
        self.label_17.setMaximumSize(QSize(41, 41))
        self.label_17.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_16.addWidget(self.label_18)


        self.verticalLayout.addWidget(self.frame_15)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.lineEdit_7 = QLineEdit(self.frame_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 0))
        self.lineEdit_7.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_7)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_16 = QFrame(Dialog)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.label_19 = QLabel(self.frame_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(41, 41))
        self.label_19.setMaximumSize(QSize(41, 41))
        self.label_19.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_19.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_17.addWidget(self.label_20)


        self.verticalLayout.addWidget(self.frame_16)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.lineEdit_8 = QLineEdit(self.frame_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 0))
        self.lineEdit_8.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_8)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_17 = QFrame(Dialog)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(41, 41))
        self.label_21.setMaximumSize(QSize(41, 41))
        self.label_21.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_17)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_18.addWidget(self.label_22)


        self.verticalLayout.addWidget(self.frame_17)

        self.frame_14 = QFrame(Dialog)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setSpacing(15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(41, 41))
        self.label_15.setMaximumSize(QSize(41, 41))
        self.label_15.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_15.addWidget(self.label_16)


        self.verticalLayout.addWidget(self.frame_14)

        self.frame_28 = QFrame(Dialog)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_28)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_28)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_28)


        self.retranslateUi(Dialog)

        # Initial state: disable all line edits and push button, hide only error frames
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.pushButton.setEnabled(False)
        
        # Hide only error frames initially
        self.frame_15.hide()
        self.frame_16.hide()
        self.frame_17.hide()

        def update_frames_visibility():
            # Enable lineEdit_6 only if valid option selected (index > 0) and checkbox checked
            idx = self.comboBox.currentIndex()
            checkbox_checked = self.checkBox_1.isChecked()
            
            if idx > 0 and checkbox_checked:
                self.lineEdit_6.setEnabled(True)
                # Re-check lineEdit_7 to update lineEdit_8 state based on new combo selection
                check_lineEdit_7()
            else:
                # Disable all controls and clear them
                self.lineEdit_6.setEnabled(False)
                self.lineEdit_6.clear()
                self.lineEdit_7.setEnabled(False)
                self.lineEdit_7.clear()
                self.lineEdit_8.setEnabled(False)
                self.lineEdit_8.clear()
                self.pushButton.setEnabled(False)
                
                # Hide error frames when conditions not met
                self.frame_15.hide()
                self.frame_16.hide()
                self.frame_17.hide()

        def check_lineEdit_6():
            try:
                val = float(self.lineEdit_6.text())
                is_acceptable = 122 <= val <= 138
                
                if is_acceptable:
                    self.frame_15.hide()
                    self.lineEdit_7.setEnabled(True)
                else:
                    self.frame_15.show()
                    self.lineEdit_7.setEnabled(False)
                    self.lineEdit_7.clear()
                    self.lineEdit_8.setEnabled(False)
                    self.lineEdit_8.clear()
                    self.pushButton.setEnabled(False)
                    
            except ValueError:
                self.frame_15.hide()
                self.lineEdit_7.setEnabled(False)
                self.lineEdit_7.clear()
                self.lineEdit_8.setEnabled(False)
                self.lineEdit_8.clear()
                self.pushButton.setEnabled(False)

        def check_lineEdit_7():
            try:
                val = float(self.lineEdit_7.text())
                is_acceptable = -5 <= val <= 5
                
                if is_acceptable:
                    self.frame_16.hide()
                    # Check if lineEdit_8 should be enabled based on combo selection
                    idx = self.comboBox.currentIndex()
                    if idx == 3:  # Exit Port - enable lineEdit_8
                        self.lineEdit_8.setEnabled(True)
                    else:  # Low Shock or Water Receptacle - enable pushButton directly
                        self.lineEdit_8.setEnabled(False)
                        self.lineEdit_8.clear()
                        self.pushButton.setEnabled(True)
                else:
                    self.frame_16.show()
                    self.lineEdit_8.setEnabled(False)
                    self.lineEdit_8.clear()
                    self.pushButton.setEnabled(False)
                    
            except ValueError:
                self.frame_16.hide()
                self.lineEdit_8.setEnabled(False)
                self.lineEdit_8.clear()
                self.pushButton.setEnabled(False)

        def check_lineEdit_8():
            try:
                val = float(self.lineEdit_8.text())
                is_acceptable = 122 <= val <= 138
                
                if is_acceptable:
                    self.frame_17.hide()
                    self.pushButton.setEnabled(True)
                else:
                    self.frame_17.show()
                    self.pushButton.setEnabled(False)
                    
            except ValueError:
                self.frame_17.hide()
                self.pushButton.setEnabled(False)

        # Connect signals
        self.checkBox_1.toggled.connect(update_frames_visibility)
        self.comboBox.currentIndexChanged.connect(update_frames_visibility)
        self.lineEdit_6.textChanged.connect(check_lineEdit_6)
        self.lineEdit_7.textChanged.connect(check_lineEdit_7)
        self.lineEdit_8.textChanged.connect(check_lineEdit_8)
        
        # Initial setup
        update_frames_visibility()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select MRSC Type", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Low Shock", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Water Receptacle", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Exit Port", None))

        self.label_23.setText("")
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Close seal valve and reset valve position (SVLVPOS=0)", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Open seal Valve</span></p></body></html>", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Open seal Valve Value must be between 122 to 138</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Close seal Valve</span></p></body></html>", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Open seal Valve Value must be between -5 to 5</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Open seal Valve</span></p></body></html>", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Open seal Valve Value must be between 122 to 138</span></p></body></html>", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Keep OPEN till Guard PO Initialize and Mode set</span></p></body></html>", None))
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

class Perform_MRSC_1(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.accept)
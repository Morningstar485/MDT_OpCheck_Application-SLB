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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(579, 465)
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


        self.verticalLayout.addWidget(self.frame_4)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(470, 200))
        self.label.setMaximumSize(QSize(470, 200))
        self.label.setPixmap(QPixmap(resource_path("Icons/Img_11.png")))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)  # Initially disabled for progressive workflow
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
        self.checkBox_3.setEnabled(False)  # Initially disabled for progressive workflow
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

        # Initialize progressive form and connect signals
        self.initialize_progressive_form()
        self.connect_signals()

        self.retranslateUi(Dialog)
        self.pushButton.hide()


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Confirm that oil level is full by checking if the compensator piston\n"
"is fully back and 3 springs turns are visible in the mud hole", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Note</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">If the compensator piston is not visible in the mud hole, MRPO requires oil top up</span></p></body></html>", None))
        self.label.setText("")
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Make sure the compensator pistons are clean and not stuck. The compensator\n"
"piston moves and spring compresses as oil is being topped off", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Flush the compensator section on MRPO with DC-111", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

    def initialize_progressive_form(self):
        """Initialize the progressive form with sequential checkbox workflow"""
        # Enable only first checkbox, disable others
        self.checkBox_1.setEnabled(True)
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        
        # Disable Next button initially
        self.pushButton.setEnabled(False)

    def connect_signals(self):
        """Connect checkbox signals for progressive workflow"""
        self.checkBox_1.stateChanged.connect(self.handle_checkbox1)
        self.checkBox_2.stateChanged.connect(self.handle_checkbox2)
        self.checkBox_3.stateChanged.connect(self.handle_checkbox3)

    def handle_checkbox1(self, state):
        """Handle checkbox 1 state change - enable checkbox 2 when checked"""
        if state == 2:  # Checked
            self.checkBox_2.setEnabled(True)
        else:  # Unchecked
            # Reset subsequent checkboxes when checkbox 1 is unchecked
            self.checkBox_2.setEnabled(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.pushButton.setEnabled(False)

    def handle_checkbox2(self, state):
        """Handle checkbox 2 state change - enable checkbox 3 when checked"""
        if state == 2:  # Checked
            self.checkBox_3.setEnabled(True)
        else:  # Unchecked
            # Reset subsequent checkboxes when checkbox 2 is unchecked
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.pushButton.setEnabled(False)

    def handle_checkbox3(self, state):
        """Handle checkbox 3 state change - enable Next button when checked"""
        if state == 2:  # Checked
            self.pushButton.setEnabled(True)
        else:  # Unchecked
            self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
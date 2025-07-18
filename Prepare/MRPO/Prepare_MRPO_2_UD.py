from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(530, 190)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_1 = QCheckBox(Dialog)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(True)  # First checkbox starts enabled
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

        # Initialize progressive form - simple sequential workflow
        self.initialize_progressive_form()
        
        # Connect checkbox signals for progressive logic
        self.checkBox_1.stateChanged.connect(self.handle_checkbox1)
        self.checkBox_2.stateChanged.connect(self.handle_checkbox2)
        self.checkBox_3.stateChanged.connect(self.handle_checkbox3)
        
        # Connect button signals - InTouch button always available
        self.pushButton.clicked.connect(self.open_link)

        self.retranslateUi(Dialog)
        
        self.pushButton_2.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Set the MRPO to run in the Up/Down mode", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Confirm the drain plug (H217193) with O-ring (B013118) is installed", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Verify that the manual 3-way flowline valve is set for Up/Down operations", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Check Configuration from InTouch", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

    def open_link(self):
        QDesktopServices.openUrl(QUrl("https://intouchsupport.com/index.cfm?event=content.preview&contentId=7033048&FromRefPage=Y"))

    def initialize_progressive_form(self):
        """Initialize the progressive form with sequential checkbox workflow"""
        # Enable only first checkbox, disable others
        self.checkBox_1.setEnabled(True)
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        
        # Disable Next button initially (only controlled by progressive logic)
        self.pushButton_2.setEnabled(False)
        
        # InTouch button remains always enabled - not part of progressive workflow
        self.pushButton.setEnabled(True)

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
            self.pushButton_2.setEnabled(False)

    def handle_checkbox2(self, state):
        """Handle checkbox 2 state change - enable checkbox 3 when checked"""
        if state == 2:  # Checked
            self.checkBox_3.setEnabled(True)
        else:  # Unchecked
            # Reset subsequent checkboxes when checkbox 2 is unchecked
            self.checkBox_3.setEnabled(False)
            self.checkBox_3.setChecked(False)
            self.pushButton_2.setEnabled(False)

    def handle_checkbox3(self, state):
        """Handle checkbox 3 state change - enable Next button when checked"""
        if state == 2:  # Checked
            self.pushButton_2.setEnabled(True)
        else:  # Unchecked
            self.pushButton_2.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

import os, platform, subprocess
from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(452, 251)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setStyleSheet(u"QPushButton {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

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

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 25))

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)

        self.pushButton.hide()

        self.checkBox_1.toggled.connect(lambda checked: self.pushButton.setVisible(checked))

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Please Carefully Check the </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">SFT Manuals required for the job</span></p></body></html>", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"Open SFT 267 : Common Tools", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Open SFT 275 : MRMS", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Open SFT 273 : PS/PQ CQG", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Open SFT 285 : MRPO", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"All required SFT Tools are in order", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

class SFT_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect each push button to open respective PDFs
        self.ui.pushButton_1.clicked.connect(lambda: self.open_pdf("SFTs/SFT-267.pdf"))
        self.ui.pushButton_2.clicked.connect(lambda: self.open_pdf("SFTs/SFT-273.pdf"))
        self.ui.pushButton_3.clicked.connect(lambda: self.open_pdf("SFTs/SFT-275.pdf"))
        self.ui.pushButton_4.clicked.connect(lambda: self.open_pdf("SFTs/SFT-285.pdf"))

        self.ui.pushButton.clicked.connect(self.accept)  # Next button

    def open_pdf(self, relative_path):
        pdf_path = resource_path(relative_path)

        try:
            if platform.system() == "Windows":
                os.startfile(pdf_path)
            elif platform.system() == "Darwin":
                subprocess.run(["open", pdf_path])
            else:
                subprocess.run(["xdg-open", pdf_path])
        except Exception as e:
            print(f"[Error] Could not open PDF: {e}")
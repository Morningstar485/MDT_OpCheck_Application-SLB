from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(478, 150)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(Dialog)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_1 = QLabel(self.frame_8)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_2.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.frame_8)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(125, 25))
        self.lineEdit_1.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_1)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_9 = QFrame(Dialog)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(125, 25))
        self.lineEdit_2.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_10 = QFrame(Dialog)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(125, 25))
        self.lineEdit_3.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout.addWidget(self.frame_10)

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

        self.frame_13 = QFrame(Dialog)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(41, 41))
        self.label_14.setMaximumSize(QSize(41, 41))
        self.label_14.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout.addWidget(self.frame_13)

        self.frame_14 = QFrame(Dialog)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_9.addWidget(self.label_17)


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
        # Hide error frames initially and disable controls
        self.frame_12.hide()
        self.frame_13.hide()
        self.frame_14.hide()
        
        # Initially only first lineEdit is enabled
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.pushButton.setEnabled(False)

        def check_lineEdit_1():
            try:
                val = float(self.lineEdit_1.text())
                is_acceptable = 5.39 <= val <= 5.61
                self.frame_12.setVisible(not is_acceptable)
                
                # Enable lineEdit_2 only if lineEdit_1 has acceptable value
                self.lineEdit_2.setEnabled(is_acceptable)
                
                # If lineEdit_1 becomes unacceptable, reset subsequent controls
                if not is_acceptable:
                    self.lineEdit_2.clear()
                    self.lineEdit_2.setEnabled(False)
                    self.lineEdit_3.clear()
                    self.lineEdit_3.setEnabled(False)
                    self.pushButton.setEnabled(False)
                    
            except ValueError:
                self.frame_12.setVisible(False)
                self.lineEdit_2.setEnabled(False)
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_3.setEnabled(False)
                self.pushButton.setEnabled(False)
        self.lineEdit_1.textChanged.connect(check_lineEdit_1)
        check_lineEdit_1()

        def check_lineEdit_2():
            try:
                val = float(self.lineEdit_2.text())
                is_acceptable = 14.7 <= val <= 15.3
                self.frame_13.setVisible(not is_acceptable)
                
                # Enable lineEdit_3 only if lineEdit_2 has acceptable value
                self.lineEdit_3.setEnabled(is_acceptable)
                
                # If lineEdit_2 becomes unacceptable, reset subsequent controls
                if not is_acceptable:
                    self.lineEdit_3.clear()
                    self.lineEdit_3.setEnabled(False)
                    self.pushButton.setEnabled(False)
                    
            except ValueError:
                self.frame_13.setVisible(False)
                self.lineEdit_3.setEnabled(False)
                self.lineEdit_3.clear()
                self.pushButton.setEnabled(False)
        self.lineEdit_2.textChanged.connect(check_lineEdit_2)
        check_lineEdit_2()

        def check_lineEdit_3():
            try:
                val = float(self.lineEdit_3.text())
                # For negative range: -15.3 <= val <= -14.7
                is_acceptable = -15.3 <= val <= -14.7
                self.frame_14.setVisible(not is_acceptable)
                
                # Enable pushButton only if lineEdit_3 has acceptable value
                self.pushButton.setEnabled(is_acceptable)
                
            except ValueError:
                self.frame_14.setVisible(False)
                self.pushButton.setEnabled(False)
        self.lineEdit_3.textChanged.connect(check_lineEdit_3)
        check_lineEdit_3()

        self.lineEdit_1.textChanged.connect(check_lineEdit_1)
        self.lineEdit_2.textChanged.connect(check_lineEdit_2)
        self.lineEdit_3.textChanged.connect(check_lineEdit_3)
        
        # Initial checks
        check_lineEdit_1()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">5V Reading</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">+15V Reading</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">-15V Reading</span></p></body></html>", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Value must be between 5.39 and 5.61V</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Value must be between 14.7V and 15.3V</span></p></body></html>", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; color:#ff0000;\">Value must be between -14.7V and -15.3V</span></p></body></html>", None))
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

class Perform_MRPC_1(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.accept)
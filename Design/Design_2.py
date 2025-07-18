from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(451, 313)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_1 = QFrame(Dialog)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_1 = QLabel(self.frame_1)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout_4.addWidget(self.label_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.frame_1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_1)

        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(125, 25))
        self.lineEdit_3.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.pushButton_1 = QPushButton(self.frame_7)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(100, 25))
        self.pushButton_1.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_1)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(160, 25))
        self.comboBox.setMaximumSize(QSize(160, 25))

        self.verticalLayout.addWidget(self.comboBox)


        self.verticalLayout_3.addWidget(self.frame)

        # --- Move this block here, before adding frame_2 ---
        self.dynamicCrewLayout = QVBoxLayout()
        self.dynamicCrewLayout.setObjectName(u"dynamicCrewLayout")
        self.verticalLayout_3.addLayout(self.dynamicCrewLayout)
        # ---------------------------------------------------

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 25))
        self.pushButton_2.setMaximumSize(QSize(1000, 25))

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        # Connect the Update button
        self.pushButton_1.clicked.connect(self.add_crew_rows)

        self.retranslateUi(Dialog)
 
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Input Crew Information</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Please fill out the information of the crew working on the MDT</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Enter the number of personnel working with the toolstring</span></p></body></html>", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Select the Crew Designation</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Engineer", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"TLC SPI", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"VSP SPIL", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Crew Chief", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Operator", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Trainee FE/FS", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"Trainee Operator", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

    def add_crew_rows(self):
        # Clear previous dynamic rows
        while self.dynamicCrewLayout.count():
            item = self.dynamicCrewLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        try:
            num_rows = int(self.lineEdit_3.text())
        except ValueError:
            num_rows = 0

        # Add dynamic combo boxes (excluding the static one)
        for _ in range(max(0, num_rows - 1)):
            frame = QFrame()
            frame.setFrameShape(QFrame.Shape.StyledPanel)
            frame.setFrameShadow(QFrame.Shadow.Raised)
            frame.setContentsMargins(9, 9, 9, 9)
            layout = QVBoxLayout(frame)
            layout.setContentsMargins(0, 0, 0, 0)  # Inner layout, no extra margin

            combo = QComboBox()
            # Add the same items as the static comboBox
            for i in range(self.comboBox.count()):
                combo.addItem(self.comboBox.itemText(i))
            combo.setMinimumSize(self.comboBox.minimumSize())
            combo.setMaximumSize(self.comboBox.maximumSize())
            layout.addWidget(combo)

            self.dynamicCrewLayout.addWidget(frame)




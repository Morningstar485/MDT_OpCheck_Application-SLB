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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(374, 598)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.frame_13 = QFrame(Dialog)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.frame = QFrame(self.frame_13)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.frame)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(130, 0))
        self.lineEdit_1.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_1, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_13)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(130, 0))
        self.lineEdit_2.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(130, 0))
        self.lineEdit_3.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_3, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_13)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(130, 0))
        self.lineEdit_4.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_4, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_27 = QFrame(Dialog)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_27)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.frame_27)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_7 = QFrame(self.frame_27)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.frame_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_27)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.frame_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_9.addWidget(self.lineEdit_7)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.frame_10)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_10.addWidget(self.lineEdit_8)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_27)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.frame_12)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_12.addWidget(self.lineEdit_9)


        self.horizontalLayout_11.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.lineEdit_10 = QLineEdit(self.frame_14)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_15.addWidget(self.lineEdit_10)


        self.horizontalLayout_11.addWidget(self.frame_14)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_15 = QFrame(self.frame_27)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_17.addWidget(self.label_12)

        self.lineEdit_11 = QLineEdit(self.frame_16)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_17.addWidget(self.lineEdit_11)


        self.horizontalLayout_16.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.lineEdit_12 = QLineEdit(self.frame_17)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_18.addWidget(self.lineEdit_12)


        self.horizontalLayout_16.addWidget(self.frame_17)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_21 = QFrame(self.frame_27)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_19 = QLabel(self.frame_22)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_23.addWidget(self.label_19)

        self.lineEdit_13 = QLineEdit(self.frame_22)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_23.addWidget(self.lineEdit_13)


        self.horizontalLayout_22.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_20 = QLabel(self.frame_23)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_24.addWidget(self.label_20)

        self.lineEdit_18 = QLineEdit(self.frame_23)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.horizontalLayout_24.addWidget(self.lineEdit_18)


        self.horizontalLayout_22.addWidget(self.frame_23)


        self.verticalLayout_2.addWidget(self.frame_21)

        self.frame_18 = QFrame(self.frame_27)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_20.addWidget(self.label_17)

        self.lineEdit_16 = QLineEdit(self.frame_19)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.horizontalLayout_20.addWidget(self.lineEdit_16)


        self.horizontalLayout_19.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_21.addWidget(self.label_18)

        self.lineEdit_17 = QLineEdit(self.frame_20)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.horizontalLayout_21.addWidget(self.lineEdit_17)


        self.horizontalLayout_19.addWidget(self.frame_20)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.frame_24 = QFrame(self.frame_27)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_21 = QLabel(self.frame_25)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_26.addWidget(self.label_21)

        self.lineEdit_20 = QLineEdit(self.frame_25)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.horizontalLayout_26.addWidget(self.lineEdit_20)


        self.horizontalLayout_25.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_22 = QLabel(self.frame_26)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_27.addWidget(self.label_22)

        self.lineEdit_21 = QLineEdit(self.frame_26)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.horizontalLayout_27.addWidget(self.lineEdit_21)


        self.horizontalLayout_25.addWidget(self.frame_26)


        self.verticalLayout_2.addWidget(self.frame_24)


        self.verticalLayout_3.addWidget(self.frame_27)

        self.frame_28 = QFrame(Dialog)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_28)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.frame_28)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_28)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.setEnabled(False)
        self.pushButton.hide()
        # Only after all line edits have an input, should the push button be enabled
        def all_lineedits_filled():
            edits = [
                self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
                self.lineEdit_5, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8,
                self.lineEdit_9, self.lineEdit_10, self.lineEdit_11, self.lineEdit_12,
                self.lineEdit_13, self.lineEdit_18, self.lineEdit_16, self.lineEdit_17,
                self.lineEdit_20, self.lineEdit_21
            ]
            return all(e.text().strip() for e in edits)

        def update_pushButton_state():
            self.pushButton.setEnabled(all_lineedits_filled())

        for edit in [
            self.lineEdit_1, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
            self.lineEdit_5, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8,
            self.lineEdit_9, self.lineEdit_10, self.lineEdit_11, self.lineEdit_12,
            self.lineEdit_13, self.lineEdit_18, self.lineEdit_16, self.lineEdit_17,
            self.lineEdit_20, self.lineEdit_21
        ]:
            edit.textChanged.connect(update_pushButton_state)
        update_pushButton_state()
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Operation Details</span></p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Engineer Name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Specialist Name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cable Length</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cable Type</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Resistance Values at Surface Latch</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">1 - 4</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">1 - 10</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">2 - 3</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">2 - 10</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">2 - 5</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">3 - 10</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">2 - 6</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">4 - 10</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">3 - 5</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">5 - 10</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">3 - 6</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">6 - 10</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">5 - 6</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">7 - 10</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
    # retranslateUi

# from .Perform_Admin_2 import Perform_Admin_2

# class Perform_Admin_1(QDialog):
#     def __init__(self, child_metadata=None, admin_metadata=None):
#         super().__init__()
#         self.child_metadata = child_metadata
#         self.admin_metadata = admin_metadata

#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)

#         self.ui.pushButton.clicked.connect(self.next_step)

#     def next_step(self):
#         # Collect all relevant user input directly into self.child_metadata (flat dict)
#         ui = self.ui
#         if self.child_metadata is None:
#             self.child_metadata = {}
#         self.child_metadata['Engineer Name'] = ui.lineEdit_1.text()
#         self.child_metadata['Specialist Name'] = ui.lineEdit_2.text()

#         if self.admin_metadata and 'Well Name' in self.admin_metadata:
#             self.child_metadata['Well Name'] = self.admin_metadata['Well Name']

#         self.child_metadata['Cable Length'] = ui.lineEdit_3.text()
#         self.child_metadata['Cable Type'] = ui.lineEdit_4.text()

#         if self.admin_metadata and 'Rig Name' in self.admin_metadata:
#             self.child_metadata['Rig Name'] = self.admin_metadata['Rig Name']
#         # Group resistance values under a heading
#         resistance_values = {
#             '1 - 4': ui.lineEdit_5.text(),
#             '1 - 10': ui.lineEdit_6.text(),
#             '2 - 3': ui.lineEdit_7.text(),
#             '2 - 10': ui.lineEdit_8.text(),
#             '2 - 5': ui.lineEdit_9.text(),
#             '3 - 10': ui.lineEdit_10.text(),
#             '2 - 6': ui.lineEdit_11.text(),
#             '4 - 10': ui.lineEdit_12.text(),
#             '3 - 5': ui.lineEdit_13.text(),
#             '5 - 10': ui.lineEdit_18.text(),
#             '3 - 6': ui.lineEdit_16.text(),
#             '6 - 10': ui.lineEdit_17.text(),
#             '5 - 6': ui.lineEdit_20.text(),
#             '7 - 10': ui.lineEdit_21.text(),
#         }

#         self.child_metadata['Resistance Values at Surface Latch'] = resistance_values

#         dialog2 = Perform_Admin_2(self.child_metadata, self.admin_metadata)
#         if dialog2.exec() == QDialog.Accepted:
#             self.accept()  # ✅ Close this dialog and continue chain

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
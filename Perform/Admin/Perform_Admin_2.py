from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(906, 400)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_1 = QCheckBox(self.frame)
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

        self.frame_8 = QFrame(self.frame)
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

        self.frame_9 = QFrame(self.frame)
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

        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.frame_10 = QFrame(self.frame)
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

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(125, 25))
        self.lineEdit_4.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_5.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.frame_12)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(125, 25))
        self.lineEdit_5.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_6.addWidget(self.lineEdit_5)


        self.verticalLayout.addWidget(self.frame_12)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(41, 41))
        self.label_12.setMaximumSize(QSize(41, 41))
        self.label_12.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)


        self.verticalLayout.addWidget(self.frame_13)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.frame_14)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(125, 25))
        self.lineEdit_6.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_9.addWidget(self.lineEdit_6)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEdit_7 = QLineEdit(self.frame_15)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(125, 25))
        self.lineEdit_7.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_10.addWidget(self.lineEdit_7)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.frame_16)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(125, 25))
        self.lineEdit_8.setMaximumSize(QSize(125, 25))

        self.horizontalLayout_11.addWidget(self.lineEdit_8)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_5 = QRadioButton(self.groupBox_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_14.addWidget(self.radioButton_6)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(41, 41))
        self.label_14.setMaximumSize(QSize(41, 41))
        self.label_14.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)


        self.verticalLayout_2.addWidget(self.frame_17)

        self.checkBox_3 = QCheckBox(self.frame_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.radioButton_7 = QRadioButton(self.groupBox_4)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.groupBox_4)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.radioButton_8)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)


        self.verticalLayout_2.addWidget(self.frame_18)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        self.checkBox_2.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.groupBox_3.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.groupBox_4.setEnabled(False)

        self.frame_8.setEnabled(False)
        self.frame_9.setEnabled(False)
        self.frame_10.setEnabled(False)
        self.frame_11.setEnabled(False)
        self.frame_12.setEnabled(False)
        self.frame_13.hide()
        self.frame_14.setEnabled(False)
        self.frame_15.setEnabled(False)
        self.frame_16.setEnabled(False)
        self.frame_17.hide()
        self.frame_18.hide()
        self.pushButton.setEnabled(False)

        # checking checkBox_1 enables frame_8
        self.checkBox_1.toggled.connect(self.handle_checkbox1_change)
        self.handle_checkbox1_change()

        # filling data in lineEdit_1 (frame_8) enables frame_9
        def update_frame9_enabled():
            enabled = bool(self.lineEdit_1.text().strip()) and self.frame_8.isEnabled()
            self.frame_9.setEnabled(enabled)
            if not enabled:
                self.reset_from_frame9()
            else:
                # Re-check subsequent elements when this becomes enabled
                update_checkbox2_enabled()
        self._update_frame9_enabled = update_frame9_enabled
        self.lineEdit_1.textChanged.connect(update_frame9_enabled)
        update_frame9_enabled()

        # filling data in lineEdit_2 (frame_9) enables checkBox_2
        def update_checkbox2_enabled():
            enabled = bool(self.lineEdit_2.text().strip()) and self.frame_9.isEnabled()
            self.checkBox_2.setEnabled(enabled)
            if not enabled:
                self.reset_from_checkbox2()
            else:
                # Re-check subsequent elements when this becomes enabled
                self.handle_checkbox2_change()
        self._update_checkbox2_enabled = update_checkbox2_enabled
        self.lineEdit_2.textChanged.connect(update_checkbox2_enabled)
        update_checkbox2_enabled()

        # checking checkBox_2 enables frame_10
        self.checkBox_2.toggled.connect(self.handle_checkbox2_change)
        self.handle_checkbox2_change()

        # filling lineEdit_3 (frame_10) enables frame_11
        def update_frame11_enabled():
            enabled = bool(self.lineEdit_3.text().strip()) and self.frame_10.isEnabled()
            self.frame_11.setEnabled(enabled)
            if not enabled:
                self.reset_from_frame11()
            else:
                # Re-check subsequent elements when this becomes enabled
                update_frame12_enabled()
        self._update_frame11_enabled = update_frame11_enabled
        self.lineEdit_3.textChanged.connect(update_frame11_enabled)
        update_frame11_enabled()

        # filling lineEdit_4 (frame_11) enables frame_12
        def update_frame12_enabled():
            enabled = bool(self.lineEdit_4.text().strip()) and self.frame_11.isEnabled()
            self.frame_12.setEnabled(enabled)
            if not enabled:
                self.reset_from_frame12()
            else:
                # Re-check subsequent elements when this becomes enabled
                update_groupbox2_enabled()
        self._update_frame12_enabled = update_frame12_enabled
        self.lineEdit_4.textChanged.connect(update_frame12_enabled)
        update_frame12_enabled()

        # filling lineEdit_5 (frame_12) enables groupBox_2
        def update_groupbox2_enabled():
            enabled = bool(self.lineEdit_5.text().strip()) and self.frame_12.isEnabled()
            self.groupBox_2.setEnabled(enabled)
            if not enabled:
                self.reset_from_groupbox2()
            else:
                # Re-check radio button states when this becomes enabled
                self.handle_radiobutton3_change()
                self.handle_radiobutton4_change()
        self._update_groupbox2_enabled = update_groupbox2_enabled
        self.lineEdit_5.textChanged.connect(update_groupbox2_enabled)
        update_groupbox2_enabled()

        # selecting radioButton_3 enables frame_14, radioButton_4 shows frame_13
        self.radioButton_3.toggled.connect(self.handle_radiobutton3_change)
        self.radioButton_4.toggled.connect(self.handle_radiobutton4_change)

        # filling line edit of frame_14 enables frame_15
        def update_frame15_enabled():
            enabled = bool(self.lineEdit_6.text().strip()) and self.frame_14.isEnabled()
            self.frame_15.setEnabled(enabled)
            if not enabled:
                self.reset_from_frame15()
            else:
                # Re-check subsequent elements when this becomes enabled
                update_frame16_enabled()
        self._update_frame15_enabled = update_frame15_enabled
        self.lineEdit_6.textChanged.connect(update_frame15_enabled)
        update_frame15_enabled()

        # filling line edit of frame_15 enables frame_16
        def update_frame16_enabled():
            enabled = bool(self.lineEdit_7.text().strip()) and self.frame_15.isEnabled()
            self.frame_16.setEnabled(enabled)
            if not enabled:
                self.reset_from_frame16()
            else:
                # Re-check subsequent elements when this becomes enabled
                update_groupbox3_enabled()
        self._update_frame16_enabled = update_frame16_enabled
        self.lineEdit_7.textChanged.connect(update_frame16_enabled)
        update_frame16_enabled()

        # filling line edit of frame_16 enables groupBox_3
        def update_groupbox3_enabled():
            enabled = bool(self.lineEdit_8.text().strip()) and self.frame_16.isEnabled()
            self.groupBox_3.setEnabled(enabled)
            if not enabled:
                self.reset_from_groupbox3()
            else:
                # Re-check radio button states when this becomes enabled
                self.handle_radiobutton5_change()
                self.handle_radiobutton6_change()
        self._update_groupbox3_enabled = update_groupbox3_enabled
        self.lineEdit_8.textChanged.connect(update_groupbox3_enabled)
        update_groupbox3_enabled()

        # selecting radioButton_5 enables checkBox_3, radioButton_6 shows frame_17
        self.radioButton_5.toggled.connect(self.handle_radiobutton5_change)
        self.radioButton_6.toggled.connect(self.handle_radiobutton6_change)

        # checking checkBox_3 enables groupBox_4
        self.checkBox_3.toggled.connect(self.handle_checkbox3_change)
        self.handle_checkbox3_change()

        # selecting radioButton_7 enables pushButton, radioButton_8 shows frame_18
        self.radioButton_7.toggled.connect(self.handle_radiobutton7_change)
        self.radioButton_8.toggled.connect(self.handle_radiobutton8_change)

        self.pushButton.hide()

        QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Connected all tools as per job planned", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Maxwell Version</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Patch ID</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Declare toolstring in Maxwell and power up Head voltage", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">DH Voltage</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Downhole Current</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">EDTC HV</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Passing Successful?", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Try again with HV Power Down </span></p><p><span style=\" font-size:16pt; font-style:italic;\">and Again Powering UP</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">50 V Power Up</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PPUC Value</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PPUV Value</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"EDTC Before and after gamma ray calibration  passed", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Please do the task again</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Start Station log with selecting \u201cSampling\u201d in station Objective", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Check ACOM passing for SG/CQG and MRFA", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_8.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Do the ACOM Task Again and check</span></p><p><span style=\" font-size:16pt; font-style:italic;\">If still not passing, Recycle Power</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Finish and Next", None))
    # retranslateUi

    def handle_checkbox1_change(self):
        """Handle checkBox_1 changes and cascade effects"""
        enabled = self.checkBox_1.isChecked()
        self.frame_8.setEnabled(enabled)
        if not enabled:
            self.reset_from_frame8()
        else:
            # Re-check subsequent elements when this becomes enabled
            if hasattr(self, '_update_frame9_enabled'):
                self._update_frame9_enabled()
    
    def handle_checkbox2_change(self):
        """Handle checkBox_2 changes and cascade effects"""
        enabled = self.checkBox_2.isChecked() and self.checkBox_2.isEnabled()
        self.frame_10.setEnabled(enabled)
        if not enabled:
            self.reset_from_frame10()
        else:
            # Re-check subsequent elements when this becomes enabled
            if hasattr(self, '_update_frame11_enabled'):
                self._update_frame11_enabled()
    
    def handle_radiobutton3_change(self):
        """Handle radioButton_3 changes and cascade effects"""
        enabled = self.radioButton_3.isChecked() and self.groupBox_2.isEnabled()
        self.frame_14.setEnabled(enabled)
        if not enabled:
            self.reset_from_frame14()
        else:
            # Re-check subsequent elements when this becomes enabled
            if hasattr(self, '_update_frame15_enabled'):
                self._update_frame15_enabled()
        # Hide frame_13 when radioButton_3 is selected
        if self.radioButton_3.isChecked():
            self.frame_13.setVisible(False)
    
    def handle_radiobutton4_change(self):
        """Handle radioButton_4 changes and show frame_13"""
        if self.radioButton_4.isChecked() and self.groupBox_2.isEnabled():
            self.frame_13.setVisible(True)
            # Reset the right column when taking the "No" path
            self.reset_from_frame14()
        else:
            self.frame_13.setVisible(False)
    
    def handle_radiobutton5_change(self):
        """Handle radioButton_5 changes and enable checkBox_3"""
        enabled = self.radioButton_5.isChecked() and self.groupBox_3.isEnabled()
        self.checkBox_3.setEnabled(enabled)
        if not enabled:
            self.reset_from_checkbox3()
        else:
            # Re-check subsequent elements when this becomes enabled
            self.handle_checkbox3_change()
        # Hide frame_17 when radioButton_5 is selected
        if self.radioButton_5.isChecked():
            self.frame_17.setVisible(False)
    
    def handle_radiobutton6_change(self):
        """Handle radioButton_6 changes and show frame_17"""
        if self.radioButton_6.isChecked() and self.groupBox_3.isEnabled():
            self.frame_17.setVisible(True)
            # Reset checkBox_3 path when taking the "No" path
            self.reset_from_checkbox3()
        else:
            self.frame_17.setVisible(False)
    
    def handle_checkbox3_change(self):
        """Handle checkBox_3 changes and enable groupBox_4"""
        enabled = self.checkBox_3.isChecked() and self.checkBox_3.isEnabled()
        self.groupBox_4.setEnabled(enabled)
        if not enabled:
            self.reset_from_groupbox4()
        else:
            # Re-check radio button states when this becomes enabled
            self.handle_radiobutton7_change()
            self.handle_radiobutton8_change()
    
    def handle_radiobutton7_change(self):
        """Handle radioButton_7 changes and enable pushButton"""
        enabled = self.radioButton_7.isChecked() and self.groupBox_4.isEnabled()
        self.pushButton.setEnabled(enabled)
        # Hide frame_18 when radioButton_7 is selected
        if self.radioButton_7.isChecked():
            self.frame_18.setVisible(False)
    
    def handle_radiobutton8_change(self):
        """Handle radioButton_8 changes and show frame_18"""
        if self.radioButton_8.isChecked() and self.groupBox_4.isEnabled():
            self.frame_18.setVisible(True)
            # Disable pushButton when taking the "No" path
            self.pushButton.setEnabled(False)
        else:
            self.frame_18.setVisible(False)
    
    def reset_from_frame8(self):
        """Reset all elements from frame_8 onwards - preserve user input"""
        # Don't clear lineEdit_1 - preserve user input
        self.reset_from_frame9()
    
    def reset_from_frame9(self):
        """Reset all elements from frame_9 onwards - preserve user input"""
        self.frame_9.setEnabled(False)
        # Don't clear lineEdit_2 - preserve user input
        self.reset_from_checkbox2()
    
    def reset_from_checkbox2(self):
        """Reset all elements from checkBox_2 onwards - preserve user input"""
        self.checkBox_2.setEnabled(False)
        # Don't uncheck checkBox_2 - preserve user choice
        self.reset_from_frame10()
    
    def reset_from_frame10(self):
        """Reset all elements from frame_10 onwards - preserve user input"""
        self.frame_10.setEnabled(False)
        # Don't clear lineEdit_3 - preserve user input
        self.reset_from_frame11()
    
    def reset_from_frame11(self):
        """Reset all elements from frame_11 onwards - preserve user input"""
        self.frame_11.setEnabled(False)
        # Don't clear lineEdit_4 - preserve user input
        self.reset_from_frame12()
    
    def reset_from_frame12(self):
        """Reset all elements from frame_12 onwards - preserve user input"""
        self.frame_12.setEnabled(False)
        # Don't clear lineEdit_5 - preserve user input
        self.reset_from_groupbox2()
    
    def reset_from_groupbox2(self):
        """Reset all elements from groupBox_2 onwards - preserve user input"""
        self.groupBox_2.setEnabled(False)
        # Don't uncheck radio buttons - preserve user choice
        self.frame_13.setVisible(False)
        self.reset_from_frame14()
    
    def reset_from_frame14(self):
        """Reset all elements from frame_14 onwards - preserve user input"""
        self.frame_14.setEnabled(False)
        # Don't clear lineEdit_6 - preserve user input
        self.reset_from_frame15()
    
    def reset_from_frame15(self):
        """Reset all elements from frame_15 onwards - preserve user input"""
        self.frame_15.setEnabled(False)
        # Don't clear lineEdit_7 - preserve user input
        self.reset_from_frame16()
    
    def reset_from_frame16(self):
        """Reset all elements from frame_16 onwards - preserve user input"""
        self.frame_16.setEnabled(False)
        # Don't clear lineEdit_8 - preserve user input
        self.reset_from_groupbox3()
    
    def reset_from_groupbox3(self):
        """Reset all elements from groupBox_3 onwards - preserve user input"""
        self.groupBox_3.setEnabled(False)
        # Don't uncheck radio buttons - preserve user choice
        self.frame_17.setVisible(False)
        self.reset_from_checkbox3()
    
    def reset_from_checkbox3(self):
        """Reset all elements from checkBox_3 onwards - preserve user input"""
        self.checkBox_3.setEnabled(False)
        # Don't uncheck checkBox_3 - preserve user choice
        self.reset_from_groupbox4()
    
    def reset_from_groupbox4(self):
        """Reset all elements from groupBox_4 onwards - preserve user input"""
        self.groupBox_4.setEnabled(False)
        # Don't uncheck radio buttons - preserve user choice
        self.frame_18.setVisible(False)
        self.pushButton.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
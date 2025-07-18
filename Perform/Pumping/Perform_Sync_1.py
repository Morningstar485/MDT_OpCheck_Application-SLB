from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

from utils import resource_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 500)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.verticalLayout_2.addWidget(self.checkBox_1)

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

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame)
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

        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.groupBox_1 = QGroupBox(self.frame)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(250, 0))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
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


        self.verticalLayout_2.addWidget(self.groupBox_1)

        self.frame_12 = QFrame(self.frame)
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


        self.verticalLayout_2.addWidget(self.frame_12)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(350, 0))
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_12.addWidget(self.radioButton_4)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.frame_13 = QFrame(self.frame)
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


        self.verticalLayout_2.addWidget(self.frame_13)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(41, 41))
        self.label_9.setMaximumSize(QSize(41, 41))
        self.label_9.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_1 = QLabel(self.frame_6)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_12.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.frame_6)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMinimumSize(QSize(80, 25))
        self.lineEdit_1.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.lineEdit_7 = QLineEdit(self.frame_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(80, 25))
        self.lineEdit_7.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_7)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.lineEdit_8 = QLineEdit(self.frame_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(80, 25))
        self.lineEdit_8.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit_8)


        self.verticalLayout.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_4.addWidget(self.label_16)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(80, 25))
        self.lineEdit_2.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_2)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.lineEdit_9 = QLineEdit(self.frame_9)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(80, 25))
        self.lineEdit_9.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_9)

        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.lineEdit_10 = QLineEdit(self.frame_9)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(80, 25))
        self.lineEdit_10.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.lineEdit_10)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.checkBox_11 = QCheckBox(self.frame_3)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setEnabled(True)
        self.checkBox_11.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_11)

        self.checkBox_5 = QCheckBox(self.frame_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_5)

        self.checkBox_8 = QCheckBox(self.frame_3)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setEnabled(True)
        self.checkBox_8.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.frame_3)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setEnabled(True)
        self.checkBox_9.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_9)

        self.checkBox_6 = QCheckBox(self.frame_3)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_6)

        self.checkBox_10 = QCheckBox(self.frame_3)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setEnabled(True)
        self.checkBox_10.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_10)

        self.checkBox_7 = QCheckBox(self.frame_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_7)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)


        self.retranslateUi(Dialog)
        
        # Initialize form state
        self.initialize_form()
        
        # Connect signals for sequential validation - left column
        self.checkBox_1.toggled.connect(self.check_checkbox_1)
        self.checkBox_2.toggled.connect(self.check_checkbox_2)
        self.checkBox_3.toggled.connect(self.check_checkbox_3)
        self.checkBox_4.toggled.connect(self.check_checkbox_4)
        self.radioButton_1.toggled.connect(self.check_groupbox_1_selection)
        self.radioButton_2.toggled.connect(self.check_groupbox_1_selection)
        self.groupBox_2.setEnabled(False)  # Will be enabled after groupBox_1
        self.radioButton_3.toggled.connect(self.check_groupbox_2_selection)
        self.radioButton_4.toggled.connect(self.check_groupbox_2_selection)
        
        # Connect signals for line edits - right column
        self.lineEdit_1.textChanged.connect(self.check_line_edits_sample)
        self.lineEdit_7.textChanged.connect(self.check_line_edits_sample)
        self.lineEdit_8.textChanged.connect(self.check_line_edits_sample)
        self.lineEdit_2.textChanged.connect(self.check_line_edits_guard)
        self.lineEdit_9.textChanged.connect(self.check_line_edits_guard)
        self.lineEdit_10.textChanged.connect(self.check_line_edits_guard)
        
        # Connect signals for right column checkboxes (in order of appearance)
        self.checkBox_11.toggled.connect(self.check_checkbox_11)
        self.checkBox_5.toggled.connect(self.check_checkbox_5)
        self.checkBox_8.toggled.connect(self.check_checkbox_8)
        self.checkBox_9.toggled.connect(self.check_checkbox_9)
        self.checkBox_6.toggled.connect(self.check_checkbox_6)
        self.checkBox_10.toggled.connect(self.check_checkbox_10)
        self.checkBox_7.toggled.connect(self.check_checkbox_7)

        self.pushButton.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    
    def initialize_form(self):
        """Initialize the form to its starting state"""
        # Hide error frames initially
        self.frame_12.hide()
        self.frame_13.hide()
        
        # Disable all controls except the first checkbox
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.groupBox_1.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        
        # Right column - disable line edit frames and checkboxes
        self.frame_6.setEnabled(False)  # Sample PO line edits
        self.frame_9.setEnabled(False)  # Guard PO line edits
        self.checkBox_11.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.checkBox_8.setEnabled(False)
        self.checkBox_9.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.checkBox_10.setEnabled(False)
        self.checkBox_7.setEnabled(False)
        
        self.pushButton.setEnabled(False)
        
        # Clear all selections
        self.clear_all_inputs()
    
    def clear_all_inputs(self):
        """Clear all inputs initially"""
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.radioButton_1.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_7.setChecked(False)
        
        # Clear line edits
        self.lineEdit_1.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_2.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
    
    def is_numeric(self, text):
        """Check if text is numeric"""
        try:
            float(text)
            return True
        except ValueError:
            return False
    
    # Left column validation functions
    def check_checkbox_1(self):
        """Check first checkbox and enable second checkbox"""
        if self.checkBox_1.isChecked():
            self.checkBox_2.setEnabled(True)
        else:
            self.checkBox_2.setEnabled(False)
            self.reset_from_checkbox_2()
    
    def check_checkbox_2(self):
        """Check second checkbox and enable third checkbox"""
        if self.checkBox_2.isChecked():
            self.checkBox_3.setEnabled(True)
        else:
            self.checkBox_3.setEnabled(False)
            self.reset_from_checkbox_3()
    
    def check_checkbox_3(self):
        """Check third checkbox and enable fourth checkbox"""
        if self.checkBox_3.isChecked():
            self.checkBox_4.setEnabled(True)
        else:
            self.checkBox_4.setEnabled(False)
            self.reset_from_checkbox_4()
    
    def check_checkbox_4(self):
        """Check fourth checkbox and enable first group box"""
        if self.checkBox_4.isChecked():
            self.groupBox_1.setEnabled(True)
        else:
            self.groupBox_1.setEnabled(False)
            self.reset_from_groupbox_1()
    
    def check_groupbox_1_selection(self):
        """Check first group box selection and handle Yes/No logic"""
        if self.radioButton_1.isChecked():  # Yes selected
            self.frame_12.hide()  # Hide error frame
            self.groupBox_2.setEnabled(True)
        elif self.radioButton_2.isChecked():  # No selected
            self.frame_12.show()  # Show error frame
            # Stop progression when No is selected
            self.groupBox_2.setEnabled(False)
            self.frame_6.setEnabled(False)
            self.frame_9.setEnabled(False)
            self.reset_from_groupbox_2()
    
    def check_groupbox_2_selection(self):
        """Check second group box selection and handle Yes/No logic"""
        if self.radioButton_3.isChecked():  # Yes selected
            self.frame_13.hide()  # Hide error frame
            # Enable right column line edit frames
            self.frame_6.setEnabled(True)
            self.frame_9.setEnabled(True)
        elif self.radioButton_4.isChecked():  # No selected
            self.frame_13.show()  # Show error frame
            # Stop progression when No is selected
            self.frame_6.setEnabled(False)
            self.frame_9.setEnabled(False)
            self.reset_from_line_edits()
    
    # Right column validation functions
    def check_line_edits_sample(self):
        """Check if all sample PO line edits are filled with numeric values"""
        self.check_all_line_edits()
    
    def check_line_edits_guard(self):
        """Check if all guard PO line edits are filled with numeric values"""
        self.check_all_line_edits()
    
    def check_all_line_edits(self):
        """Check if all line edits are filled with numeric values and enable first right column checkbox"""
        sample_filled = (self.lineEdit_1.text().strip() and 
                        self.lineEdit_7.text().strip() and 
                        self.lineEdit_8.text().strip() and
                        self.is_numeric(self.lineEdit_1.text().strip()) and
                        self.is_numeric(self.lineEdit_7.text().strip()) and
                        self.is_numeric(self.lineEdit_8.text().strip()))
        
        guard_filled = (self.lineEdit_2.text().strip() and 
                       self.lineEdit_9.text().strip() and 
                       self.lineEdit_10.text().strip() and
                       self.is_numeric(self.lineEdit_2.text().strip()) and
                       self.is_numeric(self.lineEdit_9.text().strip()) and
                       self.is_numeric(self.lineEdit_10.text().strip()))
        
        if sample_filled and guard_filled:
            self.checkBox_11.setEnabled(True)
        else:
            self.checkBox_11.setEnabled(False)
            self.reset_from_checkbox_11()
    
    def check_checkbox_11(self):
        """Check checkbox 11 and enable checkbox 5"""
        if self.checkBox_11.isChecked():
            self.checkBox_5.setEnabled(True)
        else:
            self.checkBox_5.setEnabled(False)
            self.reset_from_checkbox_5()
    
    def check_checkbox_5(self):
        """Check checkbox 5 and enable checkbox 8"""
        if self.checkBox_5.isChecked():
            self.checkBox_8.setEnabled(True)
        else:
            self.checkBox_8.setEnabled(False)
            self.reset_from_checkbox_8()
    
    def check_checkbox_8(self):
        """Check checkbox 8 and enable checkbox 9"""
        if self.checkBox_8.isChecked():
            self.checkBox_9.setEnabled(True)
        else:
            self.checkBox_9.setEnabled(False)
            self.reset_from_checkbox_9()
    
    def check_checkbox_9(self):
        """Check checkbox 9 and enable checkbox 6"""
        if self.checkBox_9.isChecked():
            self.checkBox_6.setEnabled(True)
        else:
            self.checkBox_6.setEnabled(False)
            self.reset_from_checkbox_6()
    
    def check_checkbox_6(self):
        """Check checkbox 6 and enable checkbox 10"""
        if self.checkBox_6.isChecked():
            self.checkBox_10.setEnabled(True)
        else:
            self.checkBox_10.setEnabled(False)
            self.reset_from_checkbox_10()
    
    def check_checkbox_10(self):
        """Check checkbox 10 and enable checkbox 7"""
        if self.checkBox_10.isChecked():
            self.checkBox_7.setEnabled(True)
        else:
            self.checkBox_7.setEnabled(False)
            self.reset_from_checkbox_7()
    
    def check_checkbox_7(self):
        """Check checkbox 7 and enable push button"""
        if self.checkBox_7.isChecked():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
    
    # Reset functions for cascading cleanup - only handle enablement, preserve user choices
    def reset_from_checkbox_2(self):
        """Reset all controls from checkbox 2 onwards - only disable, don't clear"""
        self.checkBox_3.setEnabled(False)
        self.reset_from_checkbox_3()
    
    def reset_from_checkbox_3(self):
        """Reset all controls from checkbox 3 onwards - only disable, don't clear"""
        self.checkBox_4.setEnabled(False)
        self.reset_from_checkbox_4()
    
    def reset_from_checkbox_4(self):
        """Reset all controls from checkbox 4 onwards - only disable, don't clear"""
        self.groupBox_1.setEnabled(False)
        self.reset_from_groupbox_1()
    
    def reset_from_groupbox_1(self):
        """Reset all controls from group box 1 onwards - only disable, don't clear"""
        self.frame_12.hide()  # Always hide error frame when resetting
        self.groupBox_2.setEnabled(False)
        self.reset_from_groupbox_2()
    
    def reset_from_groupbox_2(self):
        """Reset all controls from group box 2 onwards - only disable, don't clear"""
        self.frame_13.hide()  # Always hide error frame when resetting
        self.frame_6.setEnabled(False)
        self.frame_9.setEnabled(False)
        self.reset_from_line_edits()
    
    def reset_from_line_edits(self):
        """Reset all controls from line edits onwards - only disable, don't clear"""
        self.checkBox_11.setEnabled(False)
        self.reset_from_checkbox_11()
    
    def reset_from_checkbox_11(self):
        """Reset all controls from checkbox 11 onwards - only disable, don't clear"""
        self.checkBox_5.setEnabled(False)
        self.reset_from_checkbox_5()
    
    def reset_from_checkbox_5(self):
        """Reset all controls from checkbox 5 onwards - only disable, don't clear"""
        self.checkBox_8.setEnabled(False)
        self.reset_from_checkbox_8()
    
    def reset_from_checkbox_8(self):
        """Reset all controls from checkbox 8 onwards - only disable, don't clear"""
        self.checkBox_9.setEnabled(False)
        self.reset_from_checkbox_9()
    
    def reset_from_checkbox_9(self):
        """Reset all controls from checkbox 9 onwards - only disable, don't clear"""
        self.checkBox_6.setEnabled(False)
        self.reset_from_checkbox_6()
    
    def reset_from_checkbox_6(self):
        """Reset all controls from checkbox 6 onwards - only disable, don't clear"""
        self.checkBox_10.setEnabled(False)
        self.reset_from_checkbox_10()
    
    def reset_from_checkbox_10(self):
        """Reset all controls from checkbox 10 onwards - only disable, don't clear"""
        self.checkBox_7.setEnabled(False)
        self.reset_from_checkbox_7()
    
    def reset_from_checkbox_7(self):
        """Reset all controls from checkbox 7 onwards - only disable, don't clear"""
        self.pushButton.setEnabled(False)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Select the Sync Pumping in MRPQ UI", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Set the upper pump to constant speed 400 rpm,\n"
"and then lower the pump to constant power to 60%", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Start the pumps", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Close the BYPASS valves and verify that differential pressure\n"
"between the SG and the CQG remains below 250 psi", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"The differential pressure is below 250 Psi", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Stop the Pumps and set the restrictor pressure</span></p><p><span style=\" font-size:16pt; font-style:italic;\">for upper and lower exit ports to 1000 Psi</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Sample and guard pump cumulative current is under 11 amps", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Investigate which PO is taking more current</span></p></body></html>", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">Caution</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-family:'Arial','sans-serif'; font-size:12pt; font-style:italic; color:#231f20;\">Current Limit for a single MRPO is 8.5A [MREL] and 8A [Legacy]</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Sample PO</span></p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PMPRESS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Total Current</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Differential Pressure</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Gaurd PO</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">PMPRESS</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Total Current</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">Differential Pressure</span></p></body></html>", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"After 4 strokes on each PO \u2013 set restrictor pressure to zero (OPEN Restrictor)", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Stop the pumps and open the BYPASS valve", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Remove the bottle fill tank and connect shop air to the probe barrel", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"Remove the restrictors from the exit ports", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Increase the pump speed to 2000 rpm and start pump to flush the flowline with air", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"Confirm that the SOL3 is switching with the strokes", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Stop the pump when only air is coming out of the flowline", None))
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
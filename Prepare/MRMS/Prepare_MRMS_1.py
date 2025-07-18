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
        Dialog.resize(927, 659)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(41, 41))
        self.label_12.setMaximumSize(QSize(41, 41))
        self.label_12.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_12.setScaledContents(True)
        self.label_12.setVisible(False)

        self.horizontalLayout.addWidget(self.label_12)

        self.groupBox_1 = QGroupBox(self.frame)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(230, 0))
        self.groupBox_1.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_1.setCheckable(False)
        self.groupBox_1.setChecked(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_1 = QRadioButton(self.groupBox_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.groupBox_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_13.addWidget(self.radioButton_2)


        self.horizontalLayout.addWidget(self.groupBox_1)


        self.verticalLayout.addWidget(self.frame)

        self.checkBox_1 = QCheckBox(self.frame_5)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setEnabled(False)
        self.checkBox_1.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.groupBox_2 = QGroupBox(self.frame_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_11.addWidget(self.radioButton_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_13.setVisible(False)
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

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(41, 41))
        self.label_13.setMaximumSize(QSize(41, 41))
        self.label_13.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_13.setScaledContents(True)
        self.label_13.setVisible(False)

        self.horizontalLayout_2.addWidget(self.label_13)

        self.groupBox_3 = QGroupBox(self.frame_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(230, 0))
        self.groupBox_3.setEnabled(False)
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


        self.horizontalLayout_2.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.frame_3)

        self.checkBox_2 = QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout.addWidget(self.checkBox_2)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.frame_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setEnabled(False)
        self.groupBox_7.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.radioButton_13 = QRadioButton(self.groupBox_7)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_17.addWidget(self.radioButton_13)

        self.radioButton_14 = QRadioButton(self.groupBox_7)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_17.addWidget(self.radioButton_14)


        self.verticalLayout_2.addWidget(self.groupBox_7)

        self.checkBox_6 = QCheckBox(self.frame_7)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setVisible(False)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.groupBox_5 = QGroupBox(self.frame_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setChecked(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.radioButton_9 = QRadioButton(self.groupBox_5)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.groupBox_5)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_15.addWidget(self.radioButton_10)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.checkBox_4 = QCheckBox(self.frame_7)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(450, 200))
        self.label.setMaximumSize(QSize(450, 200))
        self.label.setPixmap(QPixmap(resource_path("Icons/Img_19.png")))
        self.label.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(41, 41))
        self.label_16.setMaximumSize(QSize(41, 41))
        self.label_16.setPixmap(QPixmap(resource_path("Icons/risk-icon.png")))
        self.label_16.setScaledContents(True)
        self.label_16.setVisible(False)

        self.horizontalLayout_3.addWidget(self.label_16)

        self.groupBox_6 = QGroupBox(self.frame_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(230, 0))
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setStyleSheet(u"QGroupBox::title {\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setChecked(False)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_11 = QRadioButton(self.groupBox_6)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.groupBox_6)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setStyleSheet(u"QRadioButton{\n"
"    font-size: 14px; /* Larger text */\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 15px; /* Larger checkbox square */\n"
"    height: 15px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_16.addWidget(self.radioButton_12)


        self.horizontalLayout_3.addWidget(self.groupBox_6)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.checkBox_5 = QCheckBox(self.frame_7)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"    font-size: 15px; /* Larger text */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Larger checkbox square */\n"
"    height: 20px; /* Larger checkbox square */\n"
"}")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.lineEdit_2 = QLineEdit(self.frame_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(125, 25))
        self.lineEdit_2.setMaximumSize(QSize(125, 25))
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setPlaceholderText("Enter 1-6")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        # Connect radio button signals to show/hide risk labels and frames
        self.radioButton_2.toggled.connect(lambda checked: self.label_12.setVisible(checked))
        self.radioButton_4.toggled.connect(lambda checked: self.frame_13.setVisible(checked))
        self.radioButton_6.toggled.connect(lambda checked: self.label_13.setVisible(checked))
        self.radioButton_12.toggled.connect(lambda checked: self.label_16.setVisible(checked))

        # Sequential logic for left column with iff (if and only if) logic
        # GB1 logic: Yes <-> enable GB2, No <-> enable CB1
        self.radioButton_1.toggled.connect(lambda checked: self.groupBox_2.setEnabled(checked))
        self.radioButton_2.toggled.connect(lambda checked: self.checkBox_1.setEnabled(checked))
        
        # CB1 logic: checked <-> enable GB2
        self.checkBox_1.toggled.connect(lambda checked: self.groupBox_2.setEnabled(checked))
        
        # GB2 logic: Yes <-> enable GB3
        self.radioButton_3.toggled.connect(lambda checked: self.groupBox_3.setEnabled(checked))
        
        # GB3 logic: Yes (Low Shock) <-> enable GB7, No (Reverse Low Shock) <-> enable CB2
        self.radioButton_5.toggled.connect(lambda checked: self.groupBox_7.setEnabled(checked))
        self.radioButton_6.toggled.connect(lambda checked: self.checkBox_2.setEnabled(checked))
        
        # CB2 logic: checked <-> enable GB7 (first GB of right column)
        self.checkBox_2.toggled.connect(lambda checked: self.groupBox_7.setEnabled(checked))

        # Right column logic with iff logic
        # GB7 logic: Yes <-> show and enable CB6, No <-> enable GB5
        self.radioButton_13.toggled.connect(lambda checked: (self.checkBox_6.setVisible(checked), self.checkBox_6.setEnabled(checked)))
        self.radioButton_14.toggled.connect(lambda checked: self.groupBox_5.setEnabled(checked))
        
        # CB6 logic: checked <-> enable GB5
        self.checkBox_6.toggled.connect(lambda checked: self.groupBox_5.setEnabled(checked))
        
        # GB5 logic: Yes <-> enable CB4 with original text, No <-> change CB4 text and enable it
        self.radioButton_9.toggled.connect(lambda checked: (
            self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Mud check valve (H730507) is installed", None)) if checked else None,
            self.checkBox_4.setEnabled(True)
        ) if checked else (
            self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Relief Plug Valve (H730586) is Installed", None)),
            self.checkBox_4.setEnabled(False)
        ))
        self.radioButton_10.toggled.connect(lambda checked: (
            self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Relief Plug Valve (H730586) is Installed", None)) if checked else None,
            self.checkBox_4.setEnabled(True)
        ) if checked else (
            self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Mud check valve (H730507) is installed", None)),
            self.checkBox_4.setEnabled(False)
        ))
        
        # CB4 logic: checked <-> enable GB6
        self.checkBox_4.toggled.connect(lambda checked: self.groupBox_6.setEnabled(checked))
        
        # GB6 logic: Yes <-> enable line edit, No <-> enable CB5
        self.radioButton_11.toggled.connect(lambda checked: self.lineEdit_2.setEnabled(checked))
        self.radioButton_12.toggled.connect(lambda checked: self.checkBox_5.setEnabled(checked))
        
        # CB5 logic: checked <-> enable line edit
        self.checkBox_5.toggled.connect(lambda checked: self.lineEdit_2.setEnabled(checked))
        
        # Line edit validation: enable push button only for integers 1-6
        def validate_line_edit():
            try:
                value = int(self.lineEdit_2.text())
                self.pushButton.setEnabled(1 <= value <= 6)
            except ValueError:
                self.pushButton.setEnabled(False)
        
        self.lineEdit_2.textChanged.connect(validate_line_edit)

        self.pushButton.hide()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Please download MRMS Configuration from InTouch</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Open InTouch", None))
        self.label_12.setText("")
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"SFT-275 available with all special tools?", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Informed Base", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Check that the piston is on the top position, against </span></p><p><span style=\" font-size:12pt; font-weight:700;\">the retaining ring. If not, this is an indication that </span></p><p><span style=\" font-size:12pt; font-weight:700;\">the oil level is low and needs to be filled</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Is the Oil level Full?", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Please fill up the oil</span></p></body></html>", None))
        self.label_13.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"What is the sampling", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Low Shock", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"Reverse Low Shock", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Informed PSD/JDL for Tool Prep", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Is MRMS located Above MRPO?", None))
        self.radioButton_13.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_14.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"The relief valve plug (H730586) is installed in the lower waterline port", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Upper waterline port is used as an exit port only", None))
        self.radioButton_9.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Mud check valve (H730507) is installed", None))
        self.label.setText("")
        self.label_16.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Is the Exit Screen Filter Available", None))
        self.radioButton_11.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.radioButton_12.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Informed Base", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:11pt;\">No. of MPSR Planned for the job</span></p></body></html>", None))
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
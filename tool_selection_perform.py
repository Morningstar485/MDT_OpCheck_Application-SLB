from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(738, 312)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(160, 50))
        self.pushButton_1.setMaximumSize(QSize(160, 50))
        self.pushButton_1.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(160, 50))
        self.pushButton_2.setMaximumSize(QSize(160, 50))
        self.pushButton_2.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(160, 50))
        self.pushButton_3.setMaximumSize(QSize(160, 50))
        self.pushButton_3.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(160, 50))
        self.pushButton_4.setMaximumSize(QSize(160, 50))
        self.pushButton_4.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(160, 50))
        self.pushButton_8.setMaximumSize(QSize(160, 50))
        self.pushButton_8.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(160, 50))
        self.pushButton_7.setMaximumSize(QSize(160, 50))
        self.pushButton_7.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(160, 50))
        self.pushButton_6.setMaximumSize(QSize(160, 50))
        self.pushButton_6.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(160, 50))
        self.pushButton_5.setMaximumSize(QSize(160, 50))
        self.pushButton_5.setStyleSheet(u"font-weight: bold;\n"
"font-size: 15px;")

        self.gridLayout.addWidget(self.pushButton_5, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(200, 15, 200, -1)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Please Select the Module You Want </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">to Perform the OST on</span></p></body></html>", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"MRMS", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"MRSC", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"MRPC", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"MRPO\n"
"[Initialize]", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"MRPO\n"
"[Performance]", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Sync\n"
"Pumping", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"MRPQ-HY", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"MRFA", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Finish OST and EXIT", None))
    # retranslateUi

from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from datetime import datetime

# Import your actual perform dialog classes
from Perform.MRFA.Perform_MRFA_c import Perform_MRFA_c
from Perform.MRMS.Perform_MRMS_c import Perform_MRMS_c
from Perform.MRPO.Perform_Performa_c import Perform_Performa_c
from Perform.MRPC.Perform_MRPC_c import Perform_MRPC_c
from Perform.MRSC.Perform_MRSC_c import Perform_MRSC_c
from Perform.MRPQ.Perform_MRPQ_c import Perform_MRPQ_c
from Perform.MRPO.Perform_Initialize_c import Perform_Initialize_c
from Perform.Pumping.Perform_Pumping import Perform_Pumping

# Import metadata and report management
from metadata_manager import MetadataManager
from report_generator import ReportGenerator
from metadata_manager import MetadataManager
from report_generator import ReportGenerator

class ToolSelectionPerformDialog(QDialog):
    def __init__(self, on_complete_callback=None, metadata_manager=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.on_complete_callback = on_complete_callback
        self.active_perform_window = None
        
        # Initialize metadata management
        self.metadata_manager = metadata_manager if metadata_manager else MetadataManager()
        self.report_generator = ReportGenerator()
        
        # Track completed tools for this perform phase
        self.completed_tools = []
        self.tool_button_names = {
            self.ui.pushButton_1: "MRMS",
            self.ui.pushButton_2: "MRSC", 
            self.ui.pushButton_3: "MRPC",
            self.ui.pushButton_4: "MRPO_Initialize",
            self.ui.pushButton_5: "MRFA",
            self.ui.pushButton_6: "MRPQ",
            self.ui.pushButton_7: "Sync_Pumping",
            self.ui.pushButton_8: "MRPO_Performance",
        }
        
        self.setup_connections()

    def setup_connections(self):
        self.tool_map = {
            self.ui.pushButton_1: Perform_MRMS_c,
            self.ui.pushButton_2: Perform_MRSC_c,
            self.ui.pushButton_3: Perform_MRPC_c,
            self.ui.pushButton_4: Perform_Initialize_c,
            self.ui.pushButton_5: Perform_MRFA_c,
            self.ui.pushButton_6: Perform_MRPQ_c,
            self.ui.pushButton_7: Perform_Pumping,
            self.ui.pushButton_8: Perform_Performa_c,
        }

        for button in self.tool_map:
            button.clicked.connect(lambda checked, btn=button: self.open_perform_tool(btn))

        self.ui.pushButton.clicked.connect(self.finish_and_exit)

    def open_perform_tool(self, button):
        if self.active_perform_window is not None:
            QMessageBox.warning(self, "Window Open", "Please close the open Perform window before starting a new one.")
            return

        button.setEnabled(False)
        dialog_class = self.tool_map.get(button)
        tool_name = self.tool_button_names.get(button, "Unknown")
        
        if dialog_class:
            try:
                # Pass self as parent to ensure proper parent-child relationship
                self.active_perform_window = dialog_class(self)
                self.active_perform_window.finished.connect(lambda result, btn=button, name=tool_name: self.on_tool_completed(btn, name, result))
                self.active_perform_window.show()
            except Exception as e:
                print(f"Error creating {tool_name} dialog: {e}")
                QMessageBox.warning(self, "Error", f"Failed to create {tool_name} dialog: {str(e)}")
                button.setEnabled(True)
        else:
            QMessageBox.warning(self, "Error", "No dialog mapped for this button.")
            button.setEnabled(True)

    def on_tool_completed(self, button, tool_name, result):
        """Handle tool completion - collect metadata and generate report"""
        try:
            # Get metadata from the completed tool if it has a get_metadata method
            tool_metadata = {}
            if hasattr(self.active_perform_window, 'get_metadata'):
                tool_metadata = self.active_perform_window.get_metadata()
            
            # Record tool completion
            completion_record = {
                "tool_name": tool_name,
                "phase": "Perform",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "success": result == 1,  # QDialog.Accepted
                "metadata": tool_metadata
            }
            
            self.completed_tools.append(completion_record)
            
            # Update global metadata with this tool's completion
            if not self.metadata_manager.global_metadata.get("processed_tools"):
                self.metadata_manager.global_metadata["processed_tools"] = []
            self.metadata_manager.global_metadata["processed_tools"].append(completion_record)
            
            # If tool completed successfully and has metadata, generate individual report
            if result == 1 and tool_metadata:
                try:
                    # Initialize local metadata for this tool
                    self.metadata_manager.init_local_data(tool_name, "Perform")
                    
                    # Set the collected metadata
                    if "test_results" in tool_metadata:
                        self.metadata_manager.local_metadata["test_results"] = tool_metadata["test_results"]
                    
                    # Handle different variations of user input keys
                    if "User Inputs" in tool_metadata:
                        self.metadata_manager.local_metadata["user_inputs"] = tool_metadata["User Inputs"]
                    elif "user_inputs" in tool_metadata:
                        self.metadata_manager.local_metadata["user_inputs"] = tool_metadata["user_inputs"]
                    elif "User Choices" in tool_metadata:
                        # Handle modules that use "User Choices" as their key
                        self.metadata_manager.local_metadata["user_inputs"] = tool_metadata["User Choices"]
                    
                    if "validation_results" in tool_metadata:
                        self.metadata_manager.local_metadata["validation_results"] = tool_metadata["validation_results"]
                    
                    # Set end time
                    self.metadata_manager.local_metadata["tool_info"]["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Generate individual tool report
                    report_path = self.report_generator.generate_tool_report(
                        self.metadata_manager.global_metadata,
                        self.metadata_manager.local_metadata
                    )
                    
                    QMessageBox.information(self, "Report Generated", 
                                          f"Tool report generated successfully:\n{report_path}")
                    
                except Exception as e:
                    QMessageBox.warning(self, "Report Error", 
                                      f"Failed to generate report for {tool_name}: {str(e)}")
            
        except Exception as e:
            QMessageBox.warning(self, "Metadata Error", 
                              f"Error processing metadata for {tool_name}: {str(e)}")
        finally:
            # Always reset the button and clear active window
            self.reset_button(button)

    def reset_button(self, button):
        button.setEnabled(True)
        self.active_perform_window = None

    def get_perform_metadata(self):
        """Get metadata for all completed perform tools"""
        return {
            "completed_tools": self.completed_tools,
            "phase_summary": {
                "phase_name": "Perform",
                "tools_completed": len(self.completed_tools),
                "successful_tools": len([t for t in self.completed_tools if t["success"]]),
                "completed_tool_list": [t["tool_name"] for t in self.completed_tools if t["success"]]
            }
        }

    def finish_and_exit(self):
        if self.active_perform_window is not None:
            QMessageBox.warning(self, "Cannot Exit", "Close the open Perform window before exiting.")
            return

        # Generate perform phase summary report if any tools were completed
        if self.completed_tools:
            try:
                # Update global metadata with perform phase summary
                perform_summary = {
                    "Phase Name": "Perform",
                    "Start Time": self.completed_tools[0]["timestamp"] if self.completed_tools else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "End Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Tools Completed": len(self.completed_tools),
                    "Successful Tools": len([t for t in self.completed_tools if t["success"]]),
                    "Completed Tool List": [t["tool_name"] for t in self.completed_tools if t["success"]]
                }
                
                self.metadata_manager.global_metadata["perform_data"] = perform_summary
                
                # Generate phase summary report
                report_path = self.report_generator.generate_phase_summary_report(
                    self.metadata_manager.global_metadata, 
                    "Perform"
                )
                
                QMessageBox.information(self, "Phase Report Generated", 
                                      f"Perform phase summary report generated:\n{report_path}")
                
            except Exception as e:
                QMessageBox.warning(self, "Report Error", 
                                  f"Failed to generate perform phase summary: {str(e)}")

        confirm = QMessageBox.question(self, "Confirm Exit", "Are you sure you want to finish OST and exit?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            if self.on_complete_callback:
                self.on_complete_callback()
            self.accept()

    def closeEvent(self, event):
        event.ignore()
        self.finish_and_exit()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = ToolSelectionPerformDialog()
    dialog.show()
    sys.exit(app.exec())

from PySide6.QtWidgets import QApplication, QWizard, QWizardPage, QDialog
import os
import sys
from datetime import datetime
from .Perform_Admin_1 import Ui_Dialog as Ui_Admin1
from .Perform_Admin_2 import Ui_Dialog as Ui_Admin2

# Add parent directory to path to import from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class AdminStep1Page(QWizardPage):
    def __init__(self, on_complete_callback = None):
        super().__init__()
        self.ui = Ui_Admin1()
        self.ui.setupUi(self)
        self.setTitle("Admin Step 1 - Resistance Values")
        self.setMinimumSize(374, 598)  # Matching original dialog size
        
        # Connect validation triggers - using line edits as triggers
        line_edits = [
            'lineEdit_1', 'lineEdit_2', 'lineEdit_3', 'lineEdit_4',
            'lineEdit_5', 'lineEdit_6', 'lineEdit_7', 'lineEdit_8',
            'lineEdit_9', 'lineEdit_10', 'lineEdit_11', 'lineEdit_12',
            'lineEdit_13', 'lineEdit_16', 'lineEdit_17', 'lineEdit_18',
            'lineEdit_20', 'lineEdit_21'
        ]
        
        for line_edit_name in line_edits:
            if hasattr(self.ui, line_edit_name):
                line_edit = getattr(self.ui, line_edit_name)
                line_edit.textChanged.connect(self.checkValidation)

        self.on_complete_callback = on_complete_callback

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return hasattr(self.ui, 'pushButton') and self.ui.pushButton.isEnabled()


class AdminStep2Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Admin2()
        self.ui.setupUi(self)
        self.setTitle("Admin Step 2 - Configuration and Testing")
        self.setMinimumSize(906, 400)  # Matching original dialog size

        # Connect validation triggers - monitoring key elements that affect pushButton state
        validation_elements = [
            'checkBox_1', 'lineEdit_1', 'lineEdit_2', 'checkBox_2',
            'lineEdit_3', 'lineEdit_4', 'lineEdit_5', 'radioButton_3',
            'radioButton_4', 'lineEdit_6', 'lineEdit_7', 'lineEdit_8',
            'radioButton_5', 'radioButton_6', 'checkBox_3', 'radioButton_7',
            'radioButton_8'
        ]
        
        for element_name in validation_elements:
            if hasattr(self.ui, element_name):
                element = getattr(self.ui, element_name)
                if hasattr(element, 'textChanged'):  # LineEdit
                    element.textChanged.connect(self.checkValidation)
                elif hasattr(element, 'toggled'):  # CheckBox or RadioButton
                    element.toggled.connect(self.checkValidation)
        
    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return hasattr(self.ui, 'pushButton') and self.ui.pushButton.isEnabled()


class Perform_Admin_c(QWizard):
    def __init__(self, parent=None, on_complete_callback=None):
        super().__init__(parent)
        self.on_complete_callback = on_complete_callback
        self.setWindowTitle("Perform Admin Wizard")

        self.addPage(AdminStep1Page())
        self.addPage(AdminStep2Page())

        # self.setOption(QWizard.IndependentPages, False)
        self.setWizardStyle(QWizard.ModernStyle)
        
        # Connect finished signal to callback and report generation
        if self.on_complete_callback:
            self.finished.connect(self.on_wizard_finished)
    
    def on_wizard_finished(self, result):
        """Handle wizard completion - generate report and execute callback"""
        if result == QWizard.Accepted:
            # Generate and save the report
            self.generate_report()
            
            # Execute the callback if provided
            if self.on_complete_callback:
                self.on_complete_callback()
    
    def generate_report(self):
        """Generate a report based on the collected metadata"""
        try:
            # Import here to avoid circular imports
            from report_generator import ReportGenerator
            
            # Get the metadata
            metadata = self.get_metadata()
            
            # Create properly formatted local metadata for the report generator
            local_metadata = {
                "tool_info": {
                    "tool_name": metadata.get("Tool Name", "Admin"),
                    "phase": "Perform",
                    "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "end_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                },
                "user_inputs": metadata.get("User Inputs", {})
            }
            
            # Create a report generator and generate the report
            report_gen = ReportGenerator()
            
            # Generate tool report with properly formatted metadata
            global_metadata = {}  # We might want to add global metadata here if needed
            report_path = report_gen.generate_tool_report(global_metadata, local_metadata)
            
            print(f"Admin report generated successfully at: {report_path}")
            return report_path
        except Exception as e:
            print(f"Error generating Admin report: {str(e)}")
            return None

    def get_metadata(self):
        """Collect metadata from both admin pages with descriptive keys"""
        metadata = {
            "Tool Name": "Admin",
            "User Inputs": {}
        }
        
        # Initialize a metadata directory
        metadata_directory = {}
        
        # ===== PAGE 1 METADATA =====
        # Get reference to the UI for page 1
        if self.page(0):
            page1_ui = self.page(0).ui
            
            # Personnel information
            if hasattr(page1_ui, 'lineEdit_1'):
                value = page1_ui.lineEdit_1.text().strip() or "Not entered"
                metadata_directory["Engineer Name"] = value
                
            if hasattr(page1_ui, 'lineEdit_2'):
                value = page1_ui.lineEdit_2.text().strip() or "Not entered"
                metadata_directory["Specialist Name"] = value
            
            # Cable specifications
            if hasattr(page1_ui, 'lineEdit_3'):
                value = page1_ui.lineEdit_3.text().strip() or "Not entered"
                metadata_directory["Cable Length"] = value
                
            if hasattr(page1_ui, 'lineEdit_4'):
                value = page1_ui.lineEdit_4.text().strip() or "Not entered"
                metadata_directory["Cable Type"] = value
            
            # Resistance measurements at surface latch - organized by connection points
            resistance_map = {
                'lineEdit_5': 'Connection 1-4', 
                'lineEdit_6': 'Connection 1-10', 
                'lineEdit_7': 'Connection 2-3',
                'lineEdit_8': 'Connection 2-10', 
                'lineEdit_9': 'Connection 2-5', 
                'lineEdit_10': 'Connection 3-10',
                'lineEdit_11': 'Connection 2-6', 
                'lineEdit_12': 'Connection 4-10', 
                'lineEdit_13': 'Connection 3-5',
                'lineEdit_18': 'Connection 5-10', 
                'lineEdit_16': 'Connection 3-6', 
                'lineEdit_17': 'Connection 6-10',
                'lineEdit_20': 'Connection 5-6', 
                'lineEdit_21': 'Connection 7-10'
            }
            
            for line_edit_name, label in resistance_map.items():
                if hasattr(page1_ui, line_edit_name):
                    value = getattr(page1_ui, line_edit_name).text().strip() or "Not entered"
                    metadata_directory[label] = value
        
        # Add validation status for page 1
        metadata_directory["Page 1 Validation Status"] = "Completed successfully" if self.page(0).isComplete() else "Incomplete"
        
        # ===== PAGE 2 METADATA =====
        # Get reference to the UI for page 2
        if self.page(1):
            page2_ui = self.page(1).ui
            
            # ===== SYSTEM SETUP SECTION =====
            # Tool Connection Status
            if hasattr(page2_ui, 'checkBox_1'):
                metadata_directory["Tools Connected per Job Plan"] = "Completed" if page2_ui.checkBox_1.isChecked() else "Not completed"
            
            # Maxwell System Information
            if hasattr(page2_ui, 'lineEdit_1'):
                value = page2_ui.lineEdit_1.text().strip() or "Not entered"
                metadata_directory["Maxwell Version"] = value
                
            if hasattr(page2_ui, 'lineEdit_2'):
                value = page2_ui.lineEdit_2.text().strip() or "Not entered"
                metadata_directory["Patch ID"] = value
            
            # Toolstring Declaration
            if hasattr(page2_ui, 'checkBox_2'):
                metadata_directory["Toolstring Declared in Maxwell"] = "Completed" if page2_ui.checkBox_2.isChecked() else "Not completed"
            
            # ===== VOLTAGE AND CURRENT MEASUREMENTS =====
            if hasattr(page2_ui, 'lineEdit_3'):
                value = page2_ui.lineEdit_3.text().strip() or "Not entered"
                metadata_directory["Downhole Voltage"] = value
                
            if hasattr(page2_ui, 'lineEdit_4'):
                value = page2_ui.lineEdit_4.text().strip() or "Not entered"
                metadata_directory["Downhole Current"] = value
                
            if hasattr(page2_ui, 'lineEdit_5'):
                value = page2_ui.lineEdit_5.text().strip() or "Not entered"
                metadata_directory["EDTC HV"] = value
            
            # ===== PASSING TEST RESULTS =====
            if hasattr(page2_ui, 'groupBox_2'):
                passing_test_value = "Not selected"
                if hasattr(page2_ui, 'radioButton_3') and page2_ui.radioButton_3.isChecked():
                    passing_test_value = "Success"
                elif hasattr(page2_ui, 'radioButton_4') and page2_ui.radioButton_4.isChecked():
                    passing_test_value = "Failed"
                
                metadata_directory["Initial System Passing Test"] = passing_test_value
            
            # ===== POWER UP MEASUREMENTS =====
            if hasattr(page2_ui, 'lineEdit_6'):
                value = page2_ui.lineEdit_6.text().strip() or "Not entered"
                metadata_directory["50V Power Up"] = value
                
            if hasattr(page2_ui, 'lineEdit_7'):
                value = page2_ui.lineEdit_7.text().strip() or "Not entered"
                metadata_directory["PPUC Value"] = value
                
            if hasattr(page2_ui, 'lineEdit_8'):
                value = page2_ui.lineEdit_8.text().strip() or "Not entered"
                metadata_directory["PPUV Value"] = value
            
            # ===== EDTC GAMMA RAY CALIBRATION =====
            if hasattr(page2_ui, 'radioButton_5') and page2_ui.radioButton_5.isChecked():
                metadata_directory["EDTC Gamma Ray Calibration"] = "Success"
            elif hasattr(page2_ui, 'radioButton_6') and page2_ui.radioButton_6.isChecked():
                metadata_directory["EDTC Gamma Ray Calibration"] = "Failed"
            else:
                metadata_directory["EDTC Gamma Ray Calibration"] = "Not selected"
            
            # ===== STATION LOG INITIATION =====
            if hasattr(page2_ui, 'checkBox_3'):
                metadata_directory["Station Log Started"] = "Completed" if page2_ui.checkBox_3.isChecked() else "Not completed"
            
            # ===== ACOM PASSING VERIFICATION =====
            if hasattr(page2_ui, 'radioButton_7') and page2_ui.radioButton_7.isChecked():
                metadata_directory["ACOM Passing Verification"] = "Success"
            elif hasattr(page2_ui, 'radioButton_8') and page2_ui.radioButton_8.isChecked():
                metadata_directory["ACOM Passing Verification"] = "Failed"
            else:
                metadata_directory["ACOM Passing Verification"] = "Not selected"
            
            # Add validation status for page 2
            metadata_directory["Page 2 Validation Status"] = "Completed successfully" if self.page(1).isComplete() else "Incomplete"
        
        # Overall status
        overall_complete = (self.page(0).isComplete() and 
                          self.page(1).isComplete())
        metadata_directory["Overall Test Status"] = "All Admin steps completed successfully" if overall_complete else "Admin test incomplete"
        
        # Copy the metadata directory to the standard User Inputs field
        metadata["User Inputs"] = metadata_directory
        
        return metadata

    def get_admin_data(self):
        """Legacy method for backward compatibility - calls get_metadata()"""
        return self.get_metadata()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QMessageBox
    app = QApplication(sys.argv)

    def on_wizard_complete():
        print("Admin wizard completed successfully!")

    # Create and show the wizard
    wizard = Perform_Admin_c(None, on_wizard_complete)
    wizard.show()

    # Run the application
    result = app.exec()
    
    # Generate a report if the wizard was accepted
    if hasattr(wizard, 'generate_report') and result == 0:  # 0 is QDialog.Accepted
        report_path = wizard.generate_report()
        if report_path:
            QMessageBox.information(None, "Report Generated", 
                                  f"Admin report generated successfully:\n{report_path}")
    
    sys.exit(result)

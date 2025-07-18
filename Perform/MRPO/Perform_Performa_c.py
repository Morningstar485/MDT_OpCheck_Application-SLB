from PySide6.QtWidgets import QApplication, QWizard, QWizardPage
from .Perform_Performa_1 import Ui_Dialog as Ui_Performa1
from .Perform_Performa_2 import Ui_Dialog as Ui_Performa2

class PerformaStep1Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Performa1()
        self.ui.setupUi(self)
        self.setTitle("MRPO Performa Step 1")
        self.setMinimumSize(1148, 737)  # Adjusted size to fit content
        
        # Connect validation triggers - using line edits as triggers
        if hasattr(self.ui, 'lineEdit_31'):
            self.ui.lineEdit_31.textChanged.connect(self.checkValidation)
        if hasattr(self.ui, 'lineEdit_32'):
            self.ui.lineEdit_32.textChanged.connect(self.checkValidation)
        if hasattr(self.ui, 'lineEdit_33'):
            self.ui.lineEdit_33.textChanged.connect(self.checkValidation)

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton_next.isEnabled()


class PerformaStep2Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Performa2()
        self.ui.setupUi(self)
        self.setTitle("MRPO Performa Step 2")
        self.setMinimumSize(587, 459)  # Adjusted size to fit content

        # Connect validation triggers

        if hasattr(self.ui, 'checkBox_6'):
            self.ui.checkBox_6.toggled.connect(self.checkValidation)

        if hasattr(self.ui, 'radioButton_3'):
            self.ui.radioButton_3.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'radioButton_4'):
            self.ui.radioButton_4.toggled.connect(self.checkValidation)
        
    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton_finish.isEnabled()


class Perform_Performa_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Perform MRPO Performa Wizard")

        self.step1_page = PerformaStep1Page()
        self.step2_page = PerformaStep2Page()
        
        self.addPage(self.step1_page)
        self.addPage(self.step2_page)

        # self.setOption(QWizard.IndependentPages, False)
        self.setWizardStyle(QWizard.ModernStyle)
    
    def get_metadata(self):
        """Collect metadata from both performa wizard pages"""
        # Initialize metadata structure with standard format
        metadata = {
            "Tool Name": "MRPO Performance",
            "User Inputs": {}
        }
        
        # Initialize a metadata directory
        metadata_directory = {}
        
        # ===== PAGE 1 METADATA =====
        # Get reference to the UI for page 1
        step1_ui = self.step1_page.ui

        if hasattr(step1_ui, "checkBox_1"):
            metadata_directory["Set in Constant Speed Mode"] = "Done"
        
        # Collect line edit values for the first 6 line edits as a template
        if hasattr(step1_ui, 'lineEdit_1'):
            value = step1_ui.lineEdit_1.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-1000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_2'):
            value = step1_ui.lineEdit_2.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-1000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_3'):
            value = step1_ui.lineEdit_3.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-1000 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_4'):
            value = step1_ui.lineEdit_4.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-1500 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_5'):
            value = step1_ui.lineEdit_5.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-1500 : Current"] = value

        if hasattr(step1_ui, 'lineEdit_6'):
            value = step1_ui.lineEdit_6.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-1500 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_7'):
            value = step1_ui.lineEdit_7.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-2000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_8'):
            value = step1_ui.lineEdit_8.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-2000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_9'):
            value = step1_ui.lineEdit_9.text().strip() or "Not entered"
            metadata_directory["RPM-500, Pressure-2000 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_10'):
            value = step1_ui.lineEdit_10.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-2000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_11'):
            value = step1_ui.lineEdit_11.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-2000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_12'):
            value = step1_ui.lineEdit_12.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-2000 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_34'):
            value = step1_ui.lineEdit_34.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-1500 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_35'):
            value = step1_ui.lineEdit_35.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-1500 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_36'):
            value = step1_ui.lineEdit_36.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-1500 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_13'):
            value = step1_ui.lineEdit_13.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-1000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_14'):
            value = step1_ui.lineEdit_14.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-1000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_15'):
            value = step1_ui.lineEdit_15.text().strip() or "Not entered"
            metadata_directory["RPM-1000, Pressure-1000 : Stroke Time"] = value

        if hasattr(step1_ui, 'lineEdit_16'):
            value = step1_ui.lineEdit_16.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-1000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_17'):
            value = step1_ui.lineEdit_17.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-1000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_18'):
            value = step1_ui.lineEdit_18.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-1000 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_19'):
            value = step1_ui.lineEdit_19.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-1500 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_20'):
            value = step1_ui.lineEdit_20.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-1500 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_21'):
            value = step1_ui.lineEdit_21.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-1500 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_22'):
            value = step1_ui.lineEdit_22.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-2000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_23'):
            value = step1_ui.lineEdit_23.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-2000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_24'):
            value = step1_ui.lineEdit_24.text().strip() or "Not entered"
            metadata_directory["RPM-1500, Pressure-2000 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_25'):
            value = step1_ui.lineEdit_25.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-2000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_26'):
            value = step1_ui.lineEdit_26.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-2000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_27'):
            value = step1_ui.lineEdit_27.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-2000 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_28'):
            value = step1_ui.lineEdit_28.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-1500 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_29'):
            value = step1_ui.lineEdit_29.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-1500 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_30'):
            value = step1_ui.lineEdit_30.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-1500 : Stroke Time"] = value
            
        if hasattr(step1_ui, 'lineEdit_31'):
            value = step1_ui.lineEdit_31.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-1000 : HPRESS"] = value
            
        if hasattr(step1_ui, 'lineEdit_32'):
            value = step1_ui.lineEdit_32.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-1000 : Current"] = value
            
        if hasattr(step1_ui, 'lineEdit_33'):
            value = step1_ui.lineEdit_33.text().strip() or "Not entered"
            metadata_directory["RPM-2000, Pressure-1000 : Stroke Time"] = value
        
        # Add validation status for page 1
        metadata_directory["Page 1 Validation Status"] = "Completed successfully" if self.step1_page.isComplete() else "Incomplete"
        
        # ===== PAGE 2 METADATA =====
        # Get reference to the UI for page 2
        step2_ui = self.step2_page.ui
        
        # Collect all checkbox states in sequence
        if hasattr(step2_ui, 'checkBox_1'):
            metadata_directory["Open Restrictors"] = "Completed" if step2_ui.checkBox_1.isChecked() else "Not completed"
            
        if hasattr(step2_ui, 'checkBox_2'):
            metadata_directory["Reduce Pump Speed to 500 RPM"] = "Completed" if step2_ui.checkBox_2.isChecked() else "Not completed"
            
        if hasattr(step2_ui, 'checkBox_3'):
            metadata_directory["Close Bottom Exit Port Seal Valve"] = "Completed" if step2_ui.checkBox_3.isChecked() else "Not completed"
            
        if hasattr(step2_ui, 'checkBox_4'):
            metadata_directory["Check for Pressure Drop and Leaks"] = "Completed" if step2_ui.checkBox_4.isChecked() else "Not completed"
        
        # GroupBox 1 - Leaks Present?
        if hasattr(step2_ui, 'groupBox_1'):
            leak_value = "None selected"
            if hasattr(step2_ui, 'radioButton_1') and step2_ui.radioButton_1.isChecked():
                leak_value = "Yes"
            elif hasattr(step2_ui, 'radioButton_2') and step2_ui.radioButton_2.isChecked():
                leak_value = "No"
                
            metadata_directory["Leaks Present"] = leak_value
            
        if hasattr(step2_ui, 'checkBox_5'):
            metadata_directory["Reverse Toggle MRPO Twice"] = "Completed" if step2_ui.checkBox_5.isChecked() else "Not completed"
            
        # GroupBox 2 - HPRESS between 0-200 Psi?
        if hasattr(step2_ui, 'groupBox_2'):
            pressure_value = "None selected"
            if hasattr(step2_ui, 'radioButton_3') and step2_ui.radioButton_3.isChecked():
                pressure_value = "Yes"
            elif hasattr(step2_ui, 'radioButton_4') and step2_ui.radioButton_4.isChecked():
                pressure_value = "No"
                
            metadata_directory["HPRESS Between 0-200 Psi"] = pressure_value
            
        if hasattr(step2_ui, 'checkBox_6'):
            # This checkbox is only shown when radioButton_3 (Yes) is selected
            if not step2_ui.checkBox_6.isHidden():
                metadata_directory["Open MRSC Seal Valve and check counter 130 +- 8"] = "Completed" if step2_ui.checkBox_6.isChecked() else "Not completed"
            else:
                metadata_directory["Open MRSC Seal Valve"] = "Not applicable"
        
        # Add validation status for page 2
        metadata_directory["Page 2 Validation Status"] = "Completed successfully" if self.step2_page.isComplete() else "Incomplete"
        
        # Overall status
        overall_complete = self.step1_page.isComplete() and self.step2_page.isComplete()
        metadata_directory["Overall Test Status"] = "All MRPO Performa steps completed successfully" if overall_complete else "MRPO Performa test incomplete"
        
        # Copy the metadata directory to the standard User Inputs field
        metadata["User Inputs"] = metadata_directory
        
        return metadata

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    wizard = Perform_Performa_c()
    wizard.show()

    sys.exit(app.exec())

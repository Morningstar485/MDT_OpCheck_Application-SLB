from PySide6.QtWidgets import QApplication, QWizard, QWizardPage
from .Perform_Sync_1 import Ui_Dialog as Ui_Sync1
from .Perform_Sync_2 import Ui_Dialog as Ui_Sync2


class SyncStep1Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sync1()
        self.ui.setupUi(self)
        self.setTitle("Sync Pumping Step 1")
        self.setMinimumSize(1000, 500)  # Size to fit content
        
        if hasattr(self.ui, 'checkBox_7'):
            self.ui.checkBox_7.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'checkBox_10'):
            self.ui.checkBox_10.toggled.connect(self.checkValidation)

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton.isEnabled()


class SyncStep2Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sync2()
        self.ui.setupUi(self)
        self.setTitle("Sync Pumping Step 2")
        self.setMinimumSize(791, 447)  # Size to fit content

        # Connect validation triggers - checkboxes, line edits, radio buttons
        if hasattr(self.ui, 'checkBox_10'):
            self.ui.checkBox_10.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'checkBox_11'):
            self.ui.checkBox_11.toggled.connect(self.checkValidation)
        
    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton.isEnabled()


class Perform_Pumping(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Perform Sync Pumping Wizard")

        self.step1_page = SyncStep1Page()
        self.step2_page = SyncStep2Page()

        self.addPage(self.step1_page)
        self.addPage(self.step2_page)

        # self.setOption(QWizard.IndependentPages, False)
        self.setWizardStyle(QWizard.ModernStyle)
    
    def get_metadata(self):
        """Collect metadata from both sync pumping wizard pages"""
        # Initialize metadata structure with standard format
        metadata = {
            "Tool Name": "Sync Pumping",
            "User Inputs": {}
        }
        
        # Initialize a metadata directory like in MRMS
        metadata_directory = {}
        
        # Step 1 metadata - collect all inputs in the exact sequence from the UI
        step1_ui = self.step1_page.ui
        
        # Left column - checkbox sequence in Perform_Sync_1.py
        if hasattr(step1_ui, 'checkBox_1'):
            metadata_directory["Selected Sync Pumping in MRPQ UI"] = "Completed" if step1_ui.checkBox_1.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_2'):
            metadata_directory["Both Pumps set to given values"] = "Completed" if step1_ui.checkBox_2.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_3'):
            metadata_directory["Pumps Started"] = "Completed" if step1_ui.checkBox_3.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_4'):
            metadata_directory["Bypass Valve Closed and Differential Pressure Verified"] = "Completed" if step1_ui.checkBox_4.isChecked() else "Not completed"
        
        # GroupBox 1 radio buttons
        if hasattr(step1_ui, 'groupBox_1'):
            groupbox1_value = "None selected"
            if hasattr(step1_ui, 'radioButton_1') and step1_ui.radioButton_1.isChecked():
                groupbox1_value = "Yes"
            elif hasattr(step1_ui, 'radioButton_2') and step1_ui.radioButton_2.isChecked():
                groupbox1_value = "No"
                
            if hasattr(step1_ui, 'groupBox_1') and hasattr(step1_ui.groupBox_1, 'title'):
                metadata_directory["The differential pressure is below 250 Psi"] = groupbox1_value
            else:
                metadata_directory["GroupBox 1 Selection"] = groupbox1_value
        
        # GroupBox 2 radio buttons
        if hasattr(step1_ui, 'groupBox_2'):
            groupbox2_value = "None selected"
            if hasattr(step1_ui, 'radioButton_3') and step1_ui.radioButton_3.isChecked():
                groupbox2_value = "Yes"
            elif hasattr(step1_ui, 'radioButton_4') and step1_ui.radioButton_4.isChecked():
                groupbox2_value = "No"
                
            if hasattr(step1_ui, 'groupBox_2') and hasattr(step1_ui.groupBox_2, 'title'):
                metadata_directory["Sample and guard pump cumulative current is under 11 amps"] = groupbox2_value
            else:
                metadata_directory["GroupBox 2 Selection"] = groupbox2_value
        
        # Right column - line edits and remaining checkboxes
        # Sample line edits
        if hasattr(step1_ui, 'lineEdit_1'):
            sample_pressure = step1_ui.lineEdit_1.text().strip() or "Not entered"
            metadata_directory["Sample PO PMPRESS"] = sample_pressure
            
        if hasattr(step1_ui, 'lineEdit_7'):
            sample_flow = step1_ui.lineEdit_7.text().strip() or "Not entered"
            metadata_directory["Sample PO Total Current"] = sample_flow
            
        if hasattr(step1_ui, 'lineEdit_8'):
            sample_pump = step1_ui.lineEdit_8.text().strip() or "Not entered"
            metadata_directory["Sample PO Differential Pressure"] = sample_pump
        
        # Guard line edits
        if hasattr(step1_ui, 'lineEdit_2'):
            guard_pressure = step1_ui.lineEdit_2.text().strip() or "Not entered"
            metadata_directory["Guard PO PMPRESS"] = guard_pressure
            
        if hasattr(step1_ui, 'lineEdit_9'):
            guard_flow = step1_ui.lineEdit_9.text().strip() or "Not entered"
            metadata_directory["Guard PO Total Current"] = guard_flow
            
        if hasattr(step1_ui, 'lineEdit_10'):
            guard_pump = step1_ui.lineEdit_10.text().strip() or "Not entered"
            metadata_directory["Guard PO Differential Pressure"] = guard_pump

        # Remaining checkboxes in order of appearance in the UI
        if hasattr(step1_ui, 'checkBox_11'):
            metadata_directory["Reset Valve Counter to 0"] = "Completed" if step1_ui.checkBox_11.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_5'):
            metadata_directory["Open pump inlet valves"] = "Completed" if step1_ui.checkBox_5.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_8'):
            metadata_directory["Cycle probe 5 times"] = "Completed" if step1_ui.checkBox_8.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_9'):
            metadata_directory["Pump inlet valves closed"] = "Completed" if step1_ui.checkBox_9.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_6'):
            metadata_directory["Open pump bypass valves"] = "Completed" if step1_ui.checkBox_6.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_10'):
            metadata_directory["Sync pumping complete"] = "Completed" if step1_ui.checkBox_10.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_7'):
            metadata_directory["MRPQ UI closed"] = "Completed" if step1_ui.checkBox_7.isChecked() else "Not completed"
        
        metadata_directory["Step 1 Validation Status"] = "Completed successfully" if self.step1_page.isComplete() else "Incomplete"
        
        # Step 2 metadata - collect all inputs in the exact sequence from the UI in Perform_Sync_2.py
        step2_ui = self.step2_page.ui
        
        # First column checkboxes (left side)
        if hasattr(step2_ui, 'checkBox_1'):
            metadata_directory["Set SWTC to 1500 RPM"] = "Completed" if step2_ui.checkBox_1.isChecked() else "Not completed"
            
        if hasattr(step2_ui, 'checkBox_2'):
            metadata_directory["Set GWTC to 1700 RPM"] = "Completed" if step2_ui.checkBox_2.isChecked() else "Not completed"
            
        if hasattr(step2_ui, 'checkBox_3'):
            metadata_directory["Exit and enter PUMPTEST"] = "Completed" if step2_ui.checkBox_3.isChecked() else "Not completed"

        # Line edit values for pressure readings in left column
        if hasattr(step2_ui, 'lineEdit_2'):
            pressure_val = step2_ui.lineEdit_2.text().strip() or "Not entered"
            metadata_directory["HPRESS Reading 1"] = pressure_val
                
        if hasattr(step2_ui, 'lineEdit_1'):
            pressure_val = step2_ui.lineEdit_1.text().strip() or "Not entered"
            metadata_directory["HPRESS Reading 2"] = pressure_val
        # Next checkboxes in sequence
        if hasattr(step2_ui, 'checkBox_4'):
            metadata_directory["Choose Yes in popup window for auto Retract"] = "Completed" if step2_ui.checkBox_4.isChecked() else "Not completed"

        # Line edit values for additional readings
        if hasattr(step2_ui, 'lineEdit_4'):
            reading_val = step2_ui.lineEdit_4.text().strip() or "Not entered"
            metadata_directory["PMPRESS Reading 1"] = reading_val

        if hasattr(step2_ui, 'lineEdit_3'):
            reading_val = step2_ui.lineEdit_3.text().strip() or "Not entered"
            metadata_directory["PMPRESS Reading 2"] = reading_val
    
        if hasattr(step2_ui, 'checkBox_5'):
            metadata_directory["Wait for complete retraction (Piston/Probe)"] = "Completed" if step2_ui.checkBox_5.isChecked() else "Not completed"
            
        if hasattr(step2_ui, 'checkBox_6'):
            metadata_directory["Check that Probe/Piston has Retracted"] = "Completed" if step2_ui.checkBox_6.isChecked() else "Not completed"

        # Second column elements (right side)
        # GroupBox radio buttons
        if hasattr(step2_ui, 'groupBox_2'):
            groupbox_value = "None selected"
            if hasattr(step2_ui, 'radioButton_3') and step2_ui.radioButton_3.isChecked():
                groupbox_value = "Yes"
            elif hasattr(step2_ui, 'radioButton_4') and step2_ui.radioButton_4.isChecked():
                groupbox_value = "No"
                
            metadata_directory["After Probe & Piston have retracted, go to manual retract"] = groupbox_value

        if hasattr(step2_ui, 'checkBox_7'):
            metadata_directory["Choose NO in the popup window"] = "Completed" if step2_ui.checkBox_7.isChecked() else "Not completed"

        if hasattr(step2_ui, 'checkBox_8'):
            metadata_directory['Wait for 1 minute and verify that the Probe & Piston did not Retracted'] = "Completed" if step2_ui.checkBox_8.isChecked() else "Not completed"

        if hasattr(step2_ui, 'checkBox_9'):
            metadata_directory['Subsequently, choose YES in the popup window to Auto retract probe'] = "Completed" if step2_ui.checkBox_9.isChecked() else "Not completed"

        if hasattr(step2_ui, 'checkBox_10'):
            metadata_directory['Generate station dlis with naming “MDT OST_Rig name_Section_Date"'] = "Completed" if step2_ui.checkBox_10.isChecked() else "Not completed"

        if hasattr(step2_ui, 'checkBox_11'):
            metadata_directory['Create Job spec dlis with naming “MDT PQ#--- FA#--- _date"'] = "Completed" if step2_ui.checkBox_11.isChecked() else "Not completed"

        metadata_directory["Step 2 Validation Status"] = "Completed successfully" if self.step2_page.isComplete() else "Incomplete"
        
        # Overall status
        overall_complete = self.step1_page.isComplete() and self.step2_page.isComplete()
        metadata_directory["Overall Test Status"] = "All sync pumping steps completed successfully" if overall_complete else "Sync pumping test incomplete"
        
        # Copy the metadata directory to the standard User Inputs field
        metadata["User Inputs"] = metadata_directory
        
        return metadata

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    wizard = Perform_Pumping()
    wizard.show()

    sys.exit(app.exec())

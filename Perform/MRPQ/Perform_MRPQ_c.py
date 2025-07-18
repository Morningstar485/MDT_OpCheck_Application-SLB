from PySide6.QtWidgets import QApplication, QWizard, QWizardPage
from .Perform_MRPQ_1 import Ui_Dialog as Ui_MRPQ1
from .Perform_MRPQ_2 import Ui_Dialog as Ui_MRPQ2
from .Perform_MRPQ_3 import Ui_Dialog as Ui_MRPQ3


class MRPQStep1Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPQ1()
        self.ui.setupUi(self)
        self.setTitle("MRPQ Step 1")
        self.setMinimumSize(1337, 660)  # Adjusted size to fit content
 
        if hasattr(self.ui, 'lineEdit_11'):
            self.ui.lineEdit_11.textChanged.connect(self.checkValidation)
        if hasattr(self.ui, 'lineEdit_12'):
            self.ui.lineEdit_12.textChanged.connect(self.checkValidation)

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton.isEnabled()

class MRPQStep2Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPQ2()
        self.ui.setupUi(self)
        self.setTitle("MRPQ Step 2")
        self.setMinimumSize(1106, 731)  # Adjusted size to fit content

        if hasattr(self.ui, 'lineEdit_13'):
            self.ui.lineEdit_13.textChanged.connect(self.checkValidation)
        if hasattr(self.ui, 'lineEdit_14'):
            self.ui.lineEdit_14.textChanged.connect(self.checkValidation)

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton.isEnabled()

class MRPQStep3Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPQ3()
        self.ui.setupUi(self)
        self.setTitle("MRPQ Step 3")
        self.setMinimumSize(562,412)

        self.ui.pushButton.hide()  # Hide the original next button
        self.ui.pushButton_2.hide()  # Hide the original back button

        if hasattr(self.ui, 'checkBox_3'):
            self.ui.checkBox_3.stateChanged.connect(self.checkValidation)
        
    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton.isEnabled()

class Perform_MRPQ_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Perform MRPQ Wizard")

        self.step1_page = MRPQStep1Page()
        self.step2_page = MRPQStep2Page()
        self.step3_page = MRPQStep3Page()

        self.addPage(self.step1_page)
        self.addPage(self.step2_page)
        self.addPage(self.step3_page)

        # self.setOption(QWizard.IndependentPages, False)
        self.setWizardStyle(QWizard.ModernStyle)
    
    def get_metadata(self):
        """Collect metadata from all three MRPQ wizard pages"""
        metadata = {
            "Tool Name": "MRPQ",
            "User Inputs": {}
        }
        
        # Initialize a metadata directory
        metadata_directory = {}
        
        # ===== PAGE 1 METADATA =====
        # Get reference to the UI for page 1
        step1_ui = self.step1_page.ui
        
        # Collect checkbox states
        if hasattr(step1_ui, 'checkBox_1'):
            metadata_directory["Close ADV with 10 ft..lb TORQUE ONLY"] = "Completed" if step1_ui.checkBox_1.isChecked() else "Not completed"
            
        # Collect line edit values from first row
        if hasattr(step1_ui, 'lineEdit_1'):
            value = step1_ui.lineEdit_1.text().strip() or "Not entered"
            metadata_directory["Initial Set Line Pressure"] = value
            
        if hasattr(step1_ui, 'lineEdit_2'):
            value = step1_ui.lineEdit_2.text().strip() or "Not entered"
            metadata_directory["Initial Hydraulic Pressure"] = value
            
        # Collect line edit values from second row
        if hasattr(step1_ui, 'lineEdit_3'):
            value = step1_ui.lineEdit_3.text().strip() or "Not entered"
            metadata_directory["SG Pressure"] = value
            
        if hasattr(step1_ui, 'lineEdit_4'):
            value = step1_ui.lineEdit_4.text().strip() or "Not entered"
            metadata_directory["SG Temperature"] = value
            
        # Collect line edit values from third row
        if hasattr(step1_ui, 'lineEdit_5'):
            value = step1_ui.lineEdit_5.text().strip() or "Not entered"
            metadata_directory["CQG Pressure"] = value
            
        if hasattr(step1_ui, 'lineEdit_8'):
            value = step1_ui.lineEdit_8.text().strip() or "Not entered"
            metadata_directory["CQG Temperature"] = value

        # Collect checkbox state
        if hasattr(step1_ui, 'checkBox_3'):
            metadata_directory["Set the Probe"] = "Completed" if step1_ui.checkBox_3.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'groupBox_1'):
            groupbox1_value = "None selected"
            if hasattr(step1_ui, 'radioButton_1') and step1_ui.radioButton_1.isChecked():
                groupbox1_value = "Yes"
            elif hasattr(step1_ui, 'radioButton_2') and step1_ui.radioButton_2.isChecked():
                groupbox1_value = "No"
                
            metadata_directory["Solenoid Status Charging"] = groupbox1_value

        if hasattr(step1_ui, 'groupBox_2') and step1_ui.groupBox_2.isEnabled():
            groupbox2_value = "None selected"
            if hasattr(step1_ui, 'radioButton_3') and step1_ui.radioButton_3.isChecked():
                groupbox2_value = "Yes"
            elif hasattr(step1_ui, 'radioButton_4') and step1_ui.radioButton_4.isChecked():
                groupbox2_value = "No"
                
            metadata_directory["Is the updated Status as Charging?"] = groupbox2_value
        
        if hasattr(step1_ui, 'checkBox_4'):
            metadata_directory["Set the Probe Again"] = "Completed" if step1_ui.checkBox_4.isChecked() else "Not completed"
            
        # Collect line edit values from final row
        if hasattr(step1_ui, 'lineEdit_6'):
            value = step1_ui.lineEdit_6.text().strip() or "Not entered"
            metadata_directory["Set Line Pressure 1"] = value
            
        if hasattr(step1_ui, 'lineEdit_7'):
            value = step1_ui.lineEdit_7.text().strip() or "Not entered"
            metadata_directory["Hydraulic Pressure 1"] = value
            
        # ===== SECOND COLUMN OF PAGE 1 =====
        # Collect checkbox states from second column

        if hasattr(step1_ui, 'groupBox_3'):
            groupbox3_value = "None selected"
            if hasattr(step1_ui, 'radioButton_5') and step1_ui.radioButton_5.isChecked():
                groupbox3_value = "Yes"
            elif hasattr(step1_ui, 'radioButton_6') and step1_ui.radioButton_6.isChecked():
                groupbox3_value = "No"
                
            metadata_directory["Is the Volumetric 10cc @60cc/min"] = groupbox3_value
         

        if hasattr(step1_ui, 'checkBox_2'):
            metadata_directory["PTVOL is 10 ± 0.5 cc 1st"] = "Completed" if step1_ui.checkBox_2.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_5'):
            metadata_directory["MRHY PMPVOL reads between 65 and 80 cc 1st"] = "Completed" if step1_ui.checkBox_5.isChecked() else "Not completed"
        
        if hasattr(step1_ui, 'groupBox_4'):
            groupbox4_value = "None selected"
            if hasattr(step1_ui, 'radioButton_7') and step1_ui.radioButton_7.isChecked():
                groupbox4_value = "Pass"
            elif hasattr(step1_ui, 'radioButton_8') and step1_ui.radioButton_8.isChecked():
                groupbox4_value = "Fail"
                
            metadata_directory["Is the Volumetric 15 cc @ 30 cc/min"] = groupbox4_value
        

        if hasattr(step1_ui, 'checkBox_6'):
            metadata_directory["PTVOL is 10 ± 0.5 cc 2nd"] = "Completed" if step1_ui.checkBox_6.isChecked() else "Not completed"
            
        if hasattr(step1_ui, 'checkBox_7'):
            metadata_directory["MRHY PMPVOL reads between 65 and 80 cc 2nd"] = "Completed" if step1_ui.checkBox_7.isChecked() else "Not completed"
        # Collect line edit values from second column

        if hasattr(step1_ui, 'lineEdit_12'):
            value = step1_ui.lineEdit_12.text().strip() or "Not entered"
            metadata_directory["Set Line Pressure 2"] = value
            
        if hasattr(step1_ui, 'lineEdit_11'):
            value = step1_ui.lineEdit_11.text().strip() or "Not entered"
            metadata_directory["Hydraulic Pressure 2"] = value
         
        # Add validation status for page 1
        metadata_directory["Page 1 Validation Status"] = "Completed successfully" if self.step1_page.isComplete() else "Incomplete"
        
        # ===== PAGE 2 METADATA =====
        # Get reference to the UI for page 2
        step2_ui = self.step2_page.ui

        if hasattr(step2_ui, 'lineEdit_1'):
            value = step2_ui.lineEdit_1.text().strip() or "Not entered"
            metadata_directory["Initial Resistivity"] = value

        if hasattr(step2_ui, 'lineEdit_2'):
            value = step2_ui.lineEdit_2.text().strip() or "Not entered"
            metadata_directory["Initial Temperature"] = value
        
        # Collect checkbox states for page 2
        if hasattr(step2_ui, 'checkBox_1'):
            metadata_directory["Pour Warm water with Salt solution in probe"] = "Done" if step2_ui.checkBox_1.isChecked() else "Not completed"
            
        # Collect radio button group 1 selection
        if hasattr(step2_ui, 'groupBox_1'):
            groupbox1_value = "None selected"
            if hasattr(step2_ui, 'radioButton_2') and step2_ui.radioButton_2.isChecked():
                groupbox1_value = "Yes"
            elif hasattr(step2_ui, 'radioButton_1') and step2_ui.radioButton_1.isChecked():
                groupbox1_value = "No"
                
            metadata_directory["Resistivity Values Change"] = groupbox1_value

        if hasattr(step2_ui, 'lineEdit_3'):
            value = step2_ui.lineEdit_3.text().strip() or "Not entered"
            metadata_directory["Updated Resistivity"] = value

        if hasattr(step2_ui, 'lineEdit_4'):
            value = step2_ui.lineEdit_4.text().strip() or "Not entered"
            metadata_directory["Updated Temperature"] = value
            
            
        # Collect line edit values from first measurement section
        if hasattr(step2_ui, 'lineEdit_7'):
            value = step2_ui.lineEdit_7.text().strip() or "Not entered"
            metadata_directory["Opened ISO Valves"]["Set line pressure"] = value
            
        if hasattr(step2_ui, 'lineEdit_8'):
            value = step2_ui.lineEdit_8.text().strip() or "Not entered"
            metadata_directory["Opened ISO Valves"]["Hydraulic pressure"] = value

           
        if hasattr(step2_ui, 'lineEdit_5'):
            value = step2_ui.lineEdit_5.text().strip() or "Not entered"
            metadata_directory["Closed Bypass Valves"]["Hydraulic pressure"] = value
            
        if hasattr(step2_ui, 'lineEdit_6'):
            value = step2_ui.lineEdit_6.text().strip() or "Not entered"
            metadata_directory["Closed Bypass Valves"]["Hydraulic pressure"] = value

        if hasattr(step2_ui, 'lineEdit_11'):
            value = step2_ui.lineEdit_11.text().strip() or "Not entered"
            metadata_directory["Opened Bypass Valves"]["Hydraulic pressure"] = value

        if hasattr(step2_ui, 'lineEdit_12'):
            value = step2_ui.lineEdit_12.text().strip() or "Not entered"
            metadata_directory["Opened Bypass Valves"]["Hydraulic pressure"] = value

        if hasattr(step2_ui, 'lineEdit_9'):
            value = step2_ui.lineEdit_9.text().strip() or "Not entered"
            metadata_directory["Closed ISO Valves"]["Hydraulic pressure"] = value

        if hasattr(step2_ui, 'lineEdit_10'):
            value = step2_ui.lineEdit_10.text().strip() or "Not entered"
            metadata_directory["Closed ISO Valves"]["Hydraulic pressure"] = value

        if hasattr(step2_ui, 'lineEdit_5'):
            value = step2_ui.lineEdit_5.text().strip() or "Not entered"
            metadata_directory["Closed Bypass Valves"]["Hydraulic pressure"] = value
            
        if hasattr(step2_ui, 'lineEdit_6'):
            value = step2_ui.lineEdit_6.text().strip() or "Not entered"
            metadata_directory["Closed Bypass Valves"]["Hydraulic pressure"] = value

        if hasattr(step2_ui, 'checkBox_6'):
            metadata_directory["Put MPMP jig on Probe and connect waterline with shop Air(~100psi)"] = "Completed" if step2_ui.checkBox_6.isChecked() else "Not completed"

        if hasattr(step2_ui, 'groupBox_2'):
            groupbox2_value = "None selected"
            if hasattr(step2_ui, 'radioButton_3') and step2_ui.radioButton_3.isChecked():
                groupbox2_value = "Yes"
            elif hasattr(step2_ui, 'radioButton_4') and step2_ui.radioButton_4.isChecked():
                groupbox2_value = "No"
                
            metadata_directory["Both Mini Flowline leak OK"] = groupbox2_value

        if hasattr(step2_ui, 'lineEdit_13'):
            value = step2_ui.lineEdit_13.text().strip() or "Not entered"
            metadata_directory["MPMP Jig on Probe"]["Hydraulic pressure"] = value

        if hasattr(step2_ui, 'lineEdit_14'):
            value = step2_ui.lineEdit_14.text().strip() or "Not entered"
            metadata_directory["MPMP Jig on Probe"]["Hydraulic pressure"] = value

        # Add validation status for page 2
        metadata_directory["Page 2 Validation Status"] = "Completed successfully" if self.step2_page.isComplete() else "Incomplete"
        
        # ===== PAGE 3 METADATA =====
        # Get reference to the UI for page 3
        step3_ui = self.step3_page.ui
        
        # Collect ISO valve checkbox
        if hasattr(step3_ui, 'checkBox_2'):
            metadata_directory["Opened the ISO Valve"] = "Completed" if step3_ui.checkBox_2.isChecked() else "Not completed"
            
        # Collect line edit values from pressure measurement
        if hasattr(step3_ui, 'lineEdit_2'):
            value = step3_ui.lineEdit_2.text().strip() or "Not entered"
            metadata_directory["Final Set Line Pressure"] = value
            
        if hasattr(step3_ui, 'lineEdit_4'):
            value = step3_ui.lineEdit_4.text().strip() or "Not entered"
            metadata_directory["Final Hydraulic Pressure"] = value
            
        # Collect pump functionality checkboxes
        if hasattr(step3_ui, 'checkBox_1'):
            metadata_directory["Connect Bottle Fill Tank to Probe Barrel"] = "Completed" if step3_ui.checkBox_1.isChecked() else "Not completed"
            
        # Collect MPMP usage selection
        if hasattr(step3_ui, 'groupBox_1'):
            groupbox1_value = "None selected"
            if hasattr(step3_ui, 'radioButton_2') and step3_ui.radioButton_2.isChecked():
                groupbox1_value = "Yes"
            elif hasattr(step3_ui, 'radioButton_1') and step3_ui.radioButton_1.isChecked():
                groupbox1_value = "No"
                
            metadata_directory["Using MPMP"] = groupbox1_value
            
        # Collect remaining checkboxes
        if hasattr(step3_ui, 'checkBox_4') and step3_ui.checkBox_4.isEnabled():
            metadata_directory["Connect Two Bottles to Air Adapter"] = "Completed" if step3_ui.checkBox_4.isChecked() else "Not completed"
            
        if hasattr(step3_ui, 'checkBox_3'):
            metadata_directory["Install Restrictor and Confirm Open"] = "Completed" if step3_ui.checkBox_3.isChecked() else "Not completed"
            
        # Add validation status for page 3
        metadata_directory["Page 3 Validation Status"] = "Completed successfully" if self.step3_page.isComplete() else "Incomplete"
        
        # Copy the metadata directory to the standard User Inputs field
        metadata["User Inputs"] = metadata_directory
        
        return metadata

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    wizard = Perform_MRPQ_c()
    wizard.show()

    sys.exit(app.exec())

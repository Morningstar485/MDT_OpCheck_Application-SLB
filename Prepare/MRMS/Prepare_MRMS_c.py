from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
from .Prepare_MRMS_1 import Ui_Dialog as MRMSStep1UI
from .Prepare_MRMS_2 import Ui_Dialog as MRMSStep2UI


class MRMSStep1Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("MRMS Preparation - Step 1")
        
        # Create layout and setup UI
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create UI instance and setup
        self.ui = MRMSStep1UI()
        from PySide6.QtWidgets import QWidget
        self.content_widget = QWidget()
        self.ui.setupUi(self.content_widget)
        layout.addWidget(self.content_widget)
        
        # Hide the original next button since we're using wizard navigation
        self.ui.pushButton.hide()
        
        # Connect signals for validation
        self.setup_validation()
        
    def setup_validation(self):
        """Setup validation signals for the complex workflow"""
        # Monitor all critical controls for completion
        self.ui.lineEdit_2.textChanged.connect(lambda: self.completeChanged.emit())
        
        # Connect all the existing sequential logic signals
        self.ui.radioButton_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_2.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_3.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_4.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_5.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_6.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_2.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_13.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_14.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_6.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_9.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_10.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_4.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_11.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_12.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_5.toggled.connect(lambda: self.completeChanged.emit())
        
    def isComplete(self):
        """Check if the page is complete based on the complex workflow"""
        # Check if lineEdit_2 has valid input (1-6)
        try:
            value = int(self.ui.lineEdit_2.text())
            if not (1 <= value <= 6):
                return False
        except (ValueError, AttributeError):
            return False
            
        # Verify that all required steps in the workflow are completed
        # Left column flow
        if not (self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()):
            return False
            
        # If No was selected in GB1, CB1 must be checked
        if self.ui.radioButton_2.isChecked() and not self.ui.checkBox_1.isChecked():
            return False
            
        # GB2 must have selection if enabled
        if self.ui.groupBox_2.isEnabled():
            if not (self.ui.radioButton_3.isChecked() or self.ui.radioButton_4.isChecked()):
                return False
                
        # GB3 must have selection if enabled
        if self.ui.groupBox_3.isEnabled():
            if not (self.ui.radioButton_5.isChecked() or self.ui.radioButton_6.isChecked()):
                return False
                
        # If Reverse Low Shock was selected, CB2 must be checked
        if self.ui.radioButton_6.isChecked() and not self.ui.checkBox_2.isChecked():
            return False
            
        # Right column flow
        if self.ui.groupBox_7.isEnabled():
            if not (self.ui.radioButton_13.isChecked() or self.ui.radioButton_14.isChecked()):
                return False
                
            # If Yes in GB7, CB6 must be checked
            if self.ui.radioButton_13.isChecked() and not self.ui.checkBox_6.isChecked():
                return False
                
        # GB5 validation if enabled
        if self.ui.groupBox_5.isEnabled():
            if not (self.ui.radioButton_9.isChecked() or self.ui.radioButton_10.isChecked()):
                return False
                
        # CB4 must be checked if enabled
        if self.ui.checkBox_4.isEnabled() and not self.ui.checkBox_4.isChecked():
            return False
            
        # GB6 validation if enabled
        if self.ui.groupBox_6.isEnabled():
            if not (self.ui.radioButton_11.isChecked() or self.ui.radioButton_12.isChecked()):
                return False
                
            # If No in GB6, CB5 must be checked
            if self.ui.radioButton_12.isChecked() and not self.ui.checkBox_5.isChecked():
                return False
        
        return True
        
    def nextId(self):
        """Always go to step 2"""
        return 1

class MRMSStep2Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("MRMS Preparation - Step 2")
        
        # Create layout and setup UI
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create UI instance and setup
        self.ui = MRMSStep2UI()
        from PySide6.QtWidgets import QWidget
        self.content_widget = QWidget()
        self.ui.setupUi(self.content_widget)
        layout.addWidget(self.content_widget)
        
        # Hide the original finish button since we're using wizard navigation
        self.ui.pushButton.hide()
        
        # Connect validation signals
        self.setup_validation()
        
    def setup_validation(self):
        """Setup validation for the sequential workflow"""
        # Connect all checkboxes and radio buttons
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_2.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_2.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_3.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_3.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_4.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_4.toggled.connect(lambda: self.completeChanged.emit())
        
    def isComplete(self):
        """Check if all required elements are completed"""
        # Both initial checkboxes must be checked
        if not (self.ui.checkBox_1.isChecked() and self.ui.checkBox_2.isChecked()):
            return False
            
        # GB1 must have a selection
        if not (self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()):
            return False
            
        # If No was selected in GB1, CB3 must be checked
        if self.ui.radioButton_2.isChecked() and not self.ui.checkBox_3.isChecked():
            return False
            
        # GB2 must have a selection
        if not (self.ui.radioButton_3.isChecked() or self.ui.radioButton_4.isChecked()):
            return False
            
        # If No was selected in GB2, CB4 must be checked
        if self.ui.radioButton_4.isChecked() and not self.ui.checkBox_4.isChecked():
            return False
            
        return True
        
    def nextId(self):
        """This is the final page"""
        return -1


class Prepare_MRMS_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRMS Preparation Workflow")
        self.resize(1200, 800)
        
        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Add pages
        self.addPage(MRMSStep1Page())
        self.addPage(MRMSStep2Page())
    
    def collect_step1_metadata(self):
        """Collect metadata from Step 1 UI elements (similar to EDTA pattern)"""
        page = self.page(0)
        if not page or not hasattr(page, 'ui'):
            return
        
        ui = page.ui
        
        # Collect GroupBox responses
        # SFT 275 availability check
        if ui.radioButton_1.isChecked():
            self.metadata_directory["SFT 275 Available with Special Tools"] = "Yes"
        elif ui.radioButton_2.isChecked():
            self.metadata_directory["SFT 275 Available with Special Tools"] = "No"
        
        # Collect checkbox data
        if ui.checkBox_1.isEnabled() and ui.checkBox_1.isChecked():
            self.metadata_directory["Informed Base about SFT 275"] = "Yes"
        
        # Collect data from enabled secondary GroupBoxes
        if ui.groupBox_2.isEnabled():
            if ui.radioButton_3.isChecked():
                self.metadata_directory["Oil Level Full"] = "Yes"
            elif ui.radioButton_4.isChecked():
                self.metadata_directory["Oil Level Full"] = "No"
        
        if ui.groupBox_3.isEnabled():
            if ui.radioButton_5.isChecked():
                self.metadata_directory["Sampling Type"] = "Low Shock"
            elif ui.radioButton_6.isChecked():
                self.metadata_directory["Sampling Type"] = "Mid Shock"

        if ui.checkBox_2.isEnabled() and ui.checkBox_2.isChecked():
            self.metadata_directory["Reverse Low Shock Verified"] = "Yes"
        
        # Right column data
        if ui.groupBox_7.isEnabled():
            if ui.radioButton_13.isChecked():
                self.metadata_directory["MRMS located above MRPO"] = "Yes"
            elif ui.radioButton_14.isChecked():
                self.metadata_directory["MRMS located above MRPO"] = "No"

            if ui.checkBox_6.isEnabled() and ui.checkBox_6.isChecked():
                self.metadata_directory["The relief valve plug (H730586) is installed in the lower waterline port"] = "Yes"
        
        if ui.groupBox_5.isEnabled():
            if ui.radioButton_9.isChecked():
                self.metadata_directory["Upper waterline port is used as an exit port only"] = "Yes"
            elif ui.radioButton_10.isChecked():
                self.metadata_directory["Upper waterline port is used as an exit port only"] = "No"
        
        if ui.checkBox_4.isEnabled() and ui.checkBox_4.isChecked():
            self.metadata_directory[ui.checkBox_4.text()] = "Done"

        if ui.groupBox_6.isEnabled():
            if ui.radioButton_11.isChecked():
                self.metadata_directory["Exit Screen Filter Available"] = "Yes"
            elif ui.radioButton_12.isChecked():
                self.metadata_directory["Exit Screen Filter Available"] = "No"

        if ui.checkBox_5.isEnabled() and ui.checkBox_5.isChecked():
            self.metadata_directory["Informed Base of Filter Unavailability"] = "Done"

        if ui.lineEdit_2.isEnabled():
            self.metadata_directory["No. of MPSR Planned"] = ui.lineEdit_2.text().strip()

    def collect_step2_metadata(self):
        """Collect metadata from Step 2 UI elements (similar to EDTA pattern)"""
        page = self.page(1)
        if not page or not hasattr(page, 'ui'):
            return
        
        ui = page.ui
        
        # Collect data from initial checkboxes
        if ui.checkBox_1.isChecked():
            self.metadata_directory["MPSR Installation Check"] = "Done"
        
        if ui.checkBox_2.isChecked():
            self.metadata_directory["Blank Crossover Plugs are Available"] = "Yes"
        
        # Collect GroupBox responses - Exit port adaptor
        if ui.groupBox_1.isEnabled():
            if ui.radioButton_1.isChecked():
                self.metadata_directory["MRMS Exit port adaptor available in SFT-275 for the Opcheck"] = "Yes"
            elif ui.radioButton_2.isChecked():
                self.metadata_directory["MRMS Exit port adaptor available in SFT-275 for the Opcheck"] = "No"
        
        # Collect checkbox data - Informed Base
        if ui.checkBox_3.isEnabled() and ui.checkBox_3.isChecked():
            self.metadata_directory["Informed Base About Exit Port Adaptor Unavailability"] = "Yes"
        
        # Collect GroupBox responses - Exo washer
        if ui.groupBox_2.isEnabled():
            if ui.radioButton_3.isChecked():
                self.metadata_directory["Exo Washer Available"] = "Yes"
            elif ui.radioButton_4.isChecked():
                self.metadata_directory["Exo Washer Available"] = "No"
        
        # Collect checkbox data - Informed Base and Raised Requirement
        if ui.checkBox_4.isEnabled() and ui.checkBox_4.isChecked():
            self.metadata_directory["Informed Base About Exo Washer Unavailability"] = "Yes"

    def get_mrms_data(self):
        """Collect data from all MRMS pages"""
        mrms_data = {}
        self.metadata_directory = {}
        
        # Collect data from Step 1
        if self.page(0):  # First page added
            step1_page = self.page(0)
            
            # Collect metadata using the EDTA pattern
            self.collect_step1_metadata()
            
            # Mark completion status
            mrms_data['step1_completed'] = True
        
        # Collect data from Step 2
        if self.page(1):  # Second page added
            step2_page = self.page(1)
            
            # Collect metadata from step 2
            self.collect_step2_metadata()
            
            # Mark completion status
            mrms_data['step2_completed'] = True
        
        # Include the combined metadata in the return value
        mrms_data["User Inputs"] = self.metadata_directory.copy()
        
        return mrms_data
    
    def get_data(self):
        """Standard method for metadata collection - calls get_mrms_data()"""
        return self.get_mrms_data()
        
    def get_metadata(self):
        """Standard method for metadata collection that matches the expected format"""
        return self.get_mrms_data()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    controller = Prepare_MRMS_c()
    controller.show()
    sys.exit(app.exec())

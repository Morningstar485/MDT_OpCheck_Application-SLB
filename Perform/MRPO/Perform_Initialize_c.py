from PySide6.QtWidgets import QWizard, QWizardPage
from .Perform_Initialize import Ui_Dialog


class MRPOInitializePage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Hide the original next button
        self.ui.pushButton.hide()
        
        # Connect to wizard validation using lambda to avoid argument passing
        self.ui.comboBox.currentTextChanged.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_2.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_5.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_6.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_3.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_4.toggled.connect(lambda: self.completeChanged.emit())
    
    def isComplete(self):
        """Validate the page completion based on original pushButton enabled state"""
        # MRPO validation: Sequential validation with Yes/No logic
        
        # Check combo box selection (must not be default)
        if self.ui.comboBox.currentIndex() == 0:  # "Select MRDU Type"
            return False
            
        # Check first group box - PO Initialize Ok?
        if not (self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()):
            return False
        
        # If "No" selected for PO Initialize, cannot proceed
        if self.ui.radioButton_2.isChecked():
            return False
            
        # Check second group box - PO Mode change Ok?
        if not (self.ui.radioButton_5.isChecked() or self.ui.radioButton_6.isChecked()):
            return False
            
        # If "No" selected for PO Mode change, cannot proceed
        if self.ui.radioButton_6.isChecked():
            return False
            
        # Check final MRPO type selection
        if not (self.ui.radioButton_3.isChecked() or self.ui.radioButton_4.isChecked()):
            return False
            
        return True


class Perform_Initialize_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRPO Initialize Wizard")
        self.resize(700, 450)
        
        # Create and add the page
        self.mrpo_page = MRPOInitializePage()
        self.addPage(self.mrpo_page)
        
    def get_metadata(self):
        """Collect metadata from the wizard"""
        metadata = {
            "Tool Name": "MRPO Initialize",
            "User Inputs": {}
        }

        # MRDU Type selection
        if self.mrpo_page.ui.comboBox.currentIndex() > 0:
            metadata["User Inputs"]["MRDU Type"] = self.mrpo_page.ui.comboBox.currentText()
        else:
            metadata["User Inputs"]["MRDU Type"] = "Not selected"
            
        # PO Initialize status
        if self.mrpo_page.ui.radioButton_1.isChecked():
            metadata["User Inputs"]["PO Initialize Status"] = "Ok - PO Initialize successful"
        elif self.mrpo_page.ui.radioButton_2.isChecked():
            metadata["User Inputs"]["PO Initialize Status"] = "Not Okay - PO Initialize failed, check Solenoid 3 status"
        else:
            metadata["User Inputs"]["PO Initialize Status"] = "Not checked"

        # PO Mode change status
        if self.mrpo_page.ui.radioButton_5.isChecked():
            metadata["PO Mode Change Status"] = "Yes"
        elif self.mrpo_page.ui.radioButton_6.isChecked():
            metadata["PO Mode Change Status"] = "No - PO Mode change failed, check Solenoid 1 & 2 status"
        else:
            metadata["PO Mode Change Status"] = "Not checked"

        # MRPO type
        if self.mrpo_page.ui.radioButton_3.isChecked():
            metadata["MRPO Purpose"] = "Sample Side MRPO"
        elif self.mrpo_page.ui.radioButton_4.isChecked():
            metadata["MRPO Purpose"] = "Guard Side MRPO"
        else:
            metadata["MRPO Purpose"] = "Not selected"

        metadata["Initialization Status"] = "All checks passed successfully" if self.mrpo_page.isComplete() else "Initialization incomplete or failed"

        return metadata

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    wizard = Perform_Initialize_c()
    wizard.show()
    sys.exit(app.exec())

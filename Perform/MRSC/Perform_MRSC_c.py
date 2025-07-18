from PySide6.QtWidgets import QWizard, QWizardPage
from .Perform_MRSC_1 import Ui_Dialog


class MRSCPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Hide the original next button
        self.ui.pushButton.hide()
        
        # Connect to wizard validation using lambda to avoid argument passing
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_6.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_7.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_8.textChanged.connect(lambda: self.completeChanged.emit())
    
    def isComplete(self):
        """Validate the page completion based on original pushButton enabled state"""
        # MRSC validation: ComboBox + Checkbox + Progressive lineEdit validation
        
        # Check combo box selection (must not be default)
        if self.ui.comboBox.currentIndex() == 0:  # "Select MRSC Type"
            return False
            
        # Check checkbox is checked
        if not self.ui.checkBox_1.isChecked():
            return False
            
        # Check lineEdit_6 (Open seal valve) - must be 122-138
        try:
            val6 = float(self.ui.lineEdit_6.text())
            if not (122 <= val6 <= 138):
                return False
        except ValueError:
            return False
            
        # Check lineEdit_7 (Close seal valve) - must be -5 to 5
        try:
            val7 = float(self.ui.lineEdit_7.text())
            if not (-5 <= val7 <= 5):
                return False
        except ValueError:
            return False
            
        # For Exit Port option, need lineEdit_8 validation too
        if self.ui.comboBox.currentIndex() == 3:  # Exit Port
            try:
                val8 = float(self.ui.lineEdit_8.text())
                if not (122 <= val8 <= 138):
                    return False
            except ValueError:
                return False
                
        return True


class Perform_MRSC_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRSC Perform Test Wizard")
        self.resize(650, 450)
        
        # Create and add the page
        self.mrsc_page = MRSCPage()
        self.addPage(self.mrsc_page)
        
    def get_metadata(self):
        """Collect metadata from the wizard"""
        metadata = {
            "Tool Name": "MRSC",
            "User Inputs": {}
        }
        
        # MRSC type selection
        if self.mrsc_page.ui.comboBox.currentIndex() > 0:
            metadata["User Inputs"]["MRSC Type"] = self.mrsc_page.ui.comboBox.currentText()
        else:
            metadata["User Inputs"]["MRSC Type"] = "Not selected"
            
        # Checkbox status
        metadata["User Inputs"]["Seal Valve Reset Status"] = "Completed" if self.mrsc_page.ui.checkBox_1.isChecked() else "Not completed"
        
        # Open seal valve reading
        open_valve_value = self.mrsc_page.ui.lineEdit_6.text()
        metadata["User Inputs"]["Open Seal Valve Reading"] = open_valve_value if open_valve_value else "Not entered"

        # Close seal valve reading
        close_valve_value = self.mrsc_page.ui.lineEdit_7.text()
        metadata["User Inputs"]["Close Seal Valve Reading"] = close_valve_value if close_valve_value else "Not entered"

        # Open seal valve (second) - only for Exit Port
        if self.mrsc_page.ui.comboBox.currentIndex() == 3:  # Exit Port
            second_open_value = self.mrsc_page.ui.lineEdit_8.text()
            metadata["User Inputs"]["Second Open Seal Valve Reading"] = second_open_value if second_open_value else "Not entered"
        else:
            metadata["User Inputs"]["Second Open Seal Valve Reading"] = "Not applicable for this MRSC type"
            
        # Validation ranges
        metadata["User Inputs"]["Validation Ranges"] = {
            "Open Seal Valve": "122-138",
            "Close Seal Valve": "-5 to +5",
            "Second Open Seal Valve": "122-138 (Exit Port only)"
        }

        metadata["User Inputs"]["Test Completion Status"] = "All validations passed successfully" if self.mrsc_page.isComplete() else "Test incomplete or validation failed"

        return metadata

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    wizard = Perform_MRSC_c()
    wizard.show()
    sys.exit(app.exec())

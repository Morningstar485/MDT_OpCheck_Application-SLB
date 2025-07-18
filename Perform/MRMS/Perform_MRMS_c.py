from PySide6.QtWidgets import QWizard, QWizardPage
from .Perform_MRMS_1 import Ui_Dialog


class MRMSPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Hide the original next button
        self.ui.pushButton.hide()
        
        # Connect to wizard validation using lambda to avoid argument passing
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_1.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_2.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_3.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_4.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_5.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_6.textChanged.connect(lambda: self.completeChanged.emit())
    
    def isComplete(self):
        """Validate the page completion based on original pushButton enabled state"""
        # The original logic enables pushButton when all validation chains pass
        if not self.ui.checkBox_1.isChecked():
            return False
            
        # Check progressive validation chain (same as original)
        if not self.ui.values_permissible_frame7():
            return False
            
        if not self.ui.values_permissible_frame8():
            return False
            
        if not self.ui.values_permissible_frame11():
            return False
            
        return True
class Perform_MRMS_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MRMS Test")
        self.setWizardStyle(QWizard.ModernStyle)
        self.resize(550, 500)
        
        # Add the test page
        self.mrms_page = MRMSPage()
        self.addPage(self.mrms_page)
    
    def get_metadata(self):
        """Collect descriptive metadata from the MRMS test"""
        metadata = {
            "Tool Name": "MRMS",
            "User Inputs": {
                "Initialization Status": "Completed" if self.mrms_page.ui.checkBox_1.isChecked() else "Not performed",
                "USV Open Valve 1": self.mrms_page.ui.lineEdit_1.text() or "Not entered",
                "LSV Open Valve 1": self.mrms_page.ui.lineEdit_2.text() or "Not entered",
                "USV Closed Valve 1": self.mrms_page.ui.lineEdit_3.text() or "Not entered",
                "LSV Closed Valve 1": self.mrms_page.ui.lineEdit_4.text() or "Not entered",
                "USV Open Valve 2": self.mrms_page.ui.lineEdit_5.text() or "Not entered",
                "LSV Closed Valve 2": self.mrms_page.ui.lineEdit_6.text() or "Not entered",
                "Validation Status": "All values within acceptable ranges" if self.mrms_page.isComplete() else "Validation incomplete"
            }
        }
        return metadata

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    wizard = Perform_MRMS_c()
    wizard.show()
    sys.exit(app.exec())
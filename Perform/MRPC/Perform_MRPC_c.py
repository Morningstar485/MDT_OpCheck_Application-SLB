from PySide6.QtWidgets import QWizard, QWizardPage
from .Perform_MRPC_1 import Ui_Dialog


class MRPCPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Hide the original next button
        self.ui.pushButton.hide()
        
        # Connect to wizard validation using lambda to avoid argument passing
        self.ui.lineEdit_1.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_2.textChanged.connect(lambda: self.completeChanged.emit())
        self.ui.lineEdit_3.textChanged.connect(lambda: self.completeChanged.emit())
    
    def isComplete(self):
        """Validate the page completion based on original pushButton enabled state"""
        # MRPC validation: Progressive enabling through voltage readings
        # 5V Reading (5.39-5.61) → +15V Reading (14.7-15.3) → -15V Reading (-15.3 to -14.7)
        
        # Check 5V reading first
        try:
            val1 = float(self.ui.lineEdit_1.text())
            if not (5.39 <= val1 <= 5.61):
                return False
        except ValueError:
            return False
            
        # Check +15V reading 
        try:
            val2 = float(self.ui.lineEdit_2.text())
            if not (14.7 <= val2 <= 15.3):
                return False
        except ValueError:
            return False
            
        # Check -15V reading
        try:
            val3 = float(self.ui.lineEdit_3.text())
            if not (-15.3 <= val3 <= -14.7):
                return False
        except ValueError:
            return False
            
        return True


class Perform_MRPC_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRPC Test Wizard")
        self.resize(500, 240)
        
        # Create and add the page
        self.mrpc_page = MRPCPage()
        self.addPage(self.mrpc_page)
        
    def get_metadata(self):
        """Collect metadata from the wizard"""
        metadata = {
            "Tool Name": "MRPC",
            "User Inputs": {
                "5V Reading": self.mrpc_page.ui.lineEdit_1.text() or "Not entered",
                "+15V Reading": self.mrpc_page.ui.lineEdit_2.text() or "Not entered", 
                "-15V Reading": self.mrpc_page.ui.lineEdit_3.text() or "Not entered",
                "Voltage Validation Status": "All voltage readings within acceptable ranges" if self.mrpc_page.isComplete() else "Validation incomplete"
            }
        }
        return metadata

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    wizard = Perform_MRPC_c()
    wizard.show()
    sys.exit(app.exec())

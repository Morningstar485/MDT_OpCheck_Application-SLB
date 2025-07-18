from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from .Prepare_MRFA_1 import Ui_Dialog as MRFAStepUI


class MRFAPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("MRFA Preparation")
        
        # Create layout and setup UI
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create UI instance and setup
        self.ui = MRFAStepUI()
        from PySide6.QtWidgets import QWidget
        self.content_widget = QWidget()
        self.ui.setupUi(self.content_widget)
        layout.addWidget(self.content_widget)
        
        # Hide the original next button since we're using wizard navigation
        self.ui.pushButton.hide()
        
        # Connect signals for validation
        self.setup_validation()
        
    def setup_validation(self):
        """Setup validation signals based on MRFA validation logic"""
        # Connect radio buttons to validation
        self.ui.radioButton_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_2.toggled.connect(lambda: self.completeChanged.emit())
        
        # Connect checkbox to validation
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        
    def isComplete(self):
        """Check if the page is complete based on MRFA validation logic"""
        # Use the same logic as the original MRFA validation
        if self.ui.radioButton_1.isChecked():
            # "Yes" selected - form complete
            return True
        elif self.ui.radioButton_2.isChecked() and self.ui.checkBox_1.isChecked():
            # "No" selected and acknowledgment checkbox checked - form complete
            return True
        else:
            # Form not complete
            return False


class Prepare_MRFA_c(QWizard):
    """
    MRFA Prepare Wizard Controller
    Simple QWizard implementation with validation logic and metadata collection
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRFA Preparation Wizard")
        self.resize(340, 380)
        
        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Add pages
        self.addPage(MRFAPage())
    
    def collect_metadata(self):
        """Collect metadata from MRFA UI elements"""
        page = self.page(0)
        if not page or not hasattr(page, 'ui'):
            return
        
        ui = page.ui
        self.metadata_directory.clear()
        
        # Collect GroupBox responses
        self._collect_groupbox_data(ui)
        
        # Collect error frame data (only if checkboxes are enabled)
        self._collect_error_frame_data(ui)
    
    def _collect_groupbox_data(self, ui):
        """Collect data from groupboxes"""
        # GroupBox 6: "Is the valid calibration job spec file available?"
        if ui.radioButton_1.isChecked():
            self.metadata_directory["Valid calibration job spec file available"] = "Yes"
        elif ui.radioButton_2.isChecked():
            self.metadata_directory["Valid calibration job spec file available"] = "No"

    def _collect_error_frame_data(self, ui):
        """Collect error frame data only if checkboxes are enabled"""
        # CheckBox 1 and its corresponding error frame (shown when No is selected)
        if ui.checkBox_1.isEnabled() and ui.checkBox_1.isChecked():
            self.metadata_directory["Downloaded from Maximo CA1 Job Spec File"] = "done"

    def get_data(self):
        """Get data for metadata integration"""
        # Collect current metadata
        self.collect_metadata()
        
        page = self.page(0)
        return {
            "Tool Name": "MRFA",
            "Completed": True,
            "User Choices": self.metadata_directory.copy()
        }
    
    def get_metadata_directory(self):
        """Get the metadata directory for report generation"""
        self.collect_metadata()
        return self.metadata_directory.copy()


# For testing
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    
    wizard = Prepare_MRFA_c()
    wizard.show()
    
    sys.exit(app.exec())

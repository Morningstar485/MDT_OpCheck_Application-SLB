from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from .Prepare_EDTC_1 import Ui_Dialog as EDTCStepUI


class EDTCPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("EDTC Preparation")
        
        # Create layout and setup UI
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create UI instance and setup
        self.ui = EDTCStepUI()
        from PySide6.QtWidgets import QWidget
        self.content_widget = QWidget()
        self.ui.setupUi(self.content_widget)
        layout.addWidget(self.content_widget)
        
        # Hide the original next button since we're using wizard navigation
        # self.ui.pushButton.hide()
        
        # Connect signals for validation
        self.setup_validation()
        
    def setup_validation(self):
        """Setup validation signals based on EDTC validation logic"""
        # Connect checkboxes to validation
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_2.toggled.connect(lambda: self.completeChanged.emit())
        
        # Connect radio buttons for final validation
        self.ui.radioButton_9.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_10.toggled.connect(lambda: self.completeChanged.emit())
        
    def isComplete(self):
        """Check if the page is complete based on EDTC validation logic"""
        # First checkbox must be checked
        if not self.ui.checkBox_1.isChecked():
            return False
            
        # Use the same logic as the original EDTC check_completion
        if self.ui.radioButton_9.isChecked():
            # "Yes" selected - form complete
            return True
        elif self.ui.radioButton_10.isChecked() and self.ui.checkBox_2.isChecked():
            # "No" selected and acknowledgment checkbox checked - form complete
            return True
        else:
            # Form not complete
            return False


class Prepare_EDTC_c(QWizard):
    """
    EDTC Prepare Wizard Controller
    Simple QWizard implementation with validation logic and metadata collection
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("EDTC Preparation Wizard")
        self.resize(390, 400)
        
        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Add pages
        self.addPage(EDTCPage())
    
    def collect_metadata(self):
        """Collect metadata from EDTC UI elements"""
        page = self.page(0)
        if not page or not hasattr(page, 'ui'):
            return
        
        ui = page.ui
        self.metadata_directory.clear()
        
        # Collect initial checkbox response
        self._collect_initial_checkbox_data(ui)
        
        # Collect GroupBox responses
        self._collect_groupbox_data(ui)
        
        # Collect error frame data (only if checkboxes are enabled)
        self._collect_error_frame_data(ui)
    
    def _collect_initial_checkbox_data(self, ui):
        """Collect data from initial checkbox"""
        if ui.checkBox_1.isChecked():
            self.metadata_directory["Check EDTC code for MDT - Need EDTC-B for the MDT job"] = "checked"
    
    def _collect_groupbox_data(self, ui):
        """Collect data from groupboxes"""
        # GroupBox 6: "Is the Gamma Ray Jig Available?"
        if ui.radioButton_9.isChecked():
            self.metadata_directory["Is the Gamma Ray Jig Available?"] = "Yes"
        elif ui.radioButton_10.isChecked():
            self.metadata_directory["Is the Gamma Ray Jig Available?"] = "No"
    
    def _collect_error_frame_data(self, ui):
        """Collect error frame data only if checkboxes are enabled"""
        # CheckBox 2 and its corresponding error frame (shown when No is selected)
        if ui.checkBox_2.isEnabled() and ui.checkBox_2.isChecked():
            self.metadata_directory["Inform PSD/JDL/Foreman"] = "done"

    def get_data(self):
        """Get data for metadata integration"""
        # Collect current metadata
        self.collect_metadata()
        
        page = self.page(0)
        return {
            "Tool Name": "EDTC",
            "Completed": True,
            "User Inputs": self.metadata_directory.copy()
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
    
    wizard = Prepare_EDTC_c()
    wizard.show()
    
    sys.exit(app.exec())

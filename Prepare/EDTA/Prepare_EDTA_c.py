from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from .Prepare_EDTA_1 import Ui_Dialog as EDTAStepUI


class EDTAPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("EDTA Preparation")
        
        # Create layout and setup UI
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create UI instance and setup
        self.ui = EDTAStepUI()
        from PySide6.QtWidgets import QWidget
        self.content_widget = QWidget()
        self.ui.setupUi(self.content_widget)
        layout.addWidget(self.content_widget)
        
        # Hide the original next button since we're using wizard navigation
        self.ui.pushButton.hide()
        
        # Connect signals for validation
        self.setup_validation()
        
    def setup_validation(self):
        """Setup validation signals based on EDTA validation logic"""
        # Connect all checkboxes to validation
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_2.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_3.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_4.toggled.connect(lambda: self.completeChanged.emit())
        
        # Connect radio buttons for final validation
        self.ui.radioButton_9.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_10.toggled.connect(lambda: self.completeChanged.emit())
        
    def isComplete(self):
        """Check if the page is complete based on EDTA validation logic"""
        # Use the same logic as the original EDTA check_form_completion
        if self.ui.radioButton_9.isChecked():
            # "Yes" selected - form complete
            return True
        elif self.ui.radioButton_10.isChecked() and self.ui.checkBox_4.isChecked():
            # "No" selected and acknowledgment checkbox checked - form complete
            return True
        else:
            # Form not complete
            return False


class Prepare_EDTA_c(QWizard):
    """
    EDTA Prepare Wizard Controller
    Simple QWizard implementation with validation logic and metadata collection
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("EDTA Preparation Wizard")
        self.setMinimumSize(680, 800)
        
        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Add pages
        self.addPage(EDTAPage())
    
    def collect_metadata(self):
        """Collect metadata from EDTA UI elements"""
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
        # GroupBox 1: "Is EDTA available in with MDT Set?"
        if ui.radioButton_1.isChecked():
            self.metadata_directory["Is EDTA available in with MDT Set?"] = "Yes"
        elif ui.radioButton_2.isChecked():
            self.metadata_directory["Is EDTA available in with MDT Set?"] = "No"
        
        # GroupBox 2: "MRPP and MRTM with cable, are 2 sets available?"
        if ui.radioButton_3.isChecked():
            self.metadata_directory["MRPP and MRTM with cable, are 2 sets available?"] = "Yes"
        elif ui.radioButton_4.isChecked():
            self.metadata_directory["MRPP and MRTM with cable, are 2 sets available?"] = "No"
        
        # GroupBox 3: "MDT Lifting cap available?"
        if ui.radioButton_5.isChecked():
            self.metadata_directory["MDT Lifting cap available?"] = "Yes"
        elif ui.radioButton_6.isChecked():
            self.metadata_directory["MDT Lifting cap available?"] = "No"
        
        # GroupBox 4: "MDT Vertical make up plate available?"
        if ui.radioButton_7.isChecked():
            self.metadata_directory["MDT Vertical make up plate available?"] = "Yes"
        elif ui.radioButton_8.isChecked():
            self.metadata_directory["MDT Vertical make up plate available?"] = "No"
        
        # GroupBox 5: "Sample draining equipment available?"
        if ui.radioButton_9.isChecked():
            self.metadata_directory["Sample draining equipment available?"] = "Yes"
        elif ui.radioButton_10.isChecked():
            self.metadata_directory["Sample draining equipment available?"] = "No"
    
    def _collect_error_frame_data(self, ui):
        """Collect error frame data only if checkboxes are enabled"""
        # CheckBox 1 and its corresponding error frame
        if ui.checkBox_1.isEnabled() and ui.checkBox_1.isChecked():
            self.metadata_directory["Inform Base about MRPP and MRTM with cable"] = "Done"
        
        # CheckBox 2 and its corresponding error frame  
        if ui.checkBox_2.isEnabled() and ui.checkBox_2.isChecked():
            self.metadata_directory["Inform Base about lifting cap"] = "Done"
        
        # CheckBox 3 and its corresponding error frame
        if ui.checkBox_3.isEnabled() and ui.checkBox_3.isChecked():
            self.metadata_directory["Inform Base about Vertical Makeup Plate"] = "Done"

        # CheckBox 4 and its corresponding error frame
        if ui.checkBox_4.isEnabled() and ui.checkBox_4.isChecked():
            self.metadata_directory["Inform Base about Sample draining equipment"] = "Done"

    def get_data(self):
        """Get data for metadata integration"""
        # Collect current metadata
        self.collect_metadata()
        
        page = self.page(0)
        return {
            "Tool Name": "EDTA",
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
    
    wizard = Prepare_EDTA_c()
    wizard.show()
    
    sys.exit(app.exec())

from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from .Prepare_MRBN_1 import Ui_Dialog as MRBNStepUI


class MRBNPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("MRBN Preparation")
        
        # Create layout and setup UI
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create UI instance and setup
        self.ui = MRBNStepUI()
        from PySide6.QtWidgets import QWidget
        self.content_widget = QWidget()
        self.ui.setupUi(self.content_widget)
        layout.addWidget(self.content_widget)
        
        # Hide the original next button since we're using wizard navigation
        self.ui.pushButton.hide()
        
        # Connect signals for validation
        self.setup_validation()
        
    def setup_validation(self):
        """Setup validation signals based on MRBN validation logic"""
        # Connect radio buttons to validation
        self.ui.radioButton_10.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.radioButton_11.toggled.connect(lambda: self.completeChanged.emit())
        
        # Connect checkboxes to validation
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_2.toggled.connect(lambda: self.completeChanged.emit())
        
    def isComplete(self):
        """Check if the page is complete based on MRBN validation logic"""
        # Sequential validation: All steps must be completed
        
        # Step 1: Radio button must be selected
        if not (self.ui.radioButton_10.isChecked() or self.ui.radioButton_11.isChecked()):
            return False
            
        # Step 2: First checkbox must be checked
        if not self.ui.checkBox_1.isChecked():
            return False
            
        # Step 3: Second checkbox must be checked
        if not self.ui.checkBox_2.isChecked():
            return False
            
        return True


class Prepare_MRBN_c(QWizard):
    """
    MRBN Prepare Wizard Controller
    Simple QWizard implementation with validation logic and metadata collection
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRBN Preparation Wizard")
        self.resize(610, 500)
        
        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Add pages
        self.addPage(MRBNPage())
    
    def collect_metadata(self):
        """Collect metadata from MRBN UI elements"""
        page = self.page(0)
        if not page or not hasattr(page, 'ui'):
            return
        
        ui = page.ui
        self.metadata_directory.clear()
        
        # Collect GroupBox responses
        self._collect_groupbox_data(ui)
        
        # Collect checkbox responses
        self._collect_checkbox_data(ui)
    
    def _collect_groupbox_data(self, ui):
        """Collect data from groupboxes"""
        # GroupBox 4: "22-Socket Pin"
        if ui.radioButton_10.isChecked():
            self.metadata_directory["22-Socket Pin"] = "No damage at surface"
        elif ui.radioButton_11.isChecked():
            self.metadata_directory["22-Socket Pin"] = "Rederessed/Replaced damaged parts"
    
    def _collect_checkbox_data(self, ui):
        """Collect checkbox data"""
        # CheckBox 1: "Drain Plug is installed"
        if ui.checkBox_1.isChecked():
            self.metadata_directory["Drain Plug is installed"] = "Done"

        # CheckBox 2: "All the resistances follow guide"
        if ui.checkBox_2.isChecked():
            self.metadata_directory["All the resistances follow guide"] = "Done"

    def get_data(self):
        """Get data for metadata integration"""
        # Collect current metadata
        self.collect_metadata()
        
        page = self.page(0)
        return {
            "Tool Name": "MRBN",
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
    
    wizard = Prepare_MRBN_c()
    wizard.show()
    
    sys.exit(app.exec())

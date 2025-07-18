from PySide6.QtWidgets import QWizard, QWizardPage, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from .Prepare_MRHY_1 import Ui_Dialog as MRHYStepUI


class MRHYPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("MRHY Preparation")
        
        # Create layout and setup UI
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create UI instance and setup
        self.ui = MRHYStepUI()
        from PySide6.QtWidgets import QWidget
        self.content_widget = QWidget()
        self.ui.setupUi(self.content_widget)
        layout.addWidget(self.content_widget)
        
        # Hide the original next button since we're using wizard navigation
        self.ui.pushButton.hide()
        
        # Connect signals for validation
        self.setup_validation()
        
    def setup_validation(self):
        """Setup validation signals based on MRHY validation logic"""
        # Connect all checkboxes to validation
        self.ui.checkBox_1.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_2.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_3.toggled.connect(lambda: self.completeChanged.emit())
        self.ui.checkBox_4.toggled.connect(lambda: self.completeChanged.emit())
        
    def isComplete(self):
        """Check if the page is complete based on MRHY validation logic"""
        # Sequential validation: All 4 checkboxes must be checked in order
        return (self.ui.checkBox_1.isChecked() and 
                self.ui.checkBox_2.isChecked() and 
                self.ui.checkBox_3.isChecked() and 
                self.ui.checkBox_4.isChecked())


class Prepare_MRHY_c(QWizard):
    """
    MRHY Prepare Wizard Controller
    Simple QWizard implementation with validation logic and metadata collection
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRHY Preparation Wizard")
        self.resize(620, 400)
        
        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Add pages
        self.addPage(MRHYPage())
    
    def collect_metadata(self):
        """Collect metadata from MRHY UI elements"""
        page = self.page(0)
        if not page or not hasattr(page, 'ui'):
            return
        
        ui = page.ui
        self.metadata_directory.clear()
        
        # Collect checkbox responses
        self._collect_checkbox_data(ui)
        
        # Collect InTouch download action
        self._collect_intouch_data(ui)
    
    def _collect_checkbox_data(self, ui):
        """Collect data from checkboxes"""
        # CheckBox 1: Hydraulic plugs/stabbers check
        if ui.checkBox_1.isChecked():
            self.metadata_directory["Hydraulic plugs/stabbers are in the correct location and type for the HY/PS/PQ configuration"] = "True"
        
        # CheckBox 2: ADV closure check
        if ui.checkBox_2.isChecked():
            self.metadata_directory["ADV is closed"] = "Done"
        
        # CheckBox 3: Compensator pistons check
        if ui.checkBox_3.isChecked():
            self.metadata_directory["Compensator pistons are clean and not stuck"] = "Done"
        
        # CheckBox 4: Oil level check
        if ui.checkBox_4.isChecked():
            self.metadata_directory["Oil level is full and three (3) springs can be seen"] = "Done"

    def get_data(self):
        """Get data for metadata integration"""
        # Collect current metadata
        self.collect_metadata()
        
        page = self.page(0)
        return {
            "Tool Name": "MRHY",
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
    
    wizard = Prepare_MRHY_c()
    wizard.show()
    
    sys.exit(app.exec())

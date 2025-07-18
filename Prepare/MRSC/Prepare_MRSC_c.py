from PySide6.QtWidgets import QWizard, QWizardPage
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from .Prepare_MRSC_1 import Ui_Dialog


class MRSCPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Hide the original finish button
        self.ui.pushButton.hide()
        
        # Connect InTouch button
        self.ui.pushButton_2.clicked.connect(self.open_intouch)
        
    def open_intouch(self):
        """Open InTouch application"""
        url = QUrl("https://intouchsupport.com/index.cfm?event=content.preview&contentId=7104273&FromRefPage=Y")
        QDesktopServices.openUrl(url)
    
    def isComplete(self):
        """Validate the page completion based on the original UI logic"""
        # Check if groupBox_6 (MRSC preparation type) has selection
        if not (self.ui.radioButton_1.isChecked() or 
                self.ui.radioButton_2.isChecked() or 
                self.ui.radioButton_3.isChecked()):
            return False
            
        # For Low Shock and Water Receptacle (options 1 & 2), skip groupBox_7
        # and go directly to oil level check
        if self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked():
            # Check groupBox_2 (oil level) has selection and is "Yes"
            if not self.ui.radioButton_6.isChecked():
                return False
        
        # For Exit Port (option 3), need to check exit screen filter first
        elif self.ui.radioButton_3.isChecked():
            # Check groupBox_7 (exit screen filter) has selection
            if not (self.ui.radioButton_4.isChecked() or self.ui.radioButton_5.isChecked()):
                return False
                
            # If "Yes" selected for filter, check oil level
            if self.ui.radioButton_4.isChecked():
                # Check groupBox_2 (oil level) has "Yes" selection
                if not self.ui.radioButton_6.isChecked():
                    return False
            
            # If "No" selected for filter, workflow cannot complete
            # (need filter from Base)
            elif self.ui.radioButton_5.isChecked():
                return False
        
        return True


class Prepare_MRSC_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRSC Preparation Wizard")
        self.resize(600, 600)
        
        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Create and add the page
        self.mrsc_page = MRSCPage()
        self.addPage(self.mrsc_page)
        
    def collect_metadata(self):
        """Collect metadata from the wizard, similar to MRFA pattern"""
        self.metadata_directory.clear()
        
        # MRSC preparation type
        if self.mrsc_page.ui.radioButton_1.isChecked():
            self.metadata_directory["MRSC Preparation Type"] = "Low Shock"
        elif self.mrsc_page.ui.radioButton_2.isChecked():
            self.metadata_directory["MRSC Preparation Type"] = "Water Receptacle"
        elif self.mrsc_page.ui.radioButton_3.isChecked():
            self.metadata_directory["MRSC Preparation Type"] = "Exit Port"

        # Exit screen filter availability (only for Exit Port configuration)
        if self.mrsc_page.ui.radioButton_3.isChecked():
            if self.mrsc_page.ui.radioButton_4.isChecked():
                self.metadata_directory["Exit screen filter is available"] = "Yes"
            elif self.mrsc_page.ui.radioButton_5.isChecked():
                self.metadata_directory["Exit screen filter is available"] = "No - Need to request filter from Base"

        # Oil level status
        if self.mrsc_page.ui.radioButton_6.isChecked():
            self.metadata_directory["Oil Level Status"] = "Full, piston in top position against retaining ring"
        elif self.mrsc_page.ui.radioButton_7.isChecked():
            self.metadata_directory["Oil Level Status"] = "No - Oil level is low, requires filling"
    
    def get_data(self):
        """Get data for metadata integration, following MRFA pattern"""
        # Collect current metadata
        self.collect_metadata()
        
        return {
            "Tool Name": "MRSC",
            "Completed": True,
            "User Choices": self.metadata_directory.copy()
        }
    
    def get_metadata_directory(self):
        """Get the metadata directory for report generation"""
        self.collect_metadata()
        return self.metadata_directory.copy()
        
    def get_metadata(self):
        """Collect metadata from the wizard - for backwards compatibility"""
        self.collect_metadata()
        return self.metadata_directory.copy()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    wizard = Prepare_MRSC_c()
    wizard.show()
    sys.exit(app.exec())
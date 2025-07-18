from PySide6.QtWidgets import QApplication, QWizard, QWizardPage
from .Prepare_MRPO_1 import Ui_Dialog as Ui_MRPO1
from .Prepare_MRPO_2_UD import Ui_Dialog as Ui_MRPO2_UD
from .Prepare_MRPO_2_IO import Ui_Dialog as Ui_MRPO2_IO
from .Prepare_MRPO_3 import Ui_Dialog as Ui_MRPO3

class MRPOStep1Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPO1()
        self.ui.setupUi(self)
        self.setTitle("MRPO Prepare Step 1 - Configuration Selection")
        self.setMinimumSize(314, 300)  # Matching original dialog size
        
        # Connect validation triggers
        validation_elements = [
            'radioButton_1', 'radioButton_2', 'comboBox', 
            'radioButton_5', 'radioButton_6'
        ]
        
        for element_name in validation_elements:
            if hasattr(self.ui, element_name):
                element = getattr(self.ui, element_name)
                if hasattr(element, 'toggled'):  # RadioButton
                    element.toggled.connect(self.checkValidation)
                elif hasattr(element, 'currentIndexChanged'):  # ComboBox
                    element.currentIndexChanged.connect(self.checkValidation)
                    
    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton.isEnabled()

    def nextId(self):
        """Determine which page to show next based on radio button selection"""
        if self.ui.radioButton_5.isChecked():  # UP/DOWN selected
            return 1  # Go to MRPO_2_UD page
        elif self.ui.radioButton_6.isChecked():  # IN/OUT selected
            return 2  # Go to MRPO_2_IO page


class MRPOStep2UDPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPO2_UD()
        self.ui.setupUi(self)
        self.setTitle("MRPO Prepare Step 2 - UP/DOWN Configuration")
        self.setMinimumSize(530, 190)  # Matching original dialog size
        
        # Connect validation triggers
        validation_elements = ['checkBox_1', 'checkBox_2', 'checkBox_3']
        
        for element_name in validation_elements:
            if hasattr(self.ui, element_name):
                element = getattr(self.ui, element_name)
                if hasattr(element, 'stateChanged'):  # CheckBox
                    element.stateChanged.connect(self.checkValidation)

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton_2 is enabled"""
        return self.ui.pushButton_2.isEnabled()

    def nextId(self):
        """Always go to MRPO_3 after UP/DOWN configuration"""
        return 3  # Go to MRPO_3 page


class MRPOStep2IOPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPO2_IO()
        self.ui.setupUi(self)
        self.setTitle("MRPO Prepare Step 2 - IN/OUT Configuration")
        self.setMinimumSize(517, 391)  # Matching original dialog size
        
        # Connect validation triggers
        validation_elements = [
            'checkBox_1', 'checkBox_2', 'checkBox_3', 
            'radioButton_1', 'radioButton_2', 'checkBox_4'
        ]
        
        for element_name in validation_elements:
            if hasattr(self.ui, element_name):
                element = getattr(self.ui, element_name)
                if hasattr(element, 'stateChanged'):  # CheckBox
                    element.stateChanged.connect(self.checkValidation)
                elif hasattr(element, 'toggled'):  # RadioButton
                    element.toggled.connect(self.checkValidation)

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton_2 is enabled"""
        return self.ui.pushButton_2.isEnabled()

    def nextId(self):
        """Always go to MRPO_3 after IN/OUT configuration"""
        return 3  # Go to MRPO_3 page


class MRPOStep3Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPO3()
        self.ui.setupUi(self)
        self.setTitle("MRPO Prepare Step 3 - Final Checks")
        self.setMinimumSize(579, 465)  # Matching original dialog size
        
        # Connect validation triggers
        validation_elements = ['checkBox_1', 'checkBox_2', 'checkBox_3']
        
        for element_name in validation_elements:
            if hasattr(self.ui, element_name):
                element = getattr(self.ui, element_name)
                if hasattr(element, 'stateChanged'):  # CheckBox
                    element.stateChanged.connect(self.checkValidation)

    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Override isComplete to check if the internal pushButton is enabled"""
        return self.ui.pushButton.isEnabled()

    def nextId(self):
        """This is the final page - no next page"""
        return -1  # No next page, this is the final page


class Prepare_MRPO_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Prepare MRPO Wizard")
        self.resize(1200, 800)

        # Initialize metadata directory
        self.metadata_directory = {}
        
        # Track visited pages
        self.visited_pages = set()
        
        # Add all pages with explicit IDs
        step1_page = MRPOStep1Page()
        step2_ud_page = MRPOStep2UDPage()
        step2_io_page = MRPOStep2IOPage()
        step3_page = MRPOStep3Page()
        
        self.setPage(0, step1_page)    # Page 0 - Initial selection
        self.setPage(1, step2_ud_page) # Page 1 - UP/DOWN
        self.setPage(2, step2_io_page) # Page 2 - IN/OUT
        self.setPage(3, step3_page)    # Page 3 - Final

        # Set wizard options for proper navigation
        self.setWizardStyle(QWizard.ModernStyle)
        self.setOption(QWizard.HaveNextButtonOnLastPage, False)
        self.setOption(QWizard.HaveFinishButtonOnEarlyPages, False)
        
        # Start with first page
        self.setStartId(0)
        
        # Connect done signal to ensure metadata is collected
        self.finished.connect(self.on_wizard_finished)
        
        # Track page changes to record visited pages
        self.currentIdChanged.connect(self.track_visited_page)

    def track_visited_page(self, page_id):
        """Track which pages have been visited"""
        if page_id >= 0:
            self.visited_pages.add(page_id)
            
    def get_visited_pages(self):
        """Return list of visited page IDs"""
        # Always include current page
        if self.currentId() >= 0:
            self.visited_pages.add(self.currentId())
        return list(self.visited_pages)

    # Metadata collection methods
    def get_mrpo_data(self):
        """Collect data from all MRPO pages"""
        mrpo_data = {
            "User Choices": {},
            "test_results": {},
            "validation_results": {}
        }
        self.metadata_directory = {}
        
        # Collect data from Step 1 (Page 0)
        if self.page(0):
            # Collect metadata using the MRMS pattern
            self.collect_page0_metadata()
            
            # Mark completion status
            mrpo_data['test_results']['page0_completed'] = True
            
        # Get list of visited pages
        visited_page_ids = self.get_visited_pages()
        
        # Collect data from UP/DOWN page if it was used
        if self.page(1) and 1 in visited_page_ids:
            self.collect_page1_ud_metadata()
            mrpo_data['test_results']['page1_ud_completed'] = True
                
        # Collect data from IN/OUT page if it was used
        if self.page(2) and 2 in visited_page_ids:
            self.collect_page2_io_metadata()
            mrpo_data['test_results']['page2_io_completed'] = True
                
        # Collect data from final page
        if self.page(3) and 3 in visited_page_ids:
            self.collect_page3_metadata()
            mrpo_data['test_results']['page3_completed'] = True
            
        # Include the combined metadata in the return value
        mrpo_data["User Choices"] = self.metadata_directory.copy()
        
        # Add validation information
        mrpo_data["validation_results"] = {
            "validation_performed": True,
            "validation_result": "Passed" if visited_page_ids and max(visited_page_ids) == 3 else "Incomplete"
        }
        
        return mrpo_data

    def get_data(self):
        """Standard method for metadata collection"""
        return self.get_mrpo_data()
        
    def get_metadata(self):
        """Standard method for metadata collection that matches the expected format"""
        return self.get_mrpo_data()
        
    def get_metadata_directory(self):
        """Return the metadata directory"""
        return self.metadata_directory
        
    def collect_page0_metadata(self):
        """Collect metadata from Page 0 (Initial Selection)"""
        page0 = self.page(0)
        if not page0 or not hasattr(page0, 'ui'):
            return
            
        ui = page0.ui

        # Collect radio button selections for purpose
        if ui.radioButton_1.isChecked():
            self.metadata_directory["Purpose"] = "Sample Side"
        elif ui.radioButton_2.isChecked():
            self.metadata_directory["Purpose"] = "Guard Side"

        # Collect combo box selection
        self.metadata_directory["Differential Unit"] = ui.comboBox.currentText()
        
        # Collect direction selection
        if ui.radioButton_5.isChecked():
            self.metadata_directory["PO Mode"] = "UP/DOWN"
        elif ui.radioButton_6.isChecked():
            self.metadata_directory["PO Mode"] = "IN/OUT"

    def collect_page1_ud_metadata(self):
        """Collect metadata from Page 1 (UP/DOWN Configuration)"""
        page = self.page(1)
        if not page or not hasattr(page, 'ui'):
            return
            
        ui = page.ui
        
        # Collect checkbox data based on actual text of checkboxes
        if ui.checkBox_1.isChecked():
            self.metadata_directory["MRPO set to run in UP/DOWN"] = "Done"
            
        if ui.checkBox_2.isChecked():
            self.metadata_directory["Drain Plug is installed"] = "Done"
            
        if ui.checkBox_3.isChecked():
            self.metadata_directory["Manual 3-way flowline valve is set for Up/Down"] = "Done"
            
    def collect_page2_io_metadata(self):
        """Collect metadata from Page 2 (IN/OUT Configuration)"""
        page = self.page(2)
        if not page or not hasattr(page, 'ui'):
            return
            
        ui = page.ui
        
        # Collect checkbox data
        if ui.checkBox_1.isChecked():
            self.metadata_directory["MRPO set to run in IN/OUT"] = "Done"
            
        if ui.checkBox_2.isChecked():
            self.metadata_directory["Drain Plug Removed"] = "Done"
            
        if ui.checkBox_3.isChecked():
            self.metadata_directory["Manual 3-way flowline valve is set for In/Out"] = "Done"
            
        # Collect radio button selections
        if ui.radioButton_1.isChecked():
            self.metadata_directory["Exit Screen Filter Available"] = "Yes"
        elif ui.radioButton_2.isChecked():
            self.metadata_directory["Exit Screen Filter Available"] = "No"
            
        if ui.checkBox_4.isChecked() and ui.checkBox_4.isEnabled():
            self.metadata_directory["Exit Screen Filter Requirement Raised"] = "Done"
            
    def collect_page3_metadata(self):
        """Collect metadata from Page 3 (Final Checks)"""
        page = self.page(3)
        if not page or not hasattr(page, 'ui'):
            return
            
        ui = page.ui
        
        # Collect checkbox data
        if ui.checkBox_1.isChecked():
            self.metadata_directory["Oil Level"] = "Full, piston in top position against retaining ring"
            
        if ui.checkBox_2.isChecked():
            self.metadata_directory["Compensator Pistons are Clean"] = "Done"
            
        if ui.checkBox_3.isChecked():
            self.metadata_directory["Compensator Section Flushed with DC-111"] = "Done"
            
    def on_wizard_finished(self):
        """Called when the wizard is finished to ensure all metadata is collected"""
        # Make sure to collect all metadata before finishing
        self.get_mrpo_data()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    wizard = Prepare_MRPO_c(None)
    wizard.show()

    sys.exit(app.exec())

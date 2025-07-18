from PySide6.QtWidgets import QApplication, QWizard, QWizardPage
from .Prepare_MRPC_1 import Ui_Form as Ui_MRPC1
from .Prepare_MRPC_2 import Ui_Form as Ui_MRPC2
from .Prepare_MRPC_3 import Ui_Form as Ui_MRPC3
from .Prepare_MRPC_4 import Ui_Form as Ui_MRPC4
from .Prepare_MRPC_5 import Ui_Form as Ui_MRPC5
from .Prepare_MRPC_6 import Ui_Form as Ui_MRPC6
from .Prepare_MRPC_7 import Ui_Form as Ui_MRPC7
from .Prepare_MRPC_8 import Ui_Form as Ui_MRPC8
from .Prepare_MRPC_9 import Ui_Form as Ui_MRPC9
from .Prepare_MRPC_10 import Ui_Form as Ui_MRPC10
from .Prepare_MRPC_11 import Ui_Form as Ui_MRPC11

class MRPCStep1Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC1()
        self.ui.setupUi(self)
        self.setTitle("MIFA/MRBA Check")
        
        # Connect validation triggers
        self.ui.radioButton_1.toggled.connect(self.checkValidation)
        self.ui.radioButton_2.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        return self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()

    def nextId(self):
        if self.ui.radioButton_2.isChecked():  # Yes - MIFA/MRBA/Tools below
            return 2  # Go to MRPC_2
        else:  # radioButton_1.isChecked() - No
            return 7  # Go to MRPC_7

class MRPCStep2Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC2()
        self.ui.setupUi(self)
        self.setTitle("MREL/Legacy Check")
        
        self.ui.radioButton_1.toggled.connect(self.checkValidation)
        self.ui.radioButton_2.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        return self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()

    def nextId(self):
        if self.ui.radioButton_1.isChecked():  # No
            return 4  # Go to MRPC_4
        else:  # radioButton_2.isChecked() - Yes
            return 3  # Go to MRPC_3 (END)


class MRPCStep3Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC3()
        self.ui.setupUi(self)
        self.setTitle("A10 Switch Configuration")

        self.ui.checkBox_1.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        return self.ui.checkBox_1.isChecked()  # Terminal page

    def nextId(self):
        return -1  # End of wizard

class MRPCStep4Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC4()
        self.ui.setupUi(self)
        self.setTitle("Continuity Check")
        
        # Connect checkboxes from all 3 groupboxes to validation
        # GroupBox 1 checkboxes
        if hasattr(self.ui, 'radioButton_1'):
            self.ui.radioButton_1.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'radioButton_2'):
            self.ui.radioButton_2.toggled.connect(self.checkValidation)

        # GroupBox 2 checkboxes
        if hasattr(self.ui, 'radioButton_3'):
            self.ui.radioButton_3.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'radioButton_4'):
            self.ui.radioButton_4.toggled.connect(self.checkValidation)
        
        # GroupBox 3 checkboxes
        if hasattr(self.ui, 'radioButton_5'):
            self.ui.radioButton_5.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'radioButton_6'):
            self.ui.radioButton_6.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        # Check if each of the 3 groupboxes has at least one checkbox checked

        # GroupBox 1: Check if radioButton_1 OR radioButton_2 is checked
        groupbox1_complete = False
        if self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked():
            groupbox1_complete = True
        else:
            return False

        # GroupBox 2: Check if radioButton_3 OR radioButton_4 is checked
        groupbox2_complete = False
        if self.ui.radioButton_3.isChecked() or self.ui.radioButton_4.isChecked():
            groupbox2_complete = True
        else:
            return False

        # GroupBox 3: Check if radioButton_5 OR radioButton_6 is checked
        groupbox3_complete = False
        if self.ui.radioButton_5.isChecked() or self.ui.radioButton_6.isChecked():
            groupbox3_complete = True
        else:
            return False
        
        # All 3 groupboxes must have at least one checkbox checked
        return groupbox1_complete and groupbox2_complete and groupbox3_complete

    def nextId(self):
        if self.ui.radioButton_1.isChecked() and self.ui.radioButton_3.isChecked() and self.ui.radioButton_5.isChecked():
            return 5  # Go to MRPC_5 (END)
        else:
            return 6  # Go to MRPC_6


class MRPCStep5Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC5()
        self.ui.setupUi(self)
        self.setTitle("Legacy MRPC in TW-STD")
        
    def isComplete(self):
        return True  # Terminal page
        
    def nextId(self):
        return -1  # End of wizard

class MRPCStep6Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC6()
        self.ui.setupUi(self)
        self.setTitle("Set to TW-STD Configuration")
        
        # Connect checkboxes to validation
        if hasattr(self.ui, 'checkBox_1'):
            self.ui.checkBox_1.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'checkBox_2'):
            self.ui.checkBox_2.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        return False  # Never complete - user should use back button
        
    def nextId(self):
        return -1  # Don't auto-advance, use back button instead

class MRPCStep7Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC7()
        self.ui.setupUi(self)
        self.setTitle("MREL/Legacy Check")
        
        self.ui.radioButton_1.toggled.connect(self.checkValidation)
        self.ui.radioButton_2.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        return self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()

    def nextId(self):
        if self.ui.radioButton_1.isChecked():  
            return 9  # Go to MRPC_9
        else:  
            return 8  # Go to MRPC_8 (END)


class MRPCStep8Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC8()
        self.ui.setupUi(self)
        self.setTitle("A10 Switch Configuration")

        self.ui.checkBox_1.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        return self.ui.checkBox_1.isChecked()  # Terminal page
        
    def nextId(self):
        return -1  # End of wizard

class MRPCStep9Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC9()
        self.ui.setupUi(self)
        self.setTitle("Resistivity Check")
        
        # Connect checkboxes from all 3 groupboxes to validation
        # GroupBox 1 checkboxes
        if hasattr(self.ui, 'radioButton_1'):
            self.ui.radioButton_1.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'radioButton_2'):
            self.ui.radioButton_2.toggled.connect(self.checkValidation)

        # GroupBox 2 checkboxes
        if hasattr(self.ui, 'radioButton_3'):
            self.ui.radioButton_3.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'radioButton_4'):
            self.ui.radioButton_4.toggled.connect(self.checkValidation)
        
        # GroupBox 3 checkboxes
        if hasattr(self.ui, 'radioButton_5'):
            self.ui.radioButton_5.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'radioButton_6'):
            self.ui.radioButton_6.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        # Check if each of the 3 groupboxes has at least one checkbox checked

        # GroupBox 1: Check if radioButton_1 OR radioButton_2 is checked
        groupbox1_complete = False
        if self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked():
            groupbox1_complete = True
        else:
            return False

        # GroupBox 2: Check if radioButton_3 OR radioButton_4 is checked
        groupbox2_complete = False
        if self.ui.radioButton_3.isChecked() or self.ui.radioButton_4.isChecked():
            groupbox2_complete = True
        else:
            return False

        # GroupBox 3: Check if radioButton_5 OR radioButton_6 is checked
        groupbox3_complete = False
        if self.ui.radioButton_5.isChecked() or self.ui.radioButton_6.isChecked():
            groupbox3_complete = True
        else:
            return False
        
        # All 3 groupboxes must have at least one checkbox checked
        return groupbox1_complete and groupbox2_complete and groupbox3_complete

    def nextId(self):
        if self.ui.radioButton_1.isChecked() and self.ui.radioButton_3.isChecked() and self.ui.radioButton_5.isChecked():
            return 10  # Go to MRPC_10 (END)
        else:
            return 11  # Go to MRPC_11


class MRPCStep10Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC10()
        self.ui.setupUi(self)
        self.setTitle("Legacy MRPC in No TW Mode")
        
    def isComplete(self):
        return True  # Terminal page
        
    def nextId(self):
        return -1  # End of wizard

class MRPCStep11Page(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MRPC11()
        self.ui.setupUi(self)
        self.setTitle("Set to TW-STD Configuration")
        
        # Connect checkboxes similar to MRPCStep6Page
        if hasattr(self.ui, 'checkBox_1'):
            self.ui.checkBox_1.toggled.connect(self.checkValidation)
        if hasattr(self.ui, 'checkBox_2'):
            self.ui.checkBox_2.toggled.connect(self.checkValidation)

    def checkValidation(self):
        self.completeChanged.emit()
        
    def isComplete(self):
        return False  # Never complete - user should use back button
    
    def nextId(self):
        return -1  # Don't auto-advance, use back button instead

class Prepare_MRPC_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Prepare MRPC Wizard")
        
        # Initialize metadata directory
        self.metadata_directory = {}

        # Add all pages with explicit IDs matching the dialog numbers
        self.setPage(1, MRPCStep1Page())   # MRPC_1
        self.setPage(2, MRPCStep2Page())   # MRPC_2
        self.setPage(3, MRPCStep3Page())   # MRPC_3 (END)
        self.setPage(4, MRPCStep4Page())   # MRPC_4
        self.setPage(5, MRPCStep5Page())   # MRPC_5 (END)
        self.setPage(6, MRPCStep6Page())   # MRPC_6 (LOOP)
        self.setPage(7, MRPCStep7Page())   # MRPC_7
        self.setPage(8, MRPCStep8Page())   # MRPC_8 (END)
        self.setPage(9, MRPCStep9Page())   # MRPC_9
        self.setPage(10, MRPCStep10Page()) # MRPC_10 (END)
        self.setPage(11, MRPCStep11Page()) # MRPC_11 (LOOP)

        # Set wizard options for proper navigation
        self.setWizardStyle(QWizard.ModernStyle)
        self.setOption(QWizard.HaveFinishButtonOnEarlyPages, False)
        self.setOption(QWizard.HaveNextButtonOnLastPage, False)
        
        # Start with MRPC_1
        self.setStartId(1)
        
        # Connect done signal to ensure metadata is collected
        self.finished.connect(self.on_wizard_finished)

    def get_mrpc_data(self):
        """Collect data from all visited MRPC pages"""
        mrpc_data = {}
        self.metadata_directory = {}
        
        # Get the list of visited page IDs
        visited_page_ids = self.visitedIds() if hasattr(self, 'visitedIds') else []
        
        # Collect page titles from visited pages
        self.metadata_directory["Visited Pages"] = []
        
        # Iterate through all possible page IDs
        for page_id in range(1, 12):  # MRPC has pages 1-11
            if page_id in visited_page_ids and self.page(page_id):
                page_title = self.page(page_id).title()
                self.metadata_directory["Visited Pages"].append(f"Page {page_id}: {page_title}")
        
        # Add basic choice data from first page (always visited)
        if 1 in visited_page_ids and self.page(1):
            page1 = self.page(1)
            if page1.ui.radioButton_1.isChecked():
                self.metadata_directory["MIFA/MRBA/Tools below MDT required"] = "No"
            elif page1.ui.radioButton_2.isChecked():
                self.metadata_directory["MIFA/MRBA/Tools below MDT required"] = "Yes"
        
        # Return the data in the expected format
        mrpc_data["User Inputs"] = self.metadata_directory.copy()
        
        return mrpc_data

    def get_data(self):
        """Standard method for metadata collection"""
        return self.get_mrpc_data()
        
    def get_metadata(self):
        """Standard method for metadata collection that matches the expected format"""
        return self.get_mrpc_data()
        
    def get_metadata_directory(self):
        """Return the metadata directory"""
        return self.metadata_directory
        
    def on_wizard_finished(self):
        """Called when the wizard is finished to ensure all metadata is collected"""
        # Make sure to collect all metadata before finishing
        self.get_mrpc_data()

    def accept(self):
        """Override accept to handle the completion of the wizard"""
        # Collect metadata when wizard is completed
        self.on_wizard_finished()
        super().accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    wizard = Prepare_MRPC_c(None)
    wizard.show()

    sys.exit(app.exec())

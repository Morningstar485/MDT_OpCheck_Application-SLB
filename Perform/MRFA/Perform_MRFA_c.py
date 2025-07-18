from PySide6.QtWidgets import QWizard, QWizardPage
from .Perform_MRFA_1 import Ui_Dialog


class MRFAPerformPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Hide the original finish button
        self.ui.pushButton.hide()
        
        # Connect all radio buttons to validation check
        radio_buttons = [
            'radioButton_1', 'radioButton_2', 'radioButton_3', 'radioButton_4',
            'radioButton_5', 'radioButton_6', 'radioButton_7', 'radioButton_8',
            'radioButton_9', 'radioButton_10', 'radioButton_11', 'radioButton_12',
            'radioButton_13', 'radioButton_14', 'radioButton_15', 'radioButton_16'
        ]
        
        for radio_button_name in radio_buttons:
            if hasattr(self.ui, radio_button_name):
                radio_button = getattr(self.ui, radio_button_name)
                radio_button.toggled.connect(self.checkValidation)
                
    def checkValidation(self):
        """Check if validation is complete and emit completeChanged signal"""
        self.completeChanged.emit()
        
    def isComplete(self):
        """Validate the page completion based on the original UI logic"""
        # Check groupBox_1 (FASW Data Channels)
        if not (self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()):
            return False
            
        # If "No" selected for FASW, workflow cannot complete (Contact IE)
        if self.ui.radioButton_2.isChecked():
            return False
            
        # If "Yes" selected for FASW, check groupBox_2 (FAAS Data Channels)
        if self.ui.radioButton_1.isChecked():
            if not (self.ui.radioButton_3.isChecked() or self.ui.radioButton_4.isChecked()):
                return False
                
            # If "No" selected for FAAS, workflow cannot complete (Contact IE)
            if self.ui.radioButton_4.isChecked():
                return False
                
            # If "Yes" selected for FAAS, check groupBox_3 (RSPC Data Channels)
            if self.ui.radioButton_3.isChecked():
                if not (self.ui.radioButton_5.isChecked() or self.ui.radioButton_6.isChecked()):
                    return False
                    
                # If "No" selected for RSPC, workflow cannot complete (Contact IE)
                if self.ui.radioButton_6.isChecked():
                    return False
                    
                # If "Yes" selected for RSPC, check groupBox_4 (ACOM Pass)
                if self.ui.radioButton_5.isChecked():
                    if not (self.ui.radioButton_7.isChecked() or self.ui.radioButton_8.isChecked()):
                        return False
                        
                    # Branch based on ACOM Pass result
                    if self.ui.radioButton_7.isChecked():
                        # ACOM Pass = Yes, check groupBox_6 (FAMO Data channel changing)
                        if not (self.ui.radioButton_11.isChecked() or self.ui.radioButton_12.isChecked()):
                            return False
                            
                        # Handle FAMO changing paths
                        if self.ui.radioButton_11.isChecked():
                            # FAMO changing = Yes, go to groupBox_8 (RSPC voltage check)
                            if not (self.ui.radioButton_15.isChecked() or self.ui.radioButton_16.isChecked()):
                                return False
                            # Can only complete if RSPC voltage is "Yes"
                            return self.ui.radioButton_15.isChecked()
                            
                        elif self.ui.radioButton_12.isChecked():
                            # FAMO changing = No, check groupBox_7 (changing after redo)
                            if not (self.ui.radioButton_13.isChecked() or self.ui.radioButton_14.isChecked()):
                                return False
                                
                            # If still not changing after redo, cannot complete (Contact IE)
                            if self.ui.radioButton_14.isChecked():
                                return False
                                
                            # If changing after redo, check groupBox_8
                            if self.ui.radioButton_13.isChecked():
                                if not (self.ui.radioButton_15.isChecked() or self.ui.radioButton_16.isChecked()):
                                    return False
                                # Can only complete if RSPC voltage is "Yes"
                                return self.ui.radioButton_15.isChecked()
                                
                    elif self.ui.radioButton_8.isChecked():
                        # ACOM Pass = No, check groupBox_5 (Redo ACOM)
                        if not (self.ui.radioButton_9.isChecked() or self.ui.radioButton_10.isChecked()):
                            return False
                            
                        # If not redoing ACOM, cannot complete (Contact IE)
                        if self.ui.radioButton_10.isChecked():
                            return False
                            
                        # If redoing ACOM, check groupBox_6 (FAMO Data channel changing)
                        if self.ui.radioButton_9.isChecked():
                            if not (self.ui.radioButton_11.isChecked() or self.ui.radioButton_12.isChecked()):
                                return False
                                
                            # Handle FAMO changing paths (same logic as above)
                            if self.ui.radioButton_11.isChecked():
                                if not (self.ui.radioButton_15.isChecked() or self.ui.radioButton_16.isChecked()):
                                    return False
                                return self.ui.radioButton_15.isChecked()
                                
                            elif self.ui.radioButton_12.isChecked():
                                if not (self.ui.radioButton_13.isChecked() or self.ui.radioButton_14.isChecked()):
                                    return False
                                if self.ui.radioButton_14.isChecked():
                                    return False
                                if self.ui.radioButton_13.isChecked():
                                    if not (self.ui.radioButton_15.isChecked() or self.ui.radioButton_16.isChecked()):
                                        return False
                                    return self.ui.radioButton_15.isChecked()
        
        return False


class Perform_MRFA_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRFA Performance Test Wizard")
        self.resize(1000, 560)
        
        # Create and add the page
        self.mrfa_page = MRFAPerformPage()
        self.addPage(self.mrfa_page)
        
    def get_metadata(self):
        """Collect metadata from the wizard"""
        # Create structured metadata with expected sections
        metadata = {
            "User Inputs": {},
            "Tool Name": "MRFA"
            }
        
        # FASW Data Channels status
        if self.mrfa_page.ui.radioButton_1.isChecked():
            metadata["User Inputs"]["FASW Data Channels"] = "Success - All FASW Data Channels are Green"
        elif self.mrfa_page.ui.radioButton_2.isChecked():
            metadata["User Inputs"]["FASW Data Channels"] = "Failed - FASW Data Channels not all Green (Contact IE required)"
            
        # FAAS Data Channels status
        if self.mrfa_page.ui.radioButton_3.isChecked():
            metadata["User Inputs"]["FAAS Data Channels"] = "Success - All FAAS Data Channels are Green"
        elif self.mrfa_page.ui.radioButton_4.isChecked():
            metadata["User Inputs"]["FAAS Data Channels"] = "Failed - FAAS Data Channels not all Green (Contact IE required)"
            
        # RSPC Data Channels status
        if self.mrfa_page.ui.radioButton_5.isChecked():
            metadata["User Inputs"]["RSPC Data Channels"] = "Success - All RSPC Data Channels are Green"
        elif self.mrfa_page.ui.radioButton_6.isChecked():
            metadata["User Inputs"]["RSPC Data Channels"] = "Failed - RSPC Data Channels not all Green (Contact IE required)"
            
        # ACOM Pass status
        if self.mrfa_page.ui.radioButton_7.isChecked():
            metadata["User Inputs"]["ACOM Pass"] = "Success - ACOM Pass completed successfully"
        elif self.mrfa_page.ui.radioButton_8.isChecked():
            metadata["User Inputs"]["ACOM Pass"] = "Failed - ACOM Pass failed, redo required"

        # Redo ACOM Pass (if applicable)
        if self.mrfa_page.ui.radioButton_9.isChecked():
            metadata["User Inputs"]["ACOM Pass Redo"] = "Confirmed - ACOM Pass redo performed"
        elif self.mrfa_page.ui.radioButton_10.isChecked():
            metadata["User Inputs"]["ACOM Pass Redo"] = "Declined - ACOM Pass redo not performed (Contact IE required)"
            
        # FAMO Data channel behavior during ACOM
        if self.mrfa_page.ui.radioButton_11.isChecked():
            metadata["User Inputs"]["FAMO Data Channel Behavior"] = "Observed - FAMO Data channel value changing during ACOM"
        elif self.mrfa_page.ui.radioButton_12.isChecked():
            metadata["User Inputs"]["FAMO Data Channel Behavior"] = "Stable - FAMO Data channel value not changing during ACOM"

        # FAMO behavior after redo (if applicable)
        if self.mrfa_page.ui.radioButton_13.isChecked():
            metadata["User Inputs"]["FAMO After Redo"] = "Confirmed - FAMO Data channel changing after redo"
        elif self.mrfa_page.ui.radioButton_14.isChecked():
            metadata["User Inputs"]["FAMO After Redo"] = "Issue - FAMO Data channel still not changing after redo (Contact IE required)"
            
        # RSPC voltage verification
        if self.mrfa_page.ui.radioButton_15.isChecked():
            metadata["User Inputs"]["RSPC Voltage Check"] = "Success - All RSPC channels between 1.35 V and 3.2 V"
        elif self.mrfa_page.ui.radioButton_16.isChecked():
            metadata["User Inputs"]["RSPC Voltage Check"] = "Failed - RSPC channels not within 1.35 V to 3.2 V range (Contact IE required)"

        return metadata

    def get_data(self):
        """Legacy method for backward compatibility"""
        return self.get_metadata()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    wizard = Perform_MRFA_c()
    wizard.show()
    sys.exit(app.exec())
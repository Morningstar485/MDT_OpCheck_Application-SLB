from PySide6.QtWidgets import QWizard, QWizardPage
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from .Prepare_MRPQ_1 import Ui_Dialog


class MRPQPage(QWizardPage):
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
        url = QUrl("https://intouchsupport.com/index.cfm?event=content.preview&contentId=7111097&FromRefPage=Y")
        QDesktopServices.openUrl(url)
    
    def isComplete(self):
        """Validate the page completion based on the original UI logic"""
        # Check if groupBox_1 (gauge calibration) has selection
        if not (self.ui.radioButton_1.isChecked() or self.ui.radioButton_2.isChecked()):
            return False
            
        # If "Yes" selected for gauge calibration, check first 6 checkboxes
        if self.ui.radioButton_1.isChecked():
            if not all([
                self.ui.checkBox_1.isChecked(),
                self.ui.checkBox_2.isChecked(), 
                self.ui.checkBox_3.isChecked(),
                self.ui.checkBox_4.isChecked(),
                self.ui.checkBox_5.isChecked(),
                self.ui.checkBox_6.isChecked()
            ]):
                return False
        
        # If "No" selected, still need to complete the progressive flow
        elif self.ui.radioButton_2.isChecked():
            if not all([
                self.ui.checkBox_1.isChecked(),
                self.ui.checkBox_2.isChecked(), 
                self.ui.checkBox_3.isChecked(),
                self.ui.checkBox_4.isChecked(),
                self.ui.checkBox_5.isChecked(),
                self.ui.checkBox_6.isChecked()
            ]):
                return False
        
        # Check groupBox_2 (sensor port 2) has selection
        if not (self.ui.radioButton_3.isChecked() or 
                self.ui.radioButton_4.isChecked() or 
                self.ui.radioButton_5.isChecked()):
            return False
            
        # Check combo box has valid selection (not default)
        if self.ui.comboBox.currentText() == "Select Probe":
            return False
            
        # Check installation checkboxes
        if not (self.ui.checkBox_8.isChecked() and self.ui.checkBox_7.isChecked()):
            return False
            
        # Check groupBox_3 (anchoring piston) has selection  
        if not (self.ui.radioButton_6.isChecked() or
                self.ui.radioButton_7.isChecked() or
                self.ui.radioButton_8.isChecked() or
                self.ui.radioButton_9.isChecked()):
            return False
            
        # Check final checkbox 9
        if not self.ui.checkBox_9.isChecked():
            return False
            
        # Check groupBox_4 (probe jig availability)
        if not (self.ui.radioButton_10.isChecked() or self.ui.radioButton_11.isChecked()):
            return False
            
        # If "No" selected for probe jig, check final checkbox
        if self.ui.radioButton_11.isChecked():
            if not self.ui.checkBox_10.isChecked():
                return False
        
        return True


class Prepare_MRPQ_c(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle("MRPQ Preparation Wizard")
        self.resize(1000, 750)
        
        # Create and add the page
        self.mrpq_page = MRPQPage()
        self.addPage(self.mrpq_page)
        
    def get_metadata(self):
        """Collect metadata from the wizard"""
        metadata = {}
        
        # Gauge calibration information
        if self.mrpq_page.ui.radioButton_1.isChecked():
            metadata["gauge_calibration_available"] = "Yes - Valid SG/CQG/QZD gauge calibration is available"
        elif self.mrpq_page.ui.radioButton_2.isChecked():
            metadata["gauge_calibration_available"] = "No - Need to download from Maximo"
            
        # Sequential preparation steps
        preparation_steps = []
        if self.mrpq_page.ui.checkBox_1.isChecked():
            preparation_steps.append("Checked flowline and hydraulic stabbers pressure")
        if self.mrpq_page.ui.checkBox_2.isChecked():
            preparation_steps.append("Stabber/receiver set properly with blank plug")
        if self.mrpq_page.ui.checkBox_3.isChecked():
            preparation_steps.append("CQG is flushed")
        if self.mrpq_page.ui.checkBox_4.isChecked():
            preparation_steps.append("Plug stamped 'P' installed in Port plug")
        if self.mrpq_page.ui.checkBox_5.isChecked():
            preparation_steps.append("Snubber stamped 'S' installed in Snubber port")
        if self.mrpq_page.ui.checkBox_6.isChecked():
            preparation_steps.append("Sensor ports matching confirmed")
            
        if preparation_steps:
            metadata["preparation_completed"] = preparation_steps
            
        # Sensor port 2 configuration
        if self.mrpq_page.ui.radioButton_3.isChecked():
            metadata["Sensor Port 2 Cell"] = "Dummy cell installed in Sensor Port 2"
        elif self.mrpq_page.ui.radioButton_4.isChecked():
            metadata["Sensor Port 2 Cell"] = "DV Rod installed in Sensor Port 2"
        elif self.mrpq_page.ui.radioButton_5.isChecked():
            metadata["Sensor Port 2 Cell"] = "H2S Coupon installed in Sensor Port 2"

        # Probe selection
        probe_selection = self.mrpq_page.ui.comboBox.currentText()
        if probe_selection != "Select Probe":
            metadata["Probe Type"] = f"Selected probe: {probe_selection}"

        # Installation steps
        installation_steps = []
        if self.mrpq_page.ui.checkBox_8.isChecked():
            installation_steps.append("Guard flowline socket and joint removed")
        if self.mrpq_page.ui.checkBox_7.isChecked():
            installation_steps.append("100238610 Plug for MRPQ installed")
            
        if installation_steps:
            metadata["Installation Completed"] = installation_steps

        # Anchoring piston configuration
        if self.mrpq_page.ui.radioButton_6.isChecked():
            metadata["Anchoring Piston"] = "17.5 In - MRSL piston "
        elif self.mrpq_page.ui.radioButton_7.isChecked():
            metadata["Anchoring Piston"] = "12.25 In - MRLH piston "
        elif self.mrpq_page.ui.radioButton_8.isChecked():
            metadata["Anchoring Piston"] = "8.5 In - STD Piston (SRTP) "
        elif self.mrpq_page.ui.radioButton_9.isChecked():
            metadata["Anchoring Piston"] = "6 In - STD Piston (SRTP) with inner piston and B030664 Retaining ring "

        # Final validations
        if self.mrpq_page.ui.checkBox_9.isChecked():
            metadata["Valve Validation"] = "ISO valve and Bypass valve checked - Screw out till truarc ring from Hydraulic side"
            
        # Probe jig availability
        if self.mrpq_page.ui.radioButton_10.isChecked():
            metadata["Probe Jig Available"] = "Yes - MRPQ probe jig available in RB"
        elif self.mrpq_page.ui.radioButton_11.isChecked():
            metadata["Probe Jig Available"] = "No - MRPQ probe jig not available in RB"
            if self.mrpq_page.ui.checkBox_10.isChecked():
                metadata["Pressure Check Limitation"] = "Acknowledged - Cannot check SG Pressure without jig"

        return metadata

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    wizard = Prepare_MRPQ_c()
    wizard.show()
    sys.exit(app.exec())
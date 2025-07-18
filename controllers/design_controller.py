from PySide6.QtWidgets import QWidget, QDialog
from controllers.base_controller import BaseController
from Design.Design_1 import Ui_Dialog as DesignStep1
from Design.Design_2 import Ui_Dialog as DesignStep2
from Design.Design_3 import Ui_Dialog as DesignStep3

class DesignController(BaseController):
    def __init__(self, on_complete_callback, metadata_manager=None):
        self.metadata_manager = metadata_manager
        
        # Create actual QDialog instances and apply the UI to them
        dialog1 = QDialog()
        ui1 = DesignStep1()
        ui1.setupUi(dialog1)
        
        dialog2 = QDialog()
        ui2 = DesignStep2()
        ui2.setupUi(dialog2)
        
        dialog3 = QDialog()
        ui3 = DesignStep3()
        ui3.setupUi(dialog3)
        
        # Store UI references for navigation setup
        dialog1.ui = ui1
        dialog2.ui = ui2
        dialog3.ui = ui3
        
        dialogs = [dialog1, dialog2, dialog3]
        super().__init__(dialogs, on_complete_callback)
        
        # Connect navigation buttons after initialization
        self.setup_navigation()
    
    def setup_navigation(self):
        """Connect navigation buttons to controller methods"""
        # Design 1: Connect pushButton_1 to next
        if hasattr(self.dialog_list[0].ui, 'pushButton_1'):
            self.dialog_list[0].ui.pushButton_1.clicked.connect(self.show_next)
        
        # Design 2: Connect navigation buttons and add back functionality
        if hasattr(self.dialog_list[1].ui, 'pushButton_2'):  # Next button
            self.dialog_list[1].ui.pushButton_2.clicked.connect(self.show_next)
        
        # Design 3: Connect validation and proceed
        if hasattr(self.dialog_list[2].ui, 'pushButton_3'):  # Back button
            self.dialog_list[2].ui.pushButton_3.clicked.connect(self.show_back)
        if hasattr(self.dialog_list[2].ui, 'pushButton'):  # Forward button
            # Disconnect existing connection and connect to our navigation
            try:
                self.dialog_list[2].ui.pushButton.clicked.disconnect()
            except TypeError:
                # No connections to disconnect
                pass
            self.dialog_list[2].ui.pushButton.clicked.connect(self.handle_design3_proceed)
    
    def keyPressEvent(self, event):
        """Handle keyboard navigation"""
        from PySide6.QtCore import Qt
        if event.key() == Qt.Key_Escape and self.current_index > 0:
            self.show_back()
        else:
            super().keyPressEvent(event)
    
    def handle_design3_proceed(self):
        """Handle Design 3 proceed with validation"""
        # Call the original validation method
        if self.dialog_list[2].ui.validate_and_proceed():
            # Collect design data and generate report
            if self.metadata_manager:
                print("Collecting design data...")
                design_data = self.collect_design_data()
                print(f"Design data collected: {design_data}")
                
                print("Generating design report...")
                report_path = self.generate_design_report()
                if report_path:
                    print(f"Design report generated: {report_path}")
                else:
                    print("Failed to generate design report")
            
            # If validation passes, close all dialogs and proceed to next phase
            self.close_all_dialogs()
            self.show_next()
    
    def close_all_dialogs(self):
        """Close all dialog windows properly"""
        for dialog in self.dialog_list:
            if dialog.isVisible():
                dialog.close()
    
    def close(self):
        """Override close to ensure all dialogs are closed"""
        self.close_all_dialogs()
        super().close()
    
    def collect_design_data(self):
        """Collect all design data from the three design dialogs"""
        if not self.metadata_manager:
            return
            
        design_data = {}
        
        # Design 1 - Well Information
        ui1 = self.dialog_list[0].ui
        if hasattr(ui1, 'lineEdit_1') and ui1.lineEdit_1.text():
            design_data['Well Name'] = ui1.lineEdit_1.text()
        else:
            design_data['Well Name'] = 'Not Provided'
            
        if hasattr(ui1, 'lineEdit_2') and ui1.lineEdit_2.text():
            design_data['Rig Name'] = ui1.lineEdit_2.text()
        else:
            design_data['Rig Name'] = 'Not Provided'

        if hasattr(ui1, 'lineEdit_3') and ui1.lineEdit_3.text():
            design_data['FDP Number'] = ui1.lineEdit_3.text()
        else:
            design_data['FDP Number'] = 'Not Provided'

        # Design 2 - Crew Information
        ui2 = self.dialog_list[1].ui
        crew_data = {}
        
        # Get the number of crew members
        if hasattr(ui2, 'lineEdit_3') and ui2.lineEdit_3.text():
            try:
                crew_data['Number of Crew Members'] = int(ui2.lineEdit_3.text())
            except ValueError:
                crew_data['Number of Crew Members'] = 1

        # Get primary crew designation
        if hasattr(ui2, 'comboBox') and ui2.comboBox.currentText() != "Select":
            crew_data['Primary Designation'] = ui2.comboBox.currentText()
        else:
            crew_data['Primary Designation'] = "Not Selected"
            
        # Add any additional crew designations from dynamic combo boxes
        # (This would require more complex logic to collect from dynamically created widgets)
        # For now just mark that Design 2 was completed
        design_data['Crew Information'] = crew_data

        # Design 3 - Competency and exemption data
        # Following the visual layout: Left Column (frame_7), Middle Column (frame_16), Right Column (frame_17)
        # Going from top to bottom in each column, then left to right
        ui3 = self.dialog_list[2].ui
        
        # ===== LEFT COLUMN (frame_7) - Top to Bottom =====
        
        # GB1 - PCP Competency Fulfilled
        if hasattr(ui3, 'GB1') and ui3.GB1.isEnabled():
            if hasattr(ui3, 'R1') and ui3.R1.isChecked():
                design_data['PCP Competency Fulfilled'] = 'Yes'
            elif hasattr(ui3, 'R2') and ui3.R2.isChecked():
                design_data['PCP Competency Fulfilled'] = 'No'
            else:
                design_data['PCP Competency Fulfilled'] = 'Not Selected'

        # GB2 - Exemption Raised (if enabled)
        if hasattr(ui3, 'GB2') and ui3.GB2.isEnabled():
            if hasattr(ui3, 'R3') and ui3.R3.isChecked():
                design_data['Competency Exemption Raised'] = 'Yes'
            elif hasattr(ui3, 'R4') and ui3.R4.isChecked():
                design_data['Competency Exemption Raised'] = 'No'
            else:
                design_data['Competency Exemption Raised'] = 'Not Selected'

        # LineEdit_1 - Exemption Reference Number (if enabled)
        if hasattr(ui3, 'lineEdit_1') and ui3.lineEdit_1.isEnabled():
            if ui3.lineEdit_1.text():
                design_data['Exemption Number'] = ui3.lineEdit_1.text()
            else:
                design_data['Exemption Number'] = 'Not Provided'

        # GB3 - Exemption Approved (if enabled)
        if hasattr(ui3, 'GB3') and ui3.GB3.isEnabled():
            if hasattr(ui3, 'R5') and ui3.R5.isChecked():
                design_data['Exemption Approved'] = 'Yes'
            elif hasattr(ui3, 'R6') and ui3.R6.isChecked():
                design_data['Exemption Approved'] = 'No'
            else:
                design_data['Exemption Approved'] = 'Not Selected'

        if hasattr(ui3, 'CB1') and ui3.CB1.isEnabled():
            design_data['Briefing with PSD'] = 'Done' if ui3.CB1.isChecked() else 'No'

        # ComboBox_2 - Conveyance (if enabled)
        if hasattr(ui3, 'comboBox_2') and ui3.comboBox_2.isEnabled():
            if ui3.comboBox_2.currentText() != "Select":
                design_data['Conveyance'] = ui3.comboBox_2.currentText()
            else:
                design_data['Conveyance'] = 'Not Selected'

        # LineEdit_2 - Weak Point (if enabled)
        if hasattr(ui3, 'lineEdit_2') and ui3.lineEdit_2.isEnabled():
            if ui3.lineEdit_2.text():
                design_data['Weak Point'] = ui3.lineEdit_2.text()
            else:
                design_data['Weak Point'] = 'Not Provided'

        # ComboBox_1 - Hole Size (if enabled)
        if hasattr(ui3, 'comboBox_1') and ui3.comboBox_1.isEnabled():
            if ui3.comboBox_1.currentText() != "Select":
                design_data['General Service'] = ui3.comboBox_1.currentText()
            else:
                design_data['General Service'] = 'Not Selected'

        # GB4 - Conveyance Tool Planner Ready (if enabled)
        if hasattr(ui3, 'GB4') and ui3.GB4.isEnabled():
            if hasattr(ui3, 'R7') and ui3.R7.isChecked():
                design_data['Conveyance Tool Planner Ready'] = 'Yes'
            elif hasattr(ui3, 'R8') and ui3.R8.isChecked():
                design_data['Conveyance Tool Planner Ready'] = 'No'
            else:
                design_data['Conveyance Tool Planner Ready'] = 'Not Selected'

        # GB5 - MEMS Report Valid (if enabled)
        if hasattr(ui3, 'GB5') and ui3.GB5.isEnabled():
            if hasattr(ui3, 'R9') and ui3.R9.isChecked():
                design_data['MEMS Report Valid'] = 'Yes'
            elif hasattr(ui3, 'R10') and ui3.R10.isChecked():
                design_data['MEMS Report Valid'] = 'No'
            else:
                design_data['MEMS Report Valid'] = 'Not Selected'

        # GB6 - Testing Fluid Compatible (if enabled)
        if hasattr(ui3, 'GB6') and ui3.GB6.isEnabled():
            if hasattr(ui3, 'R11') and ui3.R11.isChecked():
                design_data['Report Exemption'] = 'Raised'
            elif hasattr(ui3, 'R12') and ui3.R12.isChecked():
                design_data['Report Exemption'] = 'No'
            else:
                design_data['Report Exemption'] = 'Not Selected'

        # LineEdit_3 - Exemption Reference (MEMS) (if enabled)
        if hasattr(ui3, 'lineEdit_3') and ui3.lineEdit_3.isEnabled():
            if ui3.lineEdit_3.text():
                design_data['MEMS Exemption Number'] = ui3.lineEdit_3.text()
            else:
                design_data['MEMS Exemption Number'] = 'Not Provided'

        if hasattr(ui3, 'GB7') and ui3.GB7.isEnabled():
            if hasattr(ui3, 'R13') and ui3.R13.isChecked():
                design_data['Exemption Approved'] = 'Yes'
            elif hasattr(ui3, 'R14') and ui3.R14.isChecked():
                design_data['Exemption Approved'] = 'No'
            else:
                design_data['Exemption Approved'] = 'Not Selected'

        # LineEdit_5 - Additional Field 5 (if enabled)
        if hasattr(ui3, 'lineEdit_5') and ui3.lineEdit_5.isEnabled():
            if ui3.lineEdit_5.text():
                design_data['Tool Operation %'] = ui3.lineEdit_5.text()
            else:
                design_data['Tool Operation %'] = 'Not Provided'

        if hasattr(ui3, 'dateTimeEdit') and ui3.dateTimeEdit.isEnabled():
            design_data['Expected Rig Up'] = ui3.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        

        # ===== MIDDLE COLUMN (frame_16) - Top to Bottom =====

        # LineEdit_4 - Well Temperature Expected (°F) (if enabled)
        if hasattr(ui3, 'lineEdit_4') and ui3.lineEdit_4.isEnabled():
            if ui3.lineEdit_4.text():
                design_data['Well Temperature Expected (°F)'] = ui3.lineEdit_4.text()
            else:
                design_data['Well Temperature Expected (°F)'] = 'Not Provided'

        # GB8 - Tool Inspection (if enabled)
        if hasattr(ui3, 'GB8') and ui3.GB8.isEnabled():
            if hasattr(ui3, 'R17') and ui3.R17.isChecked():
                design_data['HT Tools Available'] = 'Yes'
            elif hasattr(ui3, 'R18') and ui3.R18.isChecked():
                design_data['HT Tools Available'] = 'No'
            else:
                design_data['HT Tools Available'] = 'Not Selected'

        # ===== RIGHT COLUMN (frame_17) - Top to Bottom =====
        
        # ComboBox - Service Selection (if enabled)
        if hasattr(ui3, 'comboBox') and ui3.comboBox.isEnabled():
            if ui3.comboBox.currentText() != "Select":
                design_data['Service Selection'] = ui3.comboBox.currentText()
            else:
                design_data['Service Selection'] = 'Not Selected'
        
        # Additional GroupBoxes (if they exist in the right column)
        # GB9 - Additional GroupBox 9 (if enabled)
        if hasattr(ui3, 'GB9') and ui3.GB9.isEnabled():
            if hasattr(ui3, 'R19') and ui3.R19.isChecked():
                design_data['Is the Solid % > 15%'] = 'Yes'
            elif hasattr(ui3, 'R20') and ui3.R20.isChecked():
                design_data['Is the Solid % > 15%'] = 'No'
            else:
                design_data['Is the Solid % > 15%'] = 'Not Selected'

        # GB10 - Dynamic title based on service selection (if enabled)
        if hasattr(ui3, 'GB10') and ui3.GB10.isEnabled():
            # Get the actual title of the GroupBox dynamically
            gb10_title = ui3.GB10.title() if hasattr(ui3.GB10, 'title') else 'GB10'
            if hasattr(ui3, 'R21') and ui3.R21.isChecked():
                design_data[gb10_title] = 'Yes'
            elif hasattr(ui3, 'R22') and ui3.R22.isChecked():
                design_data[gb10_title] = 'No'
            else:
                design_data[gb10_title] = 'Not Selected'
        
        # GB11 - What is the Mud Type (if enabled)
        if hasattr(ui3, 'GB11') and ui3.GB11.isEnabled():
            if hasattr(ui3, 'R23') and ui3.R23.isChecked():
                design_data['Mud Type'] = 'Oil Based'
            elif hasattr(ui3, 'R24') and ui3.R24.isChecked():
                design_data['Mud Type'] = 'Water Based'
            else:
                design_data['Mud Type'] = 'Not Selected'

        # GB12 - Is LFA/MIFA Available (if enabled)
        if hasattr(ui3, 'GB12') and ui3.GB12.isEnabled():
            if hasattr(ui3, 'R25') and ui3.R25.isChecked():
                design_data['Is LFA/MIFA Available'] = 'Yes'
            elif hasattr(ui3, 'R26') and ui3.R26.isChecked():
                design_data['Is LFA/MIFA Available'] = 'No'
            else:
                design_data['Is LFA/MIFA Available'] = 'Not Selected'
        
        # ===== BOTTOM SECTION - Additional Elements =====
        
        # Any additional checkboxes - Only collect if enabled
        
        # Backup tools section - Only collect if enabled
        if hasattr(ui3, 'textEdit') and ui3.textEdit.isEnabled():
            if ui3.textEdit.toPlainText().strip():
                design_data['Backup Tools Info'] = ui3.textEdit.toPlainText().strip()
            else:
                design_data['Backup Tools Info'] = 'None specified'
        
        # Store in metadata manager
        self.metadata_manager.set_global_category("design_data", design_data)
        
        return design_data
    
    def generate_design_report(self):
        """Generate a design phase report"""
        if not self.metadata_manager:
            return None
            
        # Collect current design data
        design_data = self.collect_design_data()
        
        # Import report generator
        from report_generator import ReportGenerator
        report_generator = ReportGenerator()
        
        # Initialize local metadata for design report
        self.metadata_manager.init_local_data("Design", "Design")
        self.metadata_manager.set_local_data("design_choices", "all_choices", design_data)
        self.metadata_manager.add_local_note("Design phase completed successfully")
        
        # Finalize local data
        final_local_data = self.metadata_manager.finalize_local_data()
        
        # Generate report
        try:
            report_path = report_generator.generate_tool_report(
                self.metadata_manager.get_global_data(),
                final_local_data
            )
            
            # Add to processed tools
            self.metadata_manager.add_processed_tool("Design", "Design", True)
            
            # Clear local data
            self.metadata_manager.clear_local_data()
            
            return report_path
            
        except Exception as e:
            print(f"Error generating design report: {e}")
            return None

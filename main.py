from PySide6.QtWidgets import QApplication
from controllers.design_controller import DesignController
from controllers.prepare_controller import PrepareController
from Perform.Admin.Perform_Admin_c import Perform_Admin_c
from tool_selection_perform import ToolSelectionPerformDialog
from Module_Selection import ModuleSelectionDialog
from metadata_manager import MetadataManager
from report_generator import ReportGenerator
from SFT_Dialog import SFT_Dialog

class MainApplication:
    def __init__(self):
        self.selected_toolstring = None  # Store the selected toolstring
        
        # Initialize metadata management
        self.metadata_manager = MetadataManager()
        self.report_generator = ReportGenerator()
        
        self.start_design_phase()

    def start_design_phase(self):
        self.design_controller = DesignController(self.on_design_complete, self.metadata_manager)
        self.design_controller.show()

    def on_design_complete(self):
        # Close the design controller to prevent empty window
        if hasattr(self, 'design_controller') and self.design_controller:
            self.design_controller.close()
        self.start_toolstring_declaration_phase()

    def start_toolstring_declaration_phase(self):
        print("Starting toolstring declaration phase")
        self.module_selection_dialog = ModuleSelectionDialog(None, self.metadata_manager)  # No callback
        result = self.module_selection_dialog.exec()
        print(f"ModuleSelectionDialog result: {result}")
        
        if result == 1:  # QDialog.Accepted
            print("Module selection was accepted, proceeding...")
            self.on_toolstring_declaration_complete()
        else:
            print("Module selection was cancelled/rejected")
            # Handle cancellation - could exit or return to previous phase
            return

    def on_toolstring_declaration_complete(self):
        print("on_toolstring_declaration_complete called")
        # Capture the selected toolstring from the module selection dialog
        if hasattr(self.module_selection_dialog, 'selected_tool_names'):
            self.selected_toolstring = self.module_selection_dialog.selected_tool_names
            print(f"Captured toolstring: {self.selected_toolstring}")  # For debugging
            
            # Generate a design report after module selection
            try:
                # Create local metadata for the design report
                self.metadata_manager.init_local_data("Design_Summary", "Design")
                
                # Add module selection information to the report
                toolstring_data = self.metadata_manager.global_metadata.get("toolstring_declaration", {})
                if toolstring_data:
                    self.metadata_manager.local_metadata["user_inputs"] = {
                        "Selected Modules": self.selected_toolstring,
                        "Total Modules": len(self.selected_toolstring)
                    }
                    
                    # If detailed module info is available, add it too
                    if "detailed_modules" in toolstring_data:
                        detailed_modules = toolstring_data["detailed_modules"]
                        module_details = {}
                        for i, module in enumerate(detailed_modules, 1):
                            module_details[f"Module {i}"] = module
                        self.metadata_manager.local_metadata["user_inputs"]["Module Details"] = module_details
                
                # Set end time
                from datetime import datetime
                self.metadata_manager.local_metadata["tool_info"]["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Generate the design summary report
                report_path = self.report_generator.generate_tool_report(
                    self.metadata_manager.global_metadata,
                    self.metadata_manager.local_metadata
                )
                print(f"Design Summary report generated after module selection: {report_path}")
                
                # Clear local data for next phase
                self.metadata_manager.clear_local_data()
                
            except Exception as e:
                print(f"Error generating design summary report: {e}")
                import traceback
                traceback.print_exc()
        
        # Show SFT dialog before starting prepare phase
        self.show_sft_dialog()

    def show_sft_dialog(self):
        # Create and show the SFT dialog
        print("Opening SFT dialog to check manuals")
        self.sft_dialog = SFT_Dialog()
        result = self.sft_dialog.exec()
        
        # When dialog is closed, move to prepare phase
        print(f"SFT dialog closed with result: {result}")
        self.start_prepare_phase()
        
    def start_prepare_phase(self):
        # Pass the selected toolstring to the PrepareController
        # If no toolstring was captured, PrepareController will use its default
        toolstring_to_use = self.selected_toolstring if self.selected_toolstring else []
        
        print(f"Starting prepare phase with toolstring: {toolstring_to_use}")
        
        try:
            # Create the prepare controller
            self.prepare_controller = PrepareController(self.on_prepare_complete, toolstring_to_use, self.metadata_manager)
            
            # Check if we have any tools to prepare
            if not self.prepare_controller.dialog_list or len(self.prepare_controller.dialog_list) == 0:
                print("No prepare tools to run, skipping prepare phase")
                self.on_prepare_complete()
                return
                
            # Show the controller
            print(f"Showing prepare controller with {len(self.prepare_controller.dialog_list)} tools")
            self.prepare_controller.show()
        except Exception as e:
            print(f"Error initializing prepare phase: {e}")
            import traceback
            traceback.print_exc()
            # Continue with next phase
            self.on_prepare_complete()

    def on_prepare_complete(self):
        # Close the prepare controller to prevent empty window
        if hasattr(self, 'prepare_controller') and self.prepare_controller:
            self.prepare_controller.close()
        self.start_perform_common_phase()

    def start_perform_common_phase(self):
        self.perform_common_wizard = Perform_Admin_c(None, self.on_perform_common_complete)
        self.perform_common_wizard.exec()

    def on_perform_common_complete(self):
        # Collect metadata from the common perform phase
        try:
            if hasattr(self.perform_common_wizard, 'get_metadata'):
                admin_metadata = self.perform_common_wizard.get_metadata()
                
                # Update global metadata with admin perform data
                self.metadata_manager.global_metadata["admin_perform_data"] = admin_metadata
                
                # Add to processed tools list
                if not self.metadata_manager.global_metadata.get("processed_tools"):
                    self.metadata_manager.global_metadata["processed_tools"] = []
                
                admin_completion_record = {
                    
                    "phase": "Initializing OST Perform",
                    "timestamp": self.perform_common_wizard.ui.get("end_time", "N/A") if hasattr(self.perform_common_wizard, 'ui') else "N/A",
                    "success": True,
                    "metadata": admin_metadata
                }
                self.metadata_manager.global_metadata["processed_tools"].append(admin_completion_record)
                
                # Generate individual report for admin perform
                self.metadata_manager.init_local_data("Admin_Perform", "Initializing OST Perform")
                # Set the collected admin metadata
                if "test_results" in admin_metadata:
                    self.metadata_manager.local_metadata["test_results"] = admin_metadata["test_results"]
                if "user_inputs" in admin_metadata:
                    self.metadata_manager.local_metadata["user_inputs"] = admin_metadata["user_inputs"]
                if "validation_results" in admin_metadata:
                    self.metadata_manager.local_metadata["validation_results"] = admin_metadata["validation_results"]
                
                # Set end time
                from datetime import datetime
                self.metadata_manager.local_metadata["tool_info"]["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Generate admin perform report
                try:
                    report_path = self.report_generator.generate_tool_report(
                        self.metadata_manager.global_metadata,
                        self.metadata_manager.local_metadata
                    )
                    print(f"Admin Perform report generated: {report_path}")
                except Exception as e:
                    print(f"Failed to generate admin perform report: {str(e)}")
                    
        except Exception as e:
            print(f"Error processing admin perform metadata: {str(e)}")
        
        self.start_tool_selection_phase()

    def start_tool_selection_phase(self):
        # Pass the metadata_manager to the tool selection dialog
        self.tool_selection_dialog = ToolSelectionPerformDialog(self.on_application_exit, self.metadata_manager)
        self.tool_selection_dialog.exec()

    def on_application_exit(self):
        # Generate final session summary report
        try:
            session_report_path = self.report_generator.generate_session_summary_report(
                self.metadata_manager.global_metadata
            )
            print(f"Final session summary report generated: {session_report_path}")
        except Exception as e:
            print(f"Failed to generate session summary report: {str(e)}")
        
        print("OST Application flow complete. Exiting.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApplication()
    sys.exit(app.exec())
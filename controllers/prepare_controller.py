from PySide6.QtWidgets import QWidget, QDialog
from controllers.base_controller import BaseController

from Prepare.EDTA.Prepare_EDTA_c import Prepare_EDTA_c
from Prepare.EDTC.Prepare_EDTC_c import Prepare_EDTC_c
from Prepare.MRBN.Prepare_MRBN_c import Prepare_MRBN_c
from Prepare.MRFA.Prepare_MRFA_c import Prepare_MRFA_c
from Prepare.MRHY.Prepare_MRHY_c import Prepare_MRHY_c
from Prepare.MRPQ.Prepare_MRPQ_c import Prepare_MRPQ_c
from Prepare.MRSC.Prepare_MRSC_c import Prepare_MRSC_c
from Prepare.MRPO.Prepare_MRPO_c import Prepare_MRPO_c
from Prepare.MRPC.Prepare_MRPC_c import Prepare_MRPC_c
from Prepare.MRMS.Prepare_MRMS_c import Prepare_MRMS_c

class PrepareController(BaseController):
    def __init__(self, on_complete_callback, toolstring=None, metadata_manager=None):
        self.metadata_manager = metadata_manager
        self.current_tool_name = None  # Track current tool for metadata
        
        # Use passed toolstring or default for testing
        # If an empty list is passed, use it (don't replace with default)
        if toolstring is None:
            self.toolstring = ["EDTA", "EDTC", "MRBN", "MRFA", "MRHY", "MRPQ", "MRSC", "MRPO", "MRPC", "MRMS"]
        else:
            self.toolstring = toolstring
            
        print(f"PrepareController initialized with toolstring: {self.toolstring}")
        
        # Initialize the widget first
        QWidget.__init__(self)  # Initialize QWidget first
        
        # Now build the dialog flow (wizards can use self as parent)
        dialog_list = self.build_prepare_flow()
        
        # Set the required attributes for BaseController compatibility
        self.dialog_list = dialog_list
        self.on_complete_callback = on_complete_callback
        self.current_index = 0
        
        # Don't call base controller's init_ui since it doesn't work with modal wizards
        # self.init_ui()  # Skip this
        
        # Connect navigation buttons after initialization
        self.setup_navigation()

    def build_prepare_flow(self):
        dialog_flow = []
        print(f"Building prepare flow for toolstring: {self.toolstring}")
        
        # Track the tools we successfully created wizards for
        validated_toolstring = []
        
        # Counter for each tool type to handle multiple instances
        tool_counters = {}
        
        for tool in self.toolstring:
            try:
                # Track multiple instances of the same tool
                if tool in tool_counters:
                    tool_counters[tool] += 1
                    # For multiple instances, append a counter to the tool name for tracking
                    unique_tool_name = f"{tool}_{tool_counters[tool]}"
                else:
                    tool_counters[tool] = 1
                    unique_tool_name = tool
                
                print(f"Creating wizard for tool: {tool} (instance {tool_counters[tool]})")
                
                # Create the appropriate wizard based on tool type
                wizard = None
                if tool == "EDTA":
                    wizard = Prepare_EDTA_c(None)
                elif tool == "EDTC":
                    wizard = Prepare_EDTC_c(None)
                elif tool == "MRBN":
                    wizard = Prepare_MRBN_c(None)
                elif tool == "MRFA":
                    wizard = Prepare_MRFA_c(None)
                elif tool == "MRHY":
                    wizard = Prepare_MRHY_c(None)
                elif tool == "MRPQ":
                    wizard = Prepare_MRPQ_c(None)
                elif tool == "MRSC":
                    wizard = Prepare_MRSC_c(None)
                elif tool == "MRPO":
                    wizard = Prepare_MRPO_c(None)
                elif tool == "MRPC":
                    wizard = Prepare_MRPC_c(None)
                elif tool == "MRMS":
                    wizard = Prepare_MRMS_c(None)
                else:
                    print(f"Warning: Unknown tool '{tool}' in toolstring, skipping")
                    continue
                
                # Store tool name in the wizard for later reference
                # Use the unique name to distinguish multiple instances
                wizard.tool_name = unique_tool_name
                wizard.tool_type = tool  # Store the original tool type
                # Also set Module attribute for backward compatibility
                wizard.Module = tool
                
                # Add to dialog flow
                dialog_flow.append(wizard)
                validated_toolstring.append(unique_tool_name)
                
                print(f"Added wizard for {unique_tool_name}")
                
            except Exception as e:
                print(f"Error creating wizard for tool {tool}: {e}")
                import traceback
                traceback.print_exc()
        
        # Update toolstring with only the tools we successfully created
        self.toolstring = validated_toolstring
        
        print(f"Prepare flow built with {len(dialog_flow)} dialogs")
        return dialog_flow
    
    def setup_navigation(self):
        """Connect navigation for wizard dialogs"""
        print("Setting up navigation for prepare wizards")
        
        for i, dialog in enumerate(self.dialog_list):
            # Store tool name in dialog for metadata collection
            if not hasattr(dialog, 'tool_name'):
                dialog.tool_name = self.toolstring[i]
            
            print(f"Setting up navigation for wizard {i}: {dialog.tool_name}")
            
            # Make sure the wizard knows how to find the parent controller
            dialog.parent_controller = self
    
    def init_tool_metadata(self, tool_name):
        """Initialize local metadata for a specific tool"""
        if self.metadata_manager:
            self.current_tool_name = tool_name
            
            # Extract original tool type if this is a unique instance
            tool_type = tool_name
            if '_' in tool_name and tool_name.split('_')[-1].isdigit():
                tool_type = tool_name.split('_')[0]
                
            self.metadata_manager.init_local_data(tool_name, "Prepare")
            self.metadata_manager.add_local_note(f"Started preparation for {tool_type}")
            print(f"Initialized metadata for tool: {tool_name} (type: {tool_type})")

    def handle_wizard_complete(self, result, dialog_index):
        """Handle completion of a wizard-based tool dialog"""
        print(f"Wizard completed with result: {result} for dialog index: {dialog_index}")
        
        # Get the tool name
        dialog = self.dialog_list[dialog_index]
        # Look for the tool_name attribute which was set during initialization
        # Fall back to the toolstring entry or a generic name if not found
        tool_name = getattr(dialog, 'tool_name', 
                          self.toolstring[dialog_index] if dialog_index < len(self.toolstring) else f"Wizard_{dialog_index}")
        
        if result == 1:  # QDialog.Accepted
            print(f"Processing wizard completion for tool: {tool_name}")
            
            # Initialize metadata for wizard (if not already done)
            if self.metadata_manager and self.current_tool_name != tool_name:
                self.current_tool_name = tool_name
                self.metadata_manager.init_local_data(tool_name, "Prepare")
                self.metadata_manager.add_local_note(f"Started preparation for {tool_name}")
            
            # Collect wizard data
            if self.metadata_manager:
                if hasattr(dialog, 'get_metadata'):
                    wizard_data = dialog.get_metadata()
                    # Store wizard metadata in various places for compatibility
                    self.metadata_manager.set_local_data("wizard_data", "collected_data", wizard_data)
                    self.metadata_manager.set_local_data("Prepare Phase Steps", "wizard_metadata", wizard_data)
                    
                    # Store directly in user_inputs for reports
                    if "user_inputs" not in self.metadata_manager.local_metadata:
                        self.metadata_manager.local_metadata["user_inputs"] = {}
                    
                    # If wizard_data is a dict, merge it with user_inputs
                    if isinstance(wizard_data, dict):
                        self.metadata_manager.local_metadata["user_inputs"].update(wizard_data)
                    else:
                        # If it's not a dict, store as a single entry
                        self.metadata_manager.local_metadata["user_inputs"]["Wizard Data"] = wizard_data
                    
                    print(f"Collected wizard metadata for {tool_name}")
                    
                elif hasattr(dialog, 'get_data'):
                    wizard_data = dialog.get_data()
                    # Store legacy wizard data
                    self.metadata_manager.set_local_data("wizard_data", "collected_data", wizard_data)
                    self.metadata_manager.set_local_data("Prepare Phase Steps", "legacy_data", wizard_data)
                    
                    # Store directly in user_inputs for reports
                    if "user_inputs" not in self.metadata_manager.local_metadata:
                        self.metadata_manager.local_metadata["user_inputs"] = {}
                    
                    # If wizard_data is a dict, merge it with user_inputs
                    if isinstance(wizard_data, dict):
                        self.metadata_manager.local_metadata["user_inputs"].update(wizard_data)
                    else:
                        # If it's not a dict, store as a single entry
                        self.metadata_manager.local_metadata["user_inputs"]["Wizard Data"] = wizard_data
                    
                    print(f"Collected wizard data for {tool_name}")
                
                # Add completion note
                self.metadata_manager.add_local_note(f"Completed preparation for {tool_name}")
                
                # Generate wizard report
                self.generate_tool_prepare_report(tool_name)
        else:
            print(f"Wizard was cancelled or rejected for dialog index: {dialog_index}")
            print(f"Automatically skipping {tool_name} and continuing with next tool")
            # Add a note about the skipped tool
            if self.metadata_manager:
                self.metadata_manager.add_local_note(f"Tool {tool_name} was skipped (cancelled by user)")
        
        # Move to the next tool regardless of whether this one was completed or cancelled
        print(f"Moving to next tool after {tool_name} (result was {result})")
        
        # IMPORTANT: Move to the next tool after handling the current one
        self.move_to_next_tool()
    
    def move_to_next_tool(self):
        """Move to the next tool in the sequence"""
        # Increment the index
        next_index = self.current_index + 1
        
        if next_index >= len(self.dialog_list):
            # All dialogs completed
            print(f"All prepare dialogs completed ({len(self.dialog_list)} total), calling completion callback")
            if self.on_complete_callback:
                self.on_complete_callback()
            self.close()
        else:
            # Continue to the next tool
            print(f"Moving to next tool at index {next_index} of {len(self.dialog_list)}")
            try:
                # Move to the next index
                self.current_index = next_index
                
                # Get the next dialog
                next_dialog = self.dialog_list[self.current_index]
                next_tool_name = self.toolstring[self.current_index]
                
                # Initialize metadata for next tool
                self.init_tool_metadata(next_tool_name)
                
                # Execute the next wizard
                print(f"Executing next wizard for {next_tool_name}")
                
                # Execute the wizard - this is a blocking call
                result = next_dialog.exec()
                print(f"Wizard exec() for {next_tool_name} returned: {result}")
                
                # Handle the result
                self.handle_wizard_complete(result, self.current_index)
            except Exception as e:
                print(f"Error executing next wizard: {e}")
                import traceback
                traceback.print_exc()
                # Try to continue to the next tool
                self.move_to_next_tool()
    
    def continue_to_next_tool(self):
        """Redirect to move_to_next_tool for backward compatibility"""
        print("continue_to_next_tool called, redirecting to move_to_next_tool")
        self.move_to_next_tool()
    
    def generate_tool_prepare_report(self, tool_name):
        """Generate a report for individual tool preparation"""
        if not self.metadata_manager:
            return None
            
        try:
            # Import report generator
            from report_generator import ReportGenerator
            report_generator = ReportGenerator()
            
            # Ensure the correct tool name is set in the metadata
            if "tool_info" in self.metadata_manager.local_metadata:
                # Extract original tool type if this is a unique instance
                display_name = tool_name
                if '_' in tool_name and tool_name.split('_')[-1].isdigit():
                    display_name = tool_name.split('_')[0]
                
                # Update the tool name in the metadata
                self.metadata_manager.local_metadata["tool_info"]["tool_name"] = display_name
                print(f"Updated tool name in report to: {display_name}")
            
            # Make sure user_inputs exists and isn't empty
            if "user_inputs" not in self.metadata_manager.local_metadata or not self.metadata_manager.local_metadata["user_inputs"]:
                # Get wizard data from other locations and add to user_inputs
                wizard_data = self.metadata_manager.local_metadata.get("wizard_data", {}).get("collected_data", {})
                if wizard_data:
                    self.metadata_manager.local_metadata["user_inputs"] = wizard_data
                    print(f"Recovered wizard data for report: {tool_name}")
            
            # Debug output to see what's in user_inputs
            print(f"User inputs for {tool_name}: {self.metadata_manager.local_metadata.get('user_inputs', {})}")
            
            # Finalize local data for this tool
            final_local_data = self.metadata_manager.finalize_local_data()
            
            # Generate tool-specific prepare report
            report_path = report_generator.generate_tool_report(
                self.metadata_manager.get_global_data(),
                final_local_data
            )
            
            print(f"Generated prepare report for {tool_name}: {report_path}")
            
            # Add to processed tools
            self.metadata_manager.add_processed_tool(tool_name, "Prepare", True)
            
            # Clear local data for next tool
            self.metadata_manager.clear_local_data()
            
            return report_path
            
        except Exception as e:
            print(f"Error generating prepare report for {tool_name}: {e}")
            return None
    
    def show_next(self):
        """Override show_next to handle wizard dialogs"""
        print("show_next called, redirecting to move_to_next_tool")
        self.move_to_next_tool()
    
    def show(self):
        """Override show to handle wizard dialogs"""
        if not self.dialog_list or not self.toolstring:
            print("No dialog list or toolstring available")
            if self.on_complete_callback:
                self.on_complete_callback()
            return
        
        print(f"Starting prepare phase with {len(self.dialog_list)} wizards")
            
        # Initialize metadata for the first tool
        first_tool = self.toolstring[0]
        print(f"Initializing metadata for first tool: {first_tool}")
        self.init_tool_metadata(first_tool)
        
        # Execute the first wizard dialog
        first_dialog = self.dialog_list[0]
        print(f"Executing first wizard for {first_tool}")
        
        try:
            # Execute the wizard - this is a blocking call
            result = first_dialog.exec()
            print(f"Wizard exec() returned: {result}")
            
            # Handle wizard result immediately since exec() is blocking
            self.handle_wizard_complete(result, 0)
        except Exception as e:
            print(f"Error executing wizard: {e}")
            import traceback
            traceback.print_exc()
            # Skip this wizard and continue
            print("Skipping failed wizard and continuing...")
            self.move_to_next_tool()
    
    def keyPressEvent(self, event):
        """Handle keyboard navigation"""
        from PySide6.QtCore import Qt
        if event.key() == Qt.Key_Escape and self.current_index > 0:
            self.show_back()
        else:
            super().keyPressEvent(event)
    
    def collect_prepare_data(self):
        """Collect data from all prepare dialogs"""
        if not self.metadata_manager:
            return None
            
        # Get the original tool types (without instance numbers)
        original_tools = []
        for tool in self.toolstring:
            if '_' in tool and tool.split('_')[-1].isdigit():
                # Extract the original tool type
                original_tools.append(tool.split('_')[0])
            else:
                original_tools.append(tool)
        
        prepare_data = {
            "tools_prepared": original_tools
        }
        
        # Store the prepare data in metadata
        self.metadata_manager.set_global_category("prepare_data", prepare_data)
        print(f"Prepare data collected: {prepare_data}")
        
        return prepare_data
    
    def close(self):
        """Override close to collect prepare data before closing"""
        if self.metadata_manager:
            self.collect_prepare_data()
        super().close()
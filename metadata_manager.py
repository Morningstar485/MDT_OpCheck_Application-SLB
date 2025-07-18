"""
Metadata Manager for OST Application
Handles global and local metadata collection and management
"""

from datetime import datetime
from typing import Dict, Any, Optional


class MetadataManager:
    def __init__(self, admin_directory=None):
        """
        Initialize the metadata manager with admin directory integration
        
        Args:
            admin_directory: AdminDirectory instance for global metadata
        """
        self.admin_directory = admin_directory
        
        # Global metadata (can be backed by admin directory)
        self.global_metadata = {
            "session_info": {
                "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "application_version": "Project V3",
                "session_id": datetime.now().strftime("%Y%m%d_%H%M%S")
            },
            "design_data": {},
            "toolstring_declaration": {},
            "admin_data": {},
            "prepare_data": {}
        }
        
        # Local metadata (temporary, tool-specific)
        self.local_metadata = {}
        
        # If admin directory is available, sync global metadata
        if self.admin_directory:
            self.sync_with_admin_directory()
    
    def sync_with_admin_directory(self):
        """Sync global metadata with admin directory"""
        if not self.admin_directory:
            return
        
        # Get admin data and sync with global metadata
        admin_data = self.admin_directory.get_admin_data()
        if admin_data:
            # Update global metadata with admin data
            self.global_metadata.update({
                "session_info": admin_data.get("session_info", self.global_metadata["session_info"]),
                "design_data": admin_data.get("design_choices", {}),
                "toolstring_declaration": admin_data.get("toolstring_selection", {}),
                "admin_data": admin_data.get("global_settings", {}),
                "user_profile": admin_data.get("user_profile", {})
            })
    
    def set_global_data(self, category: str, key: str, value: Any) -> None:
        """
        Set global metadata that persists across tools
        
        Args:
            category: Category of metadata (session_info, design_data, etc.)
            key: Specific key within the category
            value: Value to store
        """
        if category not in self.global_metadata:
            self.global_metadata[category] = {}
        
        self.global_metadata[category][key] = value
        
        # Sync with admin directory if available
        if self.admin_directory:
            self.admin_directory.set_admin_data(category, key, value)
        
    def set_global_data(self, category: str, key: str, value: Any) -> None:
        """
        Set global metadata that persists across tools
        
        Args:
            category: Category of metadata (session_info, design_data, etc.)
            key: Specific key within the category
            value: Value to store
        """
        if category not in self.global_metadata:
            self.global_metadata[category] = {}
        
        self.global_metadata[category][key] = value
        
    def get_global_data(self, category: Optional[str] = None, key: Optional[str] = None) -> Any:
        """
        Get global metadata
        
        Args:
            category: Category of metadata to retrieve (optional)
            key: Specific key to retrieve (optional)
            
        Returns:
            Requested metadata or entire global metadata if no parameters
        """
        if category is None:
            return self.global_metadata
        
        if category not in self.global_metadata:
            return None
            
        if key is None:
            return self.global_metadata[category]
            
        return self.global_metadata[category].get(key)
    
    def set_global_category(self, category: str, data: Dict[str, Any]) -> None:
        """
        Set entire category of global metadata
        
        Args:
            category: Category name
            data: Dictionary of data to set for the category
        """
        self.global_metadata[category] = data
        
    def init_local_data(self, tool_name: str, phase: str) -> None:
        """
        Initialize local metadata for a specific tool/phase
        
        Args:
            tool_name: Name of the tool (e.g., "MRMS", "MRSC")
            phase: Phase of operation (e.g., "Prepare", "Perform")
        """
        self.local_metadata = {
            "tool_info": {
                "tool_name": tool_name,
                "phase": phase,
                "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "test_results": {},
            "user_inputs": {},  # Use standardized lowercase key
            "validation_results": {},
            "notes": []
        }
        
    def set_local_data(self, category: str, key: str, value: Any) -> None:
        """
        Set local metadata for current tool
        
        Args:
            category: Category of local metadata (test_results, user_inputs, etc.)
            key: Specific key within the category
            value: Value to store
        """
        if category not in self.local_metadata:
            self.local_metadata[category] = {}
            
        self.local_metadata[category][key] = value
        
    def get_local_data(self, category: Optional[str] = None, key: Optional[str] = None) -> Any:
        """
        Get local metadata for current tool
        
        Args:
            category: Category of metadata to retrieve (optional)
            key: Specific key to retrieve (optional)
            
        Returns:
            Requested metadata or entire local metadata if no parameters
        """
        if category is None:
            return self.local_metadata
        
        if category not in self.local_metadata:
            return None
            
        if key is None:
            return self.local_metadata[category]
            
        return self.local_metadata[category].get(key)
    
    def add_local_note(self, note: str) -> None:
        """
        Add a note to the local metadata
        
        Args:
            note: Note to add
        """
        if "notes" not in self.local_metadata:
            self.local_metadata["notes"] = []
        self.local_metadata["notes"].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "note": note
        })
        
    def finalize_local_data(self) -> Dict[str, Any]:
        """
        Finalize local metadata by adding end time and returning a copy
        
        Returns:
            Copy of local metadata with end time added
        """
        if "tool_info" in self.local_metadata:
            self.local_metadata["tool_info"]["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        # Return a copy of the local metadata before clearing
        return self.local_metadata.copy()
        
    def clear_local_data(self) -> None:
        """Clear local metadata after report generation"""
        self.local_metadata = {}
        
    def get_session_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the current session
        
        Returns:
            Dictionary containing session summary information
        """
        return {
            "session_info": self.global_metadata.get("session_info", {}),
            "toolstring": self.global_metadata.get("toolstring_declaration", {}).get("selected_tools", []),
            "design_summary": self.global_metadata.get("design_data", {}),
            "total_tools_processed": len(self.global_metadata.get("processed_tools", []))
        }
        
    def add_processed_tool(self, tool_name: str, phase: str, success: bool = True) -> None:
        """
        Add a tool to the list of processed tools
        
        Args:
            tool_name: Name of the processed tool
            phase: Phase that was completed
            success: Whether the tool processing was successful
        """
        if "processed_tools" not in self.global_metadata:
            self.global_metadata["processed_tools"] = []
            
        tool_entry = {
            "tool_name": tool_name,
            "phase": phase,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "success": success
        }
        
        self.global_metadata["processed_tools"].append(tool_entry)
        
        # Add to admin directory if available
        if self.admin_directory:
            self.admin_directory.add_session_event(
                "tool_completion",
                f"{tool_name} {phase} phase completed",
                tool_entry
            )
    
    def integrate_tool_data(self, tool_wizard) -> Dict[str, Any]:
        """
        Integrate data from a tool wizard's local directory
        
        Args:
            tool_wizard: BaseToolWizard instance with local directory
            
        Returns:
            Report-ready data from the tool
        """
        if not hasattr(tool_wizard, 'get_report_data'):
            return {}
        
        # Get report data from tool
        tool_report_data = tool_wizard.get_report_data()
        
        # Add to processed tools
        tool_name = tool_wizard.tool_name
        self.add_processed_tool(tool_name, "Prepare", True)
        
        return tool_report_data
    
    def get_admin_metadata(self) -> Dict[str, Any]:
        """Get admin metadata from admin directory"""
        if self.admin_directory:
            return self.admin_directory.get_admin_data()
        return {}

"""
Report Generator for OST Application
Generates PDF reports from metadata collected during tool operations
"""

import os
from datetime import datetime
from typing import Dict, Any, Optional
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT


class ReportGenerator:
    def __init__(self, output_dir: str = "Reports"):
        """
        Initialize the report generator
        
        Args:
            output_dir: Directory to save generated reports
        """
        self.output_dir = output_dir
        self.ensure_output_directory()
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
        
    def ensure_output_directory(self) -> None:
        """Ensure the output directory exists"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def setup_custom_styles(self) -> None:
        """Setup custom paragraph styles for the report"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=18,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=colors.black
        ))
        
        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceAfter=10,
            spaceBefore=10,
            textColor=colors.darkblue,
            leftIndent=0
        ))
        
        # Subsection header style
        self.styles.add(ParagraphStyle(
            name='SubsectionHeader',
            parent=self.styles['Heading3'],
            fontSize=12,
            spaceAfter=6,
            spaceBefore=6,
            textColor=colors.blue,
            leftIndent=5
        ))
        
        # Data style
        self.styles.add(ParagraphStyle(
            name='DataText',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=10,
            spaceAfter=3
        ))
        
    def generate_tool_report(self, global_metadata: Dict[str, Any], local_metadata: Dict[str, Any]) -> str:
        """
        Generate a PDF report for a specific tool operation
        
        Args:
            global_metadata: Global application metadata
            local_metadata: Tool-specific local metadata
            
        Returns:
            Path to the generated report file
        """
        # Generate filename
        tool_name = local_metadata.get("tool_info", {}).get("tool_name", "Unknown")
        phase = local_metadata.get("tool_info", {}).get("phase", "Unknown")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Report_{tool_name}_{phase}_{timestamp}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        
        # Create PDF document
        doc = SimpleDocTemplate(filepath, pagesize=A4, 
                              rightMargin=36, leftMargin=36, 
                              topMargin=36, bottomMargin=18)
        
        # Build report content
        story = []
        
        # Title
        title = f"OST Report - {tool_name} {phase} Operation"
        story.append(Paragraph(title, self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Session Information
        story.extend(self._build_session_info_section(global_metadata))
        
        # Tool Operation Details
        story.extend(self._build_tool_operation_section(local_metadata))
        
        # Include design data for design phase reports
        if phase == "Design":
            design_data = global_metadata.get("design_data", {})
            if design_data:
                story.append(Paragraph("Design Choices", self.styles['SectionHeader']))
                story.extend(self._build_key_value_section(design_data))
        
        # Build PDF
        doc.build(story)
        
        return filepath
        
    def _build_session_info_section(self, global_metadata: Dict[str, Any]) -> list:
        """Build the session information section"""
        story = []
        story.append(Paragraph("Session Information", self.styles['SectionHeader']))
        
        session_info = global_metadata.get("session_info", {})
        
        # Create session info table
        session_data = [
            ["Session Start Time", session_info.get("start_time", "N/A")],
            ["Application Version", session_info.get("application_version", "N/A")],
            ["Session ID", session_info.get("session_id", "N/A")]
        ]
        
        # Add admin data if available
        admin_data = global_metadata.get("admin_data", {})
        if admin_data:
            session_data.extend([
                ["Engineer Name", admin_data.get("Engineer Name", "N/A")],
                ["Specialist Name", admin_data.get("Specialist Name", "N/A")],
                ["Well Name", admin_data.get("Well Name", "N/A")],
                ["Rig Name", admin_data.get("Rig Name", "N/A")],
                ["Cable Length", admin_data.get("Cable Length", "N/A")],
                ["Cable Type", admin_data.get("Cable Type", "N/A")]
            ])
        
        table = Table(session_data, colWidths=[1.75*inch, 3.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('BACKGROUND', (1, 0), (1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(table)
        story.append(Spacer(1, 20))
        
        return story
        
    def _build_tool_operation_section(self, local_metadata: Dict[str, Any]) -> list:
        """Build the tool operation details section"""
        story = []
        story.append(Paragraph("Tool Operation Details", self.styles['SectionHeader']))
        
        tool_info = local_metadata.get("tool_info", {})
        
        # Tool info table
        tool_data = [
            ["Tool Name", tool_info.get("tool_name", "N/A")],
            ["Operation Phase", tool_info.get("phase", "N/A")],
            ["Start Time", tool_info.get("start_time", "N/A")],
            ["End Time", tool_info.get("end_time", "N/A")]
        ]
        
        table = Table(tool_data, colWidths=[1.75*inch, 3.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('BACKGROUND', (1, 0), (1, -1), colors.lightcyan),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(table)
        story.append(Spacer(1, 15))
        
        # Test Results
        test_results = local_metadata.get("test_results", {})
        if test_results:
            story.append(Paragraph("Test Results", self.styles['SubsectionHeader']))
            story.extend(self._build_key_value_section(test_results))
            
        # User Inputs
        user_inputs = local_metadata.get("user_inputs", {})
        if not user_inputs:
            # Check for alternate keys (for backward compatibility)
            user_inputs = local_metadata.get("User Inputs", {})
            
        if user_inputs:
            story.append(Paragraph("User Inputs", self.styles['SubsectionHeader']))
            
            # Format user inputs as individual lines rather than a table
            for key, value in user_inputs.items():
                if isinstance(value, dict):
                    # Special handling for module details
                    is_module_details = key.lower() in ["module details", "detailed_modules"] or any(k.startswith("Module ") for k in value.keys())
                    
                    if is_module_details:
                        # Format module details with each module on its own line
                        story.append(Paragraph(f"<b>{key}:</b>", self.styles['DataText']))
                        
                        # Sort modules by position if possible
                        sorted_keys = sorted(value.keys(), 
                                          key=lambda k: int(k.split(" ")[1]) if k.startswith("Module ") and k.split(" ")[1].isdigit() else 999)
                        
                        for module_key in sorted_keys:
                            module_data = value[module_key]
                            if isinstance(module_data, dict):
                                # Format each module's details
                                story.append(Paragraph(f"<b>{module_key}:</b>", 
                                                    ParagraphStyle(
                                                        name='ModuleHeader',
                                                        parent=self.styles['DataText'],
                                                        leftIndent=20,
                                                        spaceBefore=5
                                                    )))
                                
                                # Display each attribute of the module
                                for attr_key, attr_value in module_data.items():
                                    story.append(Paragraph(f"└─ <b>{attr_key}:</b> {attr_value}", 
                                                        ParagraphStyle(
                                                            name='ModuleDetail',
                                                            parent=self.styles['DataText'],
                                                            leftIndent=40
                                                        )))
                            else:
                                # Simple module entry
                                story.append(Paragraph(f"└─ <b>{module_key}:</b> {module_data}", 
                                                    ParagraphStyle(
                                                        name='ModuleItem',
                                                        parent=self.styles['DataText'],
                                                        leftIndent=30
                                                    )))
                    else:
                        # For nested dictionaries, format as paragraphs with indentation
                        story.append(Paragraph(f"<b>{key}:</b>", self.styles['DataText']))
                        for sub_key, sub_value in value.items():
                            story.append(Paragraph(f"└─ <b>{sub_key}:</b> {sub_value}", 
                                                ParagraphStyle(
                                                    name='IndentedUserInput',
                                                    parent=self.styles['DataText'],
                                                    leftIndent=40
                                                )))
                elif isinstance(value, list):
                    # For lists that represent toolstrings or tool collections, format with one item per line
                    # Check if this is likely a toolstring by key name or content
                    is_toolstring = (key.lower() in ["tools_prepared", "toolstring", "selected_tools", "modules"] or 
                                    (len(value) > 0 and all(isinstance(item, str) and len(item) <= 10 for item in value)))
                    
                    if is_toolstring:
                        # Display toolstring with one tool per line
                        story.append(Paragraph(f"<b>{key}:</b>", self.styles['DataText']))
                        for item in value:
                            story.append(Paragraph(f"• {item}", 
                                                ParagraphStyle(
                                                    name='ToolItem',
                                                    parent=self.styles['DataText'],
                                                    leftIndent=40
                                                )))
                    else:
                        # For other lists, format as a comma-separated string
                        story.append(Paragraph(f"<b>{key}:</b> {', '.join(str(item) for item in value)}", 
                                            self.styles['DataText']))
                else:
                    # For simple key-value pairs
                    story.append(Paragraph(f"<b>{key}:</b> {value}", self.styles['DataText']))
                
            story.append(Spacer(1, 10))
            
        # Notes
        notes = local_metadata.get("notes", [])
        if notes:
            story.append(Paragraph("Notes", self.styles['SubsectionHeader']))
            for note in notes:
                note_text = f"[{note.get('timestamp', 'N/A')}] {note.get('note', '')}"
                story.append(Paragraph(note_text, self.styles['DataText']))
                
        story.append(Spacer(1, 20))
        
        return story
        
    def _build_global_context_section(self, global_metadata: Dict[str, Any]) -> list:
        """Build the global context section"""
        story = []
        story.append(Paragraph("Global Context", self.styles['SectionHeader']))
        
        # Toolstring Declaration
        toolstring_data = global_metadata.get("toolstring_declaration", {})
        if toolstring_data:
            story.append(Paragraph("Toolstring Declaration", self.styles['SubsectionHeader']))
            story.extend(self._build_key_value_section(toolstring_data))
            
        # Design Data
        design_data = global_metadata.get("design_data", {})
        if design_data:
            story.append(Paragraph("Design Choices", self.styles['SubsectionHeader']))
            story.extend(self._build_key_value_section(design_data))
            
        # Prepare Data
        prepare_data = global_metadata.get("prepare_data", {})
        if prepare_data:
            story.append(Paragraph("Preparation Data", self.styles['SubsectionHeader']))
            story.extend(self._build_key_value_section(prepare_data))
            
        return story
        
    def _build_key_value_section(self, data: Dict[str, Any]) -> list:
        """Build a key-value section for displaying metadata"""
        story = []
        
        if not data:
            story.append(Paragraph("No data available", self.styles['DataText']))
            return story
        
        # Format each key-value pair as a separate paragraph instead of a table
        for key, value in data.items():
            if isinstance(value, dict):
                # Special handling for module details
                is_module_details = key.lower() in ["module details", "detailed_modules"] or any(k.startswith("Module ") for k in value.keys())
                
                if is_module_details:
                    # Format module details with each module on its own line
                    story.append(Paragraph(f"<b>{key}:</b>", self.styles['DataText']))
                    
                    # Sort modules by position if possible
                    sorted_keys = sorted(value.keys(), 
                                      key=lambda k: int(k.split(" ")[1]) if k.startswith("Module ") and k.split(" ")[1].isdigit() else 999)
                    
                    for module_key in sorted_keys:
                        module_data = value[module_key]
                        if isinstance(module_data, dict):
                            # Format each module's details
                            story.append(Paragraph(f"<b>{module_key}:</b>", 
                                                ParagraphStyle(
                                                    name='ModuleHeader',
                                                    parent=self.styles['DataText'],
                                                    leftIndent=20,
                                                    spaceBefore=5
                                                )))
                            
                            # Display each attribute of the module
                            for attr_key, attr_value in module_data.items():
                                story.append(Paragraph(f"└─ <b>{attr_key}:</b> {attr_value}", 
                                                    ParagraphStyle(
                                                        name='ModuleDetail',
                                                        parent=self.styles['DataText'],
                                                        leftIndent=40
                                                    )))
                        else:
                            # Simple module entry
                            story.append(Paragraph(f"└─ <b>{module_key}:</b> {module_data}", 
                                                ParagraphStyle(
                                                    name='ModuleItem',
                                                    parent=self.styles['DataText'],
                                                    leftIndent=30
                                                )))
                else:
                    # For regular nested dictionaries, format as paragraphs with indentation
                    story.append(Paragraph(f"<b>{key}:</b>", self.styles['DataText']))
                    for sub_key, sub_value in value.items():
                        story.append(Paragraph(f"└─ <b>{sub_key}:</b> {sub_value}", 
                                            ParagraphStyle(
                                                name='IndentedData',
                                                parent=self.styles['DataText'],
                                                leftIndent=40
                                            )))
            elif isinstance(value, list):
                # For lists that represent toolstrings or tool collections, format with one item per line
                # Check if this is likely a toolstring by key name or content
                is_toolstring = (key.lower() in ["tools_prepared", "toolstring", "selected_tools", "modules"] or 
                                (len(value) > 0 and all(isinstance(item, str) and len(item) <= 10 for item in value)))
                
                if is_toolstring:
                    # Display toolstring with one tool per line
                    story.append(Paragraph(f"<b>{key}:</b>", self.styles['DataText']))
                    for item in value:
                        story.append(Paragraph(f"• {item}", 
                                            ParagraphStyle(
                                                name='ToolItem',
                                                parent=self.styles['DataText'],
                                                leftIndent=30
                                            )))
                else:
                    # For other lists, format as a comma-separated string
                    story.append(Paragraph(f"<b>{key}:</b> {', '.join(str(item) for item in value)}", 
                                        self.styles['DataText']))
            else:
                # For simple key-value pairs
                story.append(Paragraph(f"<b>{key}:</b> {value}", self.styles['DataText']))
            
        story.append(Spacer(1, 10))
        return story
        
    def generate_session_summary_report(self, global_metadata: Dict[str, Any]) -> str:
        """
        Generate a summary report for the entire session
        
        Args:
            global_metadata: Global application metadata
            
        Returns:
            Path to the generated summary report file
        """
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Session_Summary_{timestamp}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        
        # Create PDF document
        doc = SimpleDocTemplate(filepath, pagesize=A4,
                              rightMargin=36, leftMargin=36,
                              topMargin=36, bottomMargin=18)
        
        # Build report content
        story = []
        
        # Title
        story.append(Paragraph("OST Session Summary Report", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Session Information
        story.extend(self._build_session_info_section(global_metadata))
        
        # Processed Tools Summary
        processed_tools = global_metadata.get("processed_tools", [])
        if processed_tools:
            story.append(Paragraph("Processed Tools Summary", self.styles['SectionHeader']))
            
            tools_data = [["Tool Name", "Phase", "Timestamp", "Status"]]
            for tool in processed_tools:
                status = "Success" if tool.get("success", True) else "Failed"
                tools_data.append([
                    tool.get("tool_name", "N/A"),
                    tool.get("phase", "N/A"),
                    tool.get("timestamp", "N/A"),
                    status
                ])
                
            table = Table(tools_data, colWidths=[1.5*inch, 1*inch, 1.5*inch, 1*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
            
        # Global Context
        # Build the global context section with proper formatting
        story.append(Paragraph("Global Context", self.styles['SectionHeader']))
        
        # Admin Data
        admin_data = global_metadata.get("admin_data", {})
        if admin_data:
            story.append(Paragraph("Admin Information", self.styles['SubsectionHeader']))
            story.extend(self._build_key_value_section({"Admin Data": admin_data}))
        
        # Toolstring Declaration
        toolstring_data = global_metadata.get("toolstring_declaration", {})
        if toolstring_data:
            story.append(Paragraph("Toolstring Declaration", self.styles['SubsectionHeader']))
            # Format the toolstring in an easy-to-read way
            selected_tools = toolstring_data.get("selected_tools", [])
            if selected_tools:
                story.append(Paragraph("<b>Selected Tools:</b>", self.styles['DataText']))
                for tool in selected_tools:
                    story.append(Paragraph(f"• {tool}", 
                                        ParagraphStyle(
                                            name='ToolItem',
                                            parent=self.styles['DataText'],
                                            leftIndent=30
                                        )))
            
            # Add other toolstring metadata
            for key, value in toolstring_data.items():
                if key != "selected_tools" and key != "detailed_modules":
                    if isinstance(value, dict):
                        story.append(Paragraph(f"<b>{key}:</b>", self.styles['DataText']))
                        for sub_key, sub_value in value.items():
                            story.append(Paragraph(f"└─ <b>{sub_key}:</b> {sub_value}", 
                                                ParagraphStyle(
                                                    name='IndentedData',
                                                    parent=self.styles['DataText'],
                                                    leftIndent=40
                                                )))
                    elif isinstance(value, list):
                        # Skip detailed_modules and selected_tools, handled separately
                        continue
                    else:
                        story.append(Paragraph(f"<b>{key}:</b> {value}", self.styles['DataText']))
            
            story.append(Spacer(1, 10))
        
        # Remove Global Context section for session summary reports
        
        # Build PDF
        doc.build(story)
        
        return filepath

    def generate_phase_summary_report(self, global_metadata: Dict[str, Any], phase: str) -> str:
        """
        Generate a summary report for an entire phase (e.g., Prepare, Perform)
        
        Args:
            global_metadata: Global application metadata
            phase: Phase name (e.g., "Prepare", "Perform")
            
        Returns:
            Path to the generated report file
        """
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Report_{phase}_Phase_Summary_{timestamp}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        
        # Create PDF document
        doc = SimpleDocTemplate(filepath, pagesize=A4, 
                              rightMargin=36, leftMargin=36, 
                              topMargin=36, bottomMargin=18)
        
        # Build report content
        story = []
        
        # Title
        title = f"OST Report - {phase} Phase Summary"
        story.append(Paragraph(title, self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Session Information
        story.extend(self._build_session_info_section(global_metadata))
        
        # Phase Summary
        story.append(Paragraph(f"{phase} Phase Overview", self.styles['SectionHeader']))
        
        # Get phase-specific data
        phase_data = global_metadata.get(f"{phase.lower()}_data", {})
        if phase_data:
            story.extend(self._build_key_value_section(phase_data))
        
        # Tools processed in this phase
        processed_tools = global_metadata.get("processed_tools", [])
        phase_tools = [tool for tool in processed_tools if tool.get("phase", "").lower() == phase.lower()]
        
        if phase_tools:
            story.append(Paragraph(f"Tools Processed in {phase} Phase", self.styles['SubsectionHeader']))
            
            tools_data = [["Tool Name", "Status", "Timestamp"]]
            for tool in phase_tools:
                status = "Success" if tool.get("success", True) else "Failed"
                tools_data.append([
                    tool.get("tool_name", "N/A"),
                    status,
                    tool.get("timestamp", "N/A")
                ])
                
            table = Table(tools_data, colWidths=[2*inch, 1.5*inch, 2*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
            story.append(Spacer(1, 15))
        
        # Include design data for design phase reports
        if phase == "Design":
            design_data = global_metadata.get("design_data", {})
            if design_data:
                story.append(Paragraph("Design Choices", self.styles['SectionHeader']))
                story.extend(self._build_key_value_section(design_data))
        
        # Build PDF
        doc.build(story)
        
        return filepath

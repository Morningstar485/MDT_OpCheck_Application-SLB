from PySide6.QtWidgets import QWidget, QVBoxLayout

class BaseController(QWidget):
    def __init__(self, dialog_list, on_complete_callback=None):
        super().__init__()
        self.dialog_list = dialog_list
        self.on_complete_callback = on_complete_callback
        self.current_index = 0
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        for dialog in self.dialog_list:
            self.layout.addWidget(dialog)
            dialog.hide()
        self.dialog_list[self.current_index].show()
        # Set up navigation if the dialog supports it
        if hasattr(self.dialog_list[self.current_index], 'set_navigation_callbacks'):
            self.dialog_list[self.current_index].set_navigation_callbacks(self.show_next, self.show_back)

    def show_next(self):
        self.dialog_list[self.current_index].hide()
        self.current_index += 1
        if self.current_index >= len(self.dialog_list):
            # Close all dialogs first
            self.close()
            # Then call the completion callback
            if self.on_complete_callback:
                self.on_complete_callback()
        else:
            self.dialog_list[self.current_index].show()
            # Set up navigation if the dialog supports it
            if hasattr(self.dialog_list[self.current_index], 'set_navigation_callbacks'):
                self.dialog_list[self.current_index].set_navigation_callbacks(self.show_next, self.show_back)

    def show_back(self):
        if self.current_index > 0:
            self.dialog_list[self.current_index].hide()
            self.current_index -= 1
            self.dialog_list[self.current_index].show()
            # Set up navigation if the dialog supports it
            if hasattr(self.dialog_list[self.current_index], 'set_navigation_callbacks'):
                self.dialog_list[self.current_index].set_navigation_callbacks(self.show_next, self.show_back)
    
    def close(self):
        """Override close to ensure all dialogs are properly closed"""
        for dialog in self.dialog_list:
            if hasattr(dialog, 'close'):
                dialog.close()
        # Hide and close the controller widget itself
        self.hide()
        super().close()

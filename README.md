All the UI files are present in the repository for convinience of editing in the future.
There might be some changes in the actual application, like after the design phase, there are no longer push buttons in the dialog boxes themselves, but in the outline and a couple more corrections

The application works using controllers, each phase has its own controller, which controls the sequence of the tools, report generation and overall movement of that phase.
Each tool per phase (prepare or perform) has its own controller as well, which gives us the back and forth movementin case of multiple dialog boxes for the same tool in that phase.

The UX is defined in .py files (the naming is self explanatory, the controllers use a *_c.py at the end to differentiate them from normal UX files) which use an algorithmic enable/disable mechanism, which can be easily altered

The file meta data manager has the functions which interprets the user inputs that are passed and generated the reports whenever called.


from pywinauto import backend
from pywinauto.application import Application

app = Application(backend="uia").start("notepad.exe")
app = Application(backend="uia").connect(title="Untitled - Notepad", timeout=1000)

#app.UntitledNotepad.print_control_identifiers()

textEditor = app.UntitledNotepad.child_window(class_name="Edit").wrapper_object()
textEditor.type_keys("This is working!", with_spaces = True)

fileMenu = app.UntitledNotepad.child_window(title="File", control_type="MenuItem").wrapper_object()
fileMenu.click_input()

#app.UntitledNotepad.print_control_identifiers()

#newWindow = app.UntitledNotepad.child_window(title="New Window	Ctrl+Shift+N", auto_id="8", control_type="MenuItem").wrapper_object()
#newWindow.click_input()

close = app.UntitledNotepad.child_window(title="Close", control_type="Button").wrapper_object()
close.click_input()

#app.UntitledNotepad.print_control_identifiers()

dont_save = app.UntitledNotepad.child_window(title="Don't Save", auto_id="CommandButton_7", control_type="Button").wrapper_object()
dont_save.click_input()

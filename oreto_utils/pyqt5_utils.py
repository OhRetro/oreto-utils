#PyQt5

from PyQt5.QtWidgets import QMessageBox

__all__ = ["displaymessage", "settext", "gettext", "getelements"]

Icon = {
    "Question": QMessageBox.Question, 
    "Information": QMessageBox.Information, 
    "Warning": QMessageBox.Warning, 
    "Critical": QMessageBox.Critical,}
    
Button = {
    "Ok": QMessageBox.Ok,
    "No": QMessageBox.No,
    "Yes": QMessageBox.Yes,
    "Cancel": QMessageBox.Cancel,
    "Close": QMessageBox.Close,
    "Abort": QMessageBox.Abort, 
    "Open": QMessageBox.Open, 
    "Ignore": QMessageBox.Ignore, 
    "Save": QMessageBox.Save, 
    "Retry": QMessageBox.Retry, 
    "Apply": QMessageBox.Apply, 
    "Help": QMessageBox.Help, 
    "Reset": QMessageBox.Reset, 
    "SaveAll": QMessageBox.SaveAll, 
    "YesToAll": QMessageBox.YesToAll, 
    "NoToAll": QMessageBox.NoToAll,}
    
#Display Message
def displaymessage(title:str, message:str, informative:str=None, detailed:str=None, icon=None, buttons=None) -> None:
    """
    It displays a message box with the given parameters.\n
    It can only be called inside a running QApplication.
    """
    display = QMessageBox()
    display.setWindowTitle(title)
    display.setText(message)
    if informative is not None: display.setInformativeText(informative)
    if detailed is not None: display.setDetailedText(detailed)
    if icon is not None: display.setIcon(icon)
    if buttons is not None: display.setStandardButtons(buttons)
    return display.exec_()
    
#Set Gui Element Text
def settext(gui, **element) -> None:
    for key, value in element.items():  
        getattr(gui, key).setText(value)
        
#Get Gui Element Text
def gettext(gui, element) -> str:
    return getattr(gui, element).text()

#Get Gui Elements
def getelements(gui) -> list:
    return [element.objectName() for element in gui.children()]
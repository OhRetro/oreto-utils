#PyQt

from PyQt5.QtWidgets import QMessageBox

class PyQt:
    """
    i have no idea of how to make it work with qt6
    """
    def __init__(self):
        self._QMessageBox = QMessageBox

        Icon = {
            "Question": self._QMessageBox.Question, 
            "Information": self._QMessageBox.Information, 
            "Warning": self._QMessageBox.Warning, 
            "Critical": self._QMessageBox.Critical}
            
        Button = {
            "Ok": self._QMessageBox.Ok,
            "No": self._QMessageBox.No,
            "Yes": self._QMessageBox.Yes,
            "Cancel": self._QMessageBox.Cancel,
            "Close": self._QMessageBox.Close,
            "Abort": self._QMessageBox.Abort, 
            "Open": self._QMessageBox.Open, 
            "Ignore": self._QMessageBox.Ignore, 
            "Save": self._QMessageBox.Save, 
            "Retry": self._QMessageBox.Retry, 
            "Apply": self._QMessageBox.Apply, 
            "Help": self._QMessageBox.Help, 
            "Reset": self._QMessageBox.Reset, 
            "SaveAll": self._QMessageBox.SaveAll, 
            "YesToAll": self._QMessageBox.YesToAll, 
            "NoToAll": self._QMessageBox.NoToAll}
        
        self.Icon = Icon
        self.Button = Button
        
    #Display Message
    def displaymessage(self, title:str, message:str, informative:str=None, detailed:str=None, icon=None, buttons=None) -> None:
        """
        It displays a message box with the given parameters.\n
        It can only be called inside a running QApplication.
        """
        display = self._QMessageBox()
        display.setWindowTitle(title)
        display.setText(message)
        if informative is not None: display.setInformativeText(informative)
        if detailed is not None: display.setDetailedText(detailed)
        if icon is not None: display.setIcon(icon)

        if buttons is not None:
            display.setStandardButtons(buttons)
            return display.exec_()
        else:   
            display.exec_()
        
    #Set Gui Element Text
    def settext(self, gui, **element) -> None:
        for _ in element:  
            getattr(gui, _).setText(element[_])
            
    #Get Gui Element Text
    def gettext(self, gui, element) -> str:
        return getattr(gui, element).text()
#PyQt

from PyQt5.QtWidgets import QMessageBox

class PyQt:
    #Icons to be used in display_message() or something similar 
    class Icon:
        Question = QMessageBox.Question
        Information = QMessageBox.Information
        Warning = QMessageBox.Warning
        Critical = QMessageBox.Critical
    
    #Buttons to be used in display_message() or something similar
    class Button:
        Ok = QMessageBox.Ok
        No = QMessageBox.No
        Yes = QMessageBox.Yes
        Cancel = QMessageBox.Cancel
        Close = QMessageBox.Close
        Abort = QMessageBox.Abort
        Open = QMessageBox.Open
        Retry = QMessageBox.Retry
        Ignore = QMessageBox.Ignore
        Save = QMessageBox.Save
        Retry = QMessageBox.Retry
        Apply = QMessageBox.Apply
        Help = QMessageBox.Help
        Reset = QMessageBox.Reset
        SaveAll = QMessageBox.SaveAll
        YesToAll = QMessageBox.YesToAll
        NoToAll = QMessageBox.NoToAll
    
    #Display Message
    def displaymessage(title:str, message:str, informative_message:str=None, detailed_message:str=None, icon=None, buttons=None):
        display = QMessageBox()
        display.setWindowTitle(title)
        display.setText(message)
        if informative_message is not None: display.setInformativeText(informative_message)
        if detailed_message is not None: display.setDetailedText(detailed_message)
        if icon is not None: display.setIcon(icon)

        if buttons is not None:
            display.setStandardButtons(buttons)
            return display.exec_()
        else:   
            display.exec_()
            return
        
    #Set Text
    def settext(gui,**gui_element):
        for _ in gui_element:  
            getattr(gui, _).setText(gui_element[_])
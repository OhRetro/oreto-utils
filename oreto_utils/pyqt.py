#PyQt
#0.1

from PyQt5.QtWidgets import QMessageBox

class PyQt:
    #Display Message
    def display_message(title:str, message:str, buttons=None):
        display = QMessageBox()
        display.setWindowTitle(title)
        display.setText(message)

        if buttons is not None:
            display.setStandardButtons(buttons)
            return display.exec_()
        else:   
            display.exec_()
            return
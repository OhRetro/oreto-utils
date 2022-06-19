#Tkinter

from tkinter import messagebox as tk_messagebox, filedialog as tk_filedialog, Button as tk_Button, Tk as tk_Tk, Label as tk_Label

__all__ = ["messagebox", "filedialog", "GUI"]

message_type = {
    "Info": tk_messagebox.showinfo,
    "Warning": tk_messagebox.showwarning,
    "Error": tk_messagebox.showerror,
    "Question": tk_messagebox.askquestion,
    "YesNo": tk_messagebox.askyesno,
    "OkCancel": tk_messagebox.askokcancel,
    "RetryCancel": tk_messagebox.askretrycancel,
    "YesNoCancel": tk_messagebox.askyesnocancel,}

dialog_type = {
    "File": tk_filedialog.askopenfile,
    "Files": tk_filedialog.askopenfiles,
    "FileName": tk_filedialog.asksaveasfilename,
    "FileNames": tk_filedialog.askopenfilenames,
    "SaveAs": tk_filedialog.asksaveasfile,
    "Directory": tk_filedialog.askdirectory,}

#Messagebox
def messagebox(messagetype:message_type, title:str, message:str, **kwargs) -> tk_messagebox:
    if messagetype not in message_type:
        raise ValueError("Message Type not in valid type list")

    return message_type[messagetype](title=title, message=message, **kwargs)

#Filedialog
def filedialog(dialogtype:dialog_type, title:str, **kwargs) -> tk_filedialog:
    if dialogtype not in dialog_type:
        raise ValueError("Dialog Type not in valid type list")
    
    return dialog_type[dialogtype](title=title, **kwargs)

#Tkinter GUI
class GUI(tk_Tk):
    def __init__(self, title:str, size:tuple=(800, 600), **kwargs):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.kwargs = kwargs
    
    #Label
    def label(self, text:str, **kwargs) -> tk_Label:
        return tk_Label(master=self, text=text, **kwargs)
                
    #Button
    def button(self, text:str, function:callable, **kwargs) -> tk_Button:
        return tk_Button(master=self, text=text, command=function, **kwargs)
#Tkinter

from tkinter import messagebox as tk_messagebox, filedialog as tk_filedialog

__all__ = ["messagebox", "filedialog"]

_Message = {
    "Info": tk_messagebox.showinfo,
    "Warning": tk_messagebox.showwarning,
    "Error": tk_messagebox.showerror,
    "Question": tk_messagebox.askquestion,
    "YesNo": tk_messagebox.askyesno,
    "OkCancel": tk_messagebox.askokcancel,
    "RetryCancel": tk_messagebox.askretrycancel,
    "YesNoCancel": tk_messagebox.askyesnocancel,
    }
_Dialog = {
    "OpenFile": tk_filedialog.askopenfile,
    "OpenFiles": tk_filedialog.askopenfiles,
    "OpenFileName": tk_filedialog.askopenfilename,
    "OpenFileNames": tk_filedialog.askopenfilenames,
    "SaveAsFile": tk_filedialog.asksaveasfile,
    "SaveAsFileName": tk_filedialog.asksaveasfilename,
    "Directory": tk_filedialog.askdirectory,
    }
#Message
def message(type:_Message, title:str, message:str, **kwargs) -> tk_messagebox:
    """It displays a message box with the given parameters.\n"""
    if type not in _Message:
        raise ValueError("Message Type not in valid type list")

    return _Message[type](title=title, message=message, **kwargs)

#Dialog
def dialog(type:_Dialog, title:str, initialdir:str="./", **kwargs) -> tk_filedialog:
    """It displays a file dialog with the given parameters.\n"""
    if type not in _Dialog:
        raise ValueError("Dialog Type not in valid type list")
    
    return _Dialog[type](title=title, initialdir=initialdir,**kwargs)
#Tkinter

from tkinter import messagebox as tk_messagebox, filedialog as tk_filedialog

__all__ = ["messagebox", "filedialog"]

Message = {
    "Info": tk_messagebox.showinfo,
    "Warning": tk_messagebox.showwarning,
    "Error": tk_messagebox.showerror,
    "Question": tk_messagebox.askquestion,
    "YesNo": tk_messagebox.askyesno,
    "OkCancel": tk_messagebox.askokcancel,
    "RetryCancel": tk_messagebox.askretrycancel,
    "YesNoCancel": tk_messagebox.askyesnocancel,}

Dialog = {
    "File": tk_filedialog.askopenfile,
    "Files": tk_filedialog.askopenfiles,
    "FileName": tk_filedialog.asksaveasfilename,
    "FileNames": tk_filedialog.askopenfilenames,
    "SaveAs": tk_filedialog.asksaveasfile,
    "Directory": tk_filedialog.askdirectory,}

#Messagebox
def messagebox(type:Message, title:str, message:str, **kwargs) -> tk_messagebox:
    """It displays a message box with the given parameters.\n"""
    if type not in Message:
        raise ValueError("Message Type not in valid type list")

    return Message[type](title=title, message=message, **kwargs)

#Filedialog
def filedialog(type:Dialog, title:str, **kwargs) -> tk_filedialog:
    """It displays a file dialog with the given parameters.\n"""
    if type not in Dialog:
        raise ValueError("Dialog Type not in valid type list")
    
    return Dialog[type](title=title, **kwargs)
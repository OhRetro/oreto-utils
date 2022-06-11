#Tkinter

from tkinter import messagebox
from tkinter import filedialog

__all__ = ["messagebox"]

messagebox_types = {
    "info": messagebox.showinfo,
    "warning": messagebox.showwarning,
    "error": messagebox.showerror,
    "question": messagebox.askquestion,
    "yes_no": messagebox.askyesno,
    "ok_cancel": messagebox.askokcancel,
    "retry_cancel": messagebox.askretrycancel,
}
filedialog_types = {
    "open": filedialog.askopenfilename,
    "saveas": filedialog.asksaveasfilename,
    "dir": filedialog.askdirectory,
    "color": filedialog.askcolor,
}

#Messagebox
def messagebox(messagetype:str, title:str, message:str, kwargs:dict=None) -> bool:
    return messagebox_types[messagetype](title, message, **kwargs)
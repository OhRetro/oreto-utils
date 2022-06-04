#Tkinter

from tkinter import messagebox
from tkinter import filedialog

class Tkinter:
    def __init__(self):            
        self._messagebox_types = {
            "info": messagebox.showinfo,
            "warning": messagebox.showwarning,
            "error": messagebox.showerror,
            "question": messagebox.askquestion,
            "yes_no": messagebox.askyesno,
            "ok_cancel": messagebox.askokcancel,
            "retry_cancel": messagebox.askretrycancel,
        }
        self._filedialog_types = {
            "open": filedialog.askopenfilename,
            "saveas": filedialog.asksaveasfilename,
            "dir": filedialog.askdirectory,
            "color": filedialog.askcolor,
        }
    
    #Messagebox
    def messagebox(self, messagetype:str, title:str, message:str) -> bool:
        return self._messagebox_types[messagetype](title, message)
import tkinter as tk

class CamFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.label = tk.Label(self)
        self.label.grid(column=0,row=0,sticky='NSWE')

        self.rowconfigure(0,weight=0)
        self.columnconfigure(0,weight=0)

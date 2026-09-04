import tkinter as tk
from .layer2_header import DZPHeader
from .layer2_body import BodyFrame

class ContentFrame(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)

        self.parent = parent

        self.dzpheader = DZPHeader(self, bg="#CBC8C5", borderwidth=5,
                                   relief='groove')
        self.dzpheader.grid(column=0, row=0, sticky='NWES')

        self.bodyframe = BodyFrame(self, bg="#8ECAE6", borderwidth=0,
                                   relief='groove')
        self.bodyframe.grid(column=0, row=1, sticky='NWES')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
import tkinter as tk

class TelemetryFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.label = tk.Label(self,text='TELEMETRY',
                                     font=('Courier New', 12, "bold"),
                                     fg = "#023047",bg="#CBC8C5")
        self.label.grid(column=0,row=0,sticky='NWE')

        self.gnd = tk.Label(self)
        self.gnd.grid(column=0,row=1,sticky='NWE')


        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=0)
        self.columnconfigure(0,weight=1)

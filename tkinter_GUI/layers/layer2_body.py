import tkinter as tk
from .layer3_cam import CamFrame
from .layer3_console import ConsoleFrame
from .layer3_sidebar import SideFrame
from .layer3_telemetry import TelemetryFrame

class BodyFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.console = ConsoleFrame(self,bg="#8ECAE6",
                                    borderwidth=0, relief='ridge')
        self.console.grid(column=0,row=1,columnspan=2,sticky='SWE')


        self.cam = CamFrame(self, bg="#8ECAE6",
                                 borderwidth=5, relief='ridge')
        self.cam.grid(column=0,row=0,sticky='NWES')

        self.telemetry = TelemetryFrame(self, bg="#8ECAE6",
                                        borderwidth=5, relief='ridge')
        self.telemetry.grid(column=2, row=0,rowspan=2, sticky='NWES')

        self.sidebar = SideFrame(self,bg = "#023047",borderwidth=0,relief='ridge')
        self.sidebar.grid(column=1,row=0,sticky='NWES')





        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=0)
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
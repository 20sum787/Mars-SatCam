import tkinter as tk
#from .layer4_setup import SetupFrame
#from .layer4_operation import OperationFrame
#from .layer4_figurecontrols import FigureControlFrame

class SideFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        sidelabel = tk.Label(self,text='CAM CONTROLS',
                                     font=('Courier New', 12, "bold"),
                                     fg = "#023047",bg="#CBC8C5")
        sidelabel.grid(column=0, row=0, sticky='NWE')

        #self.setup = SetupFrame(self,**kwargs)
        #self.setup.grid(column=0,row=1,sticky='NSWE')

        #self.operation = OperationFrame(self,**kwargs)
        #self.operation.grid(column=0,row=3,sticky='NSWE')

        #self.figurecontrol = FigureControlFrame(self,**kwargs)
        #self.figurecontrol.grid(column=0,row=2,sticky='NSWE')

        self.rowconfigure(0, weight=1)
        #self.rowconfigure(1,weight=0)
        #self.rowconfigure(2,weight=0)
        #self.rowconfigure(3,weight=0)

        self.columnconfigure(0, weight=1)
import tkinter as tk
from .layer1 import ContentFrame

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()


        self.geometry("%dx%d" % (width, height))

        self.title("MarsSatCam")
        self.minsize(800,500)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.contents = ContentFrame(self, padx=0, pady=0, bg="#8ECAE6",
                                 borderwidth=5, relief='ridge')
        self.contents.grid(column=0, row=0, sticky='NWES')

    def write_to_console(self,text:str,tag:str='normal'):
        # tag system - "error" red, "confirm" green, "normal" white
        self.contents.bodyframe.console.consolewindow.insert(tk.INSERT,f"{text}\n",tag)
        self.contents.bodyframe.console.consolewindow.see(tk.END)
    '''
    def sat_selection_check(self):
        selections = []
        # should ideally make dictionary/channel mapping!!!
        status1 = self.contents.bodyframe.sidebar.figurecontrol.ch1active.get()
        status2 = self.contents.bodyframe.sidebar.figurecontrol.ch2active.get()
        status3 = self.contents.bodyframe.sidebar.figurecontrol.ch3active.get()
        status4 = self.contents.bodyframe.sidebar.figurecontrol.ch4active.get()

        selections.append(status1)
        selections.append(status2)
        selections.append(status3)
        selections.append(status4)

        return selections
    '''
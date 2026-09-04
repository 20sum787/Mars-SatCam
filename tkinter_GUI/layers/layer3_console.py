import tkinter as tk
import tkinter.scrolledtext as st


class ConsoleFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        consolelabel = tk.Label(self,text='CONSOLE LOG',
                                     font=('Courier New', 12, "bold"),
                                     fg = "#023047",bg="#CBC8C5")
        consolelabel.grid(column=0, row=0,sticky='NWE')

        self.consolewindow = st.ScrolledText(self, width=70,height=6,
                                             font=('Courier New', 12, 'normal'),
                                             bg='black')

        self.consolewindow.tag_config("error",foreground='red')
        self.consolewindow.tag_config("confirm",foreground='limegreen')
        self.consolewindow.tag_config("normal",foreground='white')


        self.consolewindow.grid(column=0, row=1, sticky='NSEW')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1,weight=0)
        self.columnconfigure(0, weight=0)
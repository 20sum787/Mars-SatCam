import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = CURRENT_DIR / "isro_logo.png"  # Change to your exact filename

class DZPHeader(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)

        self.parent = parent

        dzplabel = tk.Label(self,
                                 text="MARS SATCAM",
                                 font=('Courier New', 20, "bold"), fg="#023047",
                                 **kwargs)

        dzplabel.grid(column=1, row=0, sticky='NWES')

        raw_image = Image.open(IMAGE_PATH)
        resized_image = raw_image.resize((120,88), 5)
        self.final_image = ImageTk.PhotoImage(resized_image)

        self.logolabel = tk.Label(self, image=self.final_image) # noqa
        self.logolabel.image = self.final_image
        self.logolabel.grid(column=0, row=0, sticky='NWES')
        # Implement resizing of window here too??
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image
from PIL import ImageTk as itk
import os

class SelectOption(tk.LabelFrame):

    def __init__(self, parent, bw, rlf, posx, posy, txt, img):
        tk.LabelFrame.__init__(self, parent, bd = bw, relief = rlf,
                              font = ("Calibri", 30), text = txt, padx = 8, pady = 4)

        self.parent = parent
        self.place(relx = posx, rely = posy, anchor="center")
        self.txt = txt

        self.img = Image.open(os.path.dirname(__file__) + img)
        self.imgItk = itk.PhotoImage(self.img)
        self.icon = tk.Label(master = self, image = self.imgItk, background = "#F0F0F0")
        self.icon.pack()

        self.icon.bindtags(self.bindtags())

        self.bind('<Enter>', self.hover)
        self.bind('<Leave>', self.leave)

    def hover(self, event):
        self.config(relief = "groove")

    def leave(self, event):
        self.config(relief = "flat")

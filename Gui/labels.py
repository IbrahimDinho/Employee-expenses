import tkinter as tk

class Label(tk.Label):

    def __init__(self, parent, txt, **kwargs):
        tk.Label.__init__(self, parent, text = txt, font=("Calibri 10"), **kwargs)

import tkinter as tk
from tkinter import ttk

class Buttons(tk.ttk.Button):

    def __init__(self, parent, txt, **kwargs):
        tk.ttk.Button.__init__(self, parent, text = txt, **kwargs)
        self.parent = parent
        

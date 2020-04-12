import tkinter as tk
from tkinter import ttk

class EntryBox(tk.ttk.Entry):

    def __init__(self,parent,txt, **kwargs):
        tk.ttk.Entry.__init__(self, parent, font=('Calibri', 20), **kwargs)
        self.parent = parent
        self.txt = txt
        self.insert(0, self.txt)
        
        self.bind('<FocusIn>', self.click)
        self.bind('<FocusOut>', self.notFocus)

    def getValue(self):
        self.item = self.get()
        return self.item

    def click(self, event):
        if self.getValue() == self.txt:
            self.delete(0,"end")
            self.insert(0, "")

    def notFocus(self, event):
        if self.getValue() == "":
            self.insert(0, self.txt)

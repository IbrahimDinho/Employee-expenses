import tkinter as tk
from tkinter import ttk

class EntryDateBox(tk.ttk.Entry):

    def __init__(self,parent, **kwargs):
        tk.ttk.Entry.__init__(self, parent, font=('Calibri', 20), **kwargs)
        self.parent = parent
        self.txt = "DD/MM/YYYY"
        self.insert(0, self.txt)
        
        self.bind('<FocusIn>', self.click)
        self.bind('<FocusOut>', self.notFocus)

        self.bind('<KeyRelease>', self.valiKey)        
        self.bind('<KeyPress>', self.pressKey)

    def getValue(self):
        self.item = self.get()
        return self.item

    def pressKey(self, event):
        
        if len(event.keysym) != 1:
            return

        cursor = self.index("insert")
        
        if cursor == 2:
            self.icursor(3)
        elif cursor == 5:
            self.icursor(6)
            
        self.delete(self.index("insert"))
        
    def valiKey(self, event):

        cursor = self.index("insert")
        index = cursor - 1
        
        entry = self.getValue()
        
        if len(entry) > 10:
            self.delete(10, 'end')

        if len(event.keysym) == 1:
            
            try:
                int(event.char)
            except:
                self.delete(index)
                self.insert(index, self.txt[index])
                self.icursor(index)
            
        if len(event.keysym) != 1:
            if event.keysym == "BackSpace":
                if cursor == 0 and len(self.getValue()) == 10:
                    return
                self.insert(cursor, self.txt[cursor])
                self.icursor(cursor)
            return

    def click(self, event):
        if self.getValue() == self.txt:
            self.icursor(0)
        else:
            pass

    def notFocus(self, event):
        if self.getValue() == "":
            self.insert(0, self.txt)

import tkinter as tk
from tkinter import ttk as ttk
import tkinter.font as tkfont
from config import store

class NoteBook(ttk.Notebook):

    def __init__(self, parent):
        self.parent = parent
        ttk.Notebook.__init__(self, master = self.parent, height = int(store.get("root").winfo_height() * 0.35))

    def loadData(self, data):
        for tab in self.tabs():
            self.forget(tab)
        
        self.form = {}
        self.label = {}
        self.evidence = {}
        
        for claim in data:
            self.form[claim[0]] = tk.Frame(self)
                        
            expType = claim[1]
            self.label[(claim[0], claim[1])] = tk.Label(master = self.form.get(claim[0]),
                     text = "Type: " + expType,
                     font = ("Calibri", 20))
            self.label[(claim[0], claim[1])].pack()
            
            expDate = claim[2]
            self.label[(claim[0], claim[2])] = tk.Label(master = self.form.get(claim[0]),
                     text = "Date: " + expDate,
                     font = ("Calibri", 20))
            self.label[(claim[0], claim[2])].pack()
            
            expCost = claim[3]
            self.label[(claim[0], claim[3])] = tk.Label(master = self.form.get(claim[0]),
                     text = "Cost: £" + str(expCost),
                     font = ("Calibri", 20))
            self.label[(claim[0], claim[3])].pack()
            
            self.evidence[claim[0]] = claim[4]

            claimID = "Claim " + str(claim[0])
            frame = self.form.get(claim[0])
            self.add(frame, text = claimID)

    def returnEvi(self, claimID):
        return self.evidence.get(claimID)
        

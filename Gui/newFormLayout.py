import tkinter as tk
from .frames import Frames
from .labels import Label
from .buttons import Buttons
from .claimLayout import ClaimLayout
from .imageViewer import ImageViewer

from Database import databaseTools as dT
from datetime import date
from Users import login as log

from tkinter import ttk as ttk
import tkinter as tk
from tkinter import messagebox

class NewFormLayout(object):

    def __init__(self, parent):
        self.parent = parent
        self.imageViewer()
        self.submitLayout()
        self.formLayout()

    def imageViewer(self):
        self.view = ImageViewer(self.parent)
        self.view.canvas.pack(side="top", expand = 0.6, fill="both")

    def submitLayout(self):
        self.submitButton = Buttons(self.parent, "Submit", command = self.submission)
        self.submitButton.pack(side = "bottom", anchor = "se", padx = 25, pady = 10)
    
    def formLayout(self):
        self.claims = ClaimLayout(self.parent, self.view)

    def submission(self):
        if tk.messagebox.askquestion("Submit", "Submit Form?") == "yes":

            from .selectionLayout import SelectionLayout
        
            data = self.claims.getRequests()

            today = date.today()
            submitDate = today.strftime("%d/%m/%Y")
            login = log.Login(None, None, None)
            email = login.workEmail
            repM = login.user.reportingManager

            dT.insertExpenseForm([submitDate, email, repM])
            formID = dT.getLastForm(email)
            
            claimID = 1
            
            for claim in data:
                dT.insertExpenseClaim([formID, claimID, claim[1], claim[0], claim[2], claim[3]])
                claimID += 1
            
            for i in self.parent.winfo_children():
                i.destroy()

            SelectionLayout(self.parent, login.user) 
        
        

        

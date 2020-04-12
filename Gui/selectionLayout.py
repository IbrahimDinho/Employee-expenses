import tkinter as tk
from .entryBox import EntryBox
from .frames import Frames
from .labels import Label
from .buttons import Buttons

from .selectOption import SelectOption
from .newFormLayout import NewFormLayout
from .expenseHistory import ExpenseHistoryLayout
from .viewPendingExpense import ReviewExpenseLayout

from tkinter import ttk as ttk
from tkinter import messagebox

from Users import login as log
from Users import expenseReviewer as ex
from Users import manager as m
from Users import admin as ad

from PIL import Image
from PIL import ImageTk as itk
import os

class SelectionLayout(object):

    def __init__(self, parent, role):
        self.parent = parent
        self.parent.unbind('<+>')
        self.role = role
        self.layoutOptions(parent)
        
    def layoutOptions(self, parent):

        self.widgetList = []
        self.loginInfo()
        
        self.newForm = SelectOption(parent, 6, "flat", 0.25, 0.25,
                               "Create New Form", "\\newForm.png")
        self.newForm.bind('<Button-1>', self.createNewForm)

        self.expenseHistory = SelectOption(parent, 6, "flat", 0.5, 0.25,
                                "View Submissions", "\\expenseHistory.png")
        self.expenseHistory.bind('<Button-1>', self.viewExpenseHistory)

        self.widgetList.append(self.newForm)
        self.widgetList.append(self.expenseHistory)

        if isinstance(self.role, (ex.ExpenseReviewer, m.Manager)):
            self.pendingList = SelectOption(parent, 6, "flat", 0.75, 0.25,
                                "Review Expenses", "\\pending.png")
            self.pendingList.bind('<Button-1>', self.viewPending)

            self.widgetList.append(self.pendingList)
            
        elif isinstance(self.role, ad.Admin):
            self.newAccount = SelectOption(parent, 6, "flat", 0.75, 0.25,
                                "Create Account", "\\pending.png")
            self.newAccount.bind('<Button-1>', self.createNewAccount)
            self.widgetList.append(self.newAccount)

    def loginInfo(self):
        self.topFrame = Frames(self.parent, 0, "flat")
        self.topFrame.pack(side = "top", fill = "x")

        self.logoutButton = tk.Button(master = self.topFrame, text = "Logout", command = log.Login.logout)
        self.logoutButton.pack(side = "right", anchor = "ne")
        self.loginLabel = tk.Label(master = self.topFrame, text = "Logged in as " + log.Login.workEmail)
        self.loginLabel.pack(side = "right", anchor = "ne")

        backImg = Image.open(os.path.dirname(__file__) + "\\back.png")
        imgItk = itk.PhotoImage(backImg)
        
        self.menuButton = tk.Button(master = self.topFrame, command = self.newSelectionLayout, image = imgItk, relief = "flat", width = 32, height = 32)
        self.menuButton.image = imgItk
        self.menuButton.pack(side = "left", anchor = "nw", padx = 5)

    def createNewForm(self, event):
        self.prepNewLayout()
        NewFormLayout(self.parent)

    def viewExpenseHistory(self, event):
        self.prepNewLayout()
        ExpenseHistoryLayout(self.parent)

    def viewPending(self, event):
        self.prepNewLayout()
        self.pendingList.destroy()
        ReviewExpenseLayout(self.parent)

    def createNewAccount(self, event):
        self.prepNewLayout()
        self.newAccount.destroy()

    def prepNewLayout(self):
        for widgets in self.widgetList:
            widgets.destroy()

    def newSelectionLayout(self):
        if tk.messagebox.askquestion("Menu", "Return to menu?", icon = "warning") == "yes":
        
            for i in self.parent.winfo_children():
                i.destroy()

            SelectionLayout(self.parent, self.role)
        

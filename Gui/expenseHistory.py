import tkinter as tk

from .entryBox import EntryBox
from .frames import Frames
from .labels import Label
from .buttons import Buttons
from .table import Table
from .imageViewer import ImageViewer
from .notebook import NoteBook

from Users import login as log

class ExpenseHistoryLayout(object):

    def __init__(self, parent):
        self.parent = parent
        self.revString = tk.StringVar()
        self.revString.set("Placeholder Comment")
        self.manString = tk.StringVar()
        self.manString.set("Placeholder Comment")

        self.expenseFormTable()
        self.evidenceViewer()
        self.expenseClaimViewer()

    def evidenceViewer(self):

        self.rightFrame = Frames(self.parent, 1, "groove")
        self.rightFrame.pack(side = "left", expand = 1, fill = "both")
        
        self.evidenceView = ImageViewer(self.rightFrame)
        self.evidenceView.canvas.pack(side = "top", expand = True, fill = "both")

    def expenseFormTable(self):
        self.formFrame = Frames(self.parent, 1, "groove")
        self.formFrame.pack(side = "left", fill = "y")

        login = log.Login(None, None, None)
        self.user = login.user

        self.expenseForms = self.user.viewExpenseHistory()
        expenses = []
        
        underReview = "Under Review"
        accepted = "Accepted"
        rejected = "Rejected"
        
        for expense in self.expenseForms:
            tempExp = []
            tempExp.append(expense[0])
            tempExp.append(expense[1])

            if expense[2] == 1:
                if expense[5] == 1:
                    tempExp.append(accepted)
                else:
                    tempExp.append(rejected)
            elif expense[3] == 1 and expense[4] == 0:
                tempExp.append(rejected)
            else:
                tempExp.append(underReview)

            expenses.append(tempExp)
            
        columns = ["FormID", "Date Submitted", "Status"]

        self.table = Table(self.formFrame, columns, tuple(i for i in expenses))
        self.table.tree.bind('<<TreeviewSelect>>', self.selectedForm, add = "+")
        
    def selectedForm(self, event):
        item = self.table.tree.selection()[0]
        formID = self.table.tree.item(item)["values"][0]
        claimData = self.user.viewExpense(formID)
        self.claimView.loadData(claimData)
        self.loadComments(formID)

    def loadComments(self, formID):
        for expense in self.expenseForms:
            if str(expense[0]) == str(formID):
                self.revString.set("Reviewer's Comment:\n" + str(expense[7]))
                self.manString.set("Manager's Comment:\n" + str(expense[6]))

    def expenseClaimViewer(self):
        self.bottomFrame = Frames(self.rightFrame, 0 , "groove")
        self.bottomFrame.pack(side = "bottom", expand = True, fill = "both")
        self.bottomFrame.pack_propagate(False)
        
        self.claimView = NoteBook(self.bottomFrame)
        self.claimView.pack(side = "left", expand = True, fill = "both")

        self.claimView.bind('<<NotebookTabChanged>>', self.selectedTab, add = "+")

        self.revComment = tk.Message(master = self.bottomFrame, textvariable = self.revString,
                                     font = ('Calibri', 15), anchor = "nw")

        self.revComment.bind("<Configure>", 
    lambda event: event.widget.configure(width=event.width-8))

        self.manComment = tk.Message(master = self.bottomFrame, textvariable = self.manString,
                                     font = ('Calibri', 15), anchor = "nw")
        self.manComment.pack(side = "right", expand = True, fill = "both")
        self.revComment.pack(side = "right", expand = True, fill = "both")
        
        self.manComment.bind("<Configure>", 
    lambda event: event.widget.configure(width=event.width-8))

    def selectedTab(self, event):
        filepath = self.claimView.returnEvi(self.claimView.index("current") + 1)
        self.evidenceView.imageLoad(filepath)
        

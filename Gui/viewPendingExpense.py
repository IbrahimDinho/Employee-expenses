import tkinter as tk

from .entryBox import EntryBox
from .frames import Frames
from .labels import Label
from .buttons import Buttons
from .table import Table
from .imageViewer import ImageViewer
from .notebook import NoteBook

from Users import login as log

class ReviewExpenseLayout(object):
    def __init__(self, parent):
        self.parent = parent

        self.expenseFormTable()
        self.evidenceViewer()
        self.expenseClaimViewer()

    def evidenceViewer(self):

        self.rightFrame = Frames(self.parent, 1, "groove")
        self.rightFrame.pack(side = "left", expand = True, fill = "both")
        
        self.evidenceView = ImageViewer(self.rightFrame)
        self.evidenceView.canvas.pack(side = "top", expand = True, fill = "both")

    def expenseFormTable(self):
        self.formFrame = Frames(self.parent, 1, "groove")
        self.formFrame.pack(side = "left", fill = "y")

        login = log.Login(None, None, None)
        self.user = login.user

        self.expenseForms = self.user.viewPendingExpenseList()
        expenses = []
        
        for expense in self.expenseForms:
            tempExp = []
            tempExp.append(expense[0])
            tempExp.append(expense[1])
            tempExp.append(expense[2])

            expenses.append(tempExp)
            
        columns = ["FormID", "Date Submitted", "Requester"]

        self.table = Table(self.formFrame, columns, tuple(i for i in expenses))
        self.table.tree.bind('<<TreeviewSelect>>', self.selectedForm, add = "+")
        
    def selectedForm(self, event):
        item = self.table.tree.selection()[0]
        self.formID = self.table.tree.item(item)["values"][0]
        requester = self.table.tree.item(item)["values"][2]
        claimData = self.user.viewPendingExpense(requester, self.formID)
        self.claimView.loadData(claimData)

    def expenseClaimViewer(self):
        self.bottomFrame = Frames(self.rightFrame, 0 , "groove")
        self.bottomFrame.pack(side = "bottom", expand = True, fill = "both")
        self.bottomFrame.pack_propagate(False)
        
        self.claimView = NoteBook(self.bottomFrame)
        self.claimView.pack(side = "left", expand = True, fill = "both")

        self.claimView.bind('<<NotebookTabChanged>>', self.selectedTab, add = "+")
        self.claimView.update()
        self.commentFrame = Frames(self.bottomFrame, 0, "flat", width = (self.claimView.winfo_width() *0.33), height = self.claimView.winfo_height())
        self.commentFrame.pack(side = "right", fill = "x")
        self.commentFrame.pack_propagate(False)

        self.commentFrame.update()
        self.commentLabel = tk.Label(master = self.commentFrame, font = ("Calibri", 20), text = "Reviewing Notes:")
        self.commentLabel.pack(side = "top", anchor = "nw")
        
        self.commentBoxFrame = Frames(self.commentFrame, 0, "flat",
                                height = int(self.commentFrame.winfo_height() * 0.6),
                                width = int(self.commentFrame.winfo_width() * 0.8))
        self.commentBoxFrame.pack(side = "top", anchor = "n", pady = 10)
        self.commentBoxFrame.pack_propagate(False)
        
        self.commentBox = tk.Text(master = self.commentBoxFrame, font = ("Calibri", 15))
        self.commentBox.pack(side = "top")

        self.buttonFrame = Frames(self.commentFrame, 0, "flat")
        self.buttonFrame.pack(side = "bottom", fill = "x")

        self.acceptButton = Buttons(self.buttonFrame, "Accept", command = self.accept)
        self.denyButton = Buttons(self.buttonFrame, "Deny", command = self.deny, state = "disabled")

        self.commentBox.bind('<KeyRelease>', self.checkNote)

        self.acceptButton.pack(side = "right", padx = 10, pady = 25)
        self.denyButton.pack(side = "right", padx = 10, pady = 25)

    def checkNote(self, event):
        if self.commentBox.get('1.0', 'end-1c') != "":
            self.denyButton.configure(state = "active")
        else:
            self.denyButton.configure(state = "disabled")

    def accept(self):
        if tk.messagebox.askquestion("Accept?", "Accept Selected Form?") == "yes":
            self.user.acceptExpense(int(self.formID), self.commentBox.get('1.0', 'end-1c'))
            self.removeReviewed()
            
    def deny(self):
        if tk.messagebox.askquestion("Deny?", "Deny Selected Form?") == "yes":
            self.user.denyExpense(int(self.formID), self.commentBox.get('1.0', 'end-1c'))
            self.removeReviewed()

    def removeReviewed(self):
        for form in self.table.tree.get_children():
            if self.formID == self.table.tree.item(form)["values"][0]:
                self.table.tree.delete(form)
                
                child = self.table.tree.get_children()[-1]
                self.table.tree.focus(child)
                self.table.tree.selection_set(child)

                self.commentBox.delete('1.0', 'end')
            
    def selectedTab(self, event):
        filepath = self.claimView.returnEvi(self.claimView.index("current") + 1)
        self.evidenceView.imageLoad(filepath)

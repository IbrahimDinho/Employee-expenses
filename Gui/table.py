import tkinter as tk
from tkinter import ttk as ttk
import tkinter.font as tkfont

class Table(object):

    def __init__(self, parent, columns, rowData):
        self.parent = parent
        self.columns = columns
        self.rowData = rowData

        self.tree = None
        self.treeCreation()

    def treeCreation(self):
        self.container = self.parent.frame
        self.container.pack(fill = "y", side = "left", anchor = "nw")
        self.tree = ttk.Treeview(columns = self.columns, show = "headings")

        scrolly = ttk.Scrollbar(orient = "vertical", command = self.tree.yview)

        self.tree.configure(yscrollcommand = scrolly.set)
        self.tree.grid(column = 0, row = 0, sticky = "nsew", in_=self.container)
        scrolly.grid(column = 1,row = 0, sticky = "ns", in_=self.container)
        self.container.grid_columnconfigure(0, weight = 1)
        self.container.grid_rowconfigure(0, weight = 1)

        for columns in self.columns:
            self.tree.heading(columns, text = columns.title())
            self.tree.column(columns, width = tkfont.Font().measure(columns.title()))

        for rows in self.rowData:
            self.tree.insert("", 'end', values = rows)
            for col, value in enumerate(rows):
                colWidth = tkfont.Font().measure(value)
                if self.tree.column(self.columns[col], width = None) < colWidth:
                    self.tree.column(self.columns[col], width = colWidth)
            

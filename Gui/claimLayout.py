import tkinter as tk
from .frames import Frames
from .labels import Label
from .buttons import Buttons
from .entryBox import EntryBox
from .entryDateBox import EntryDateBox
from tkinter import ttk as ttk
from tkinter import filedialog as fileDial
from tkinter import messagebox
import tkinter.font as tkfont
from PIL import Image
from PIL import ImageTk as itk
import os
import fitz

class ClaimLayout(object):

    def __init__(self, parent, view):
        self.parent = parent

        self.frameContainer = tk.Frame(self.parent)
        self.frameContainer.pack(side = "bottom", expand = 1, fill = "both", ipadx="20")

        self.formTable()
        self.entryLayout()
        self.view = view

    def formTable(self):

        style = ttk.Style()
        style.configure("largerFont.Treeview", font = ("Calibri", 15), rowheight = 30)
        style.configure("largerFont.Treeview.Heading", font = ("Calibri", 25))
        
        
        table = ["Date", "Type", "Cost", "Evidence Attached"]

        self.treeContainer = tk.Frame(self.parent)
        self.tree = None
        self.container = self.treeContainer
        self.container.pack(fill="both", expand = True, side = "top")
        self.tree = ttk.Treeview(columns = table, show = "headings", style="largerFont.Treeview")

        scrolly = ttk.Scrollbar(orient = "vertical", command = self.tree.yview)
        scrollx = ttk.Scrollbar(orient = "horizontal", command = self.tree.xview)

        self.tree.configure(yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        self.tree.grid(column = 0, row = 0, sticky = "nsew", in_=self.container)
        scrolly.grid(column = 1,row = 0, sticky = "ns", in_=self.container)
        scrollx.grid(column = 0, row = 1, sticky = "ew", in_=self.container)
        self.container.grid_columnconfigure(0, weight = 1)
        self.container.grid_rowconfigure(0, weight = 1)

        for columns in table:
            self.tree.heading(columns, text = columns.title())
            self.tree.column(columns, width = tkfont.Font().measure(columns.title()))

        self.parent.bind('<+>', self.insertBlankRowEvent)
        
        self.insertBlankRow()

    def insertBlankRowEvent(self, event):
        self.insertBlankRow()

    def insertBlankRow(self):
        self.tree.insert('', 'end', values = ["None Set","None Set","None Set","None Set"])
        child = self.tree.get_children()[-1]
        self.tree.focus(child)
        self.tree.selection_set(child)

    def deleteRow(self):
        if tk.messagebox.askquestion("Delete Rows", "Remove Selected Rows from Form?") == "yes":
                
            selected = self.tree.selection()
            for i in selected:
                self.tree.delete(i)
            child = self.tree.get_children()[-1]
            self.tree.focus(child)
            self.tree.selection_set(child)
        
    def entryLayout(self):
        self.instructions = Label(self.frameContainer, "Select Row to Edit; + to add new row")
        self.instructions.pack(side= "top", anchor = "n")
        
        self.date = EntryDateBox(self.frameContainer)
        self.date.pack(side="left", anchor = "center", padx = 25)
        self.date.bind('<KeyRelease>', self.entryDateMimic, add = "+")

        self.types = tk.Frame(self.frameContainer, padx = "20", pady = "5")
        self.types.pack(side = "left", anchor = "center")
        self.type = {}

        self.transport = Buttons(self.types, "Transport", command = lambda: self.selectType("transport"))
        self.lodging = Buttons(self.types, "Lodging", command = lambda: self.selectType("lodging"))
        self.food = Buttons(self.types, "Food", command = lambda: self.selectType("food"))
        self.other = Buttons(self.types, "Other", command = lambda: self.selectType("other"))

        self.type["transport"] = self.transport
        self.type["lodging"] = self.lodging
        self.type["food"] = self.food
        self.type["other"] = self.other

        self.transport.pack(side = "left")
        self.lodging.pack(side="left")
        self.food.pack(side="left")
        self.other.pack(side="left")

        self.cost = EntryBox(self.frameContainer, "Cost", width = "6")
        self.cost.bind('<KeyRelease>', self.entryMimic)
        self.cost.pack(side = "left", anchor = "center", padx = 25)

        self.evidenceButton = Buttons(self.frameContainer, "Attach", command = self.attach)
        self.evidenceLabel = Label(self.frameContainer, "Evidence not Attached")

        self.evidenceButton.pack(side="left")
        self.evidenceLabel.pack(side ="left")

        img = Image.open(os.path.dirname(__file__) + "\\plus.png")
        imgItk = itk.PhotoImage(img)
        
        self.addButton = tk.Button(master = self.frameContainer, image = imgItk, command = self.insertBlankRow,
                                   width = 32, height = 32)
        self.addButton.image = imgItk
        self.addButton.pack(side = "left", anchor = "center", padx = 50)

        img2 = Image.open(os.path.dirname(__file__) + "\\minus.png")
        imgDel = itk.PhotoImage(img2)

        self.deleteButton = tk.Button(master = self.frameContainer, image = imgDel,
                                      command = self.deleteRow, width = 32, height = 32)
        self.deleteButton.image = imgDel
        self.deleteButton.pack(side = "right", anchor = "e", padx = 50)
        
    def selectType(self, typeSelected):
        # Change button states to show what user selected.
        for i in self.type:
            self.type.get(i).state(["!disabled"])
        self.type[typeSelected].state(["disabled"])

        self.updateTable(1, typeSelected)

    def entryDateMimic(self, event):
        data = event.widget.getValue()
        self.updateTable(0, data)

    def entryMimic(self, event):
        data = event.widget.getValue()
        self.updateTable(2, data)

    def attach(self):
        filename = ""
        filename = fileDial.askopenfilename()
        self.updateTable(3, filename)
        self.view.imageLoad(filename)

    def updateTable(self, index, update):

        # Get and change the selection to what the user specified.
        data = self.tree.item(self.tree.focus()).get("values")
        data[index] = update

        # Update the table with the changed info.
        self.tree.item(self.tree.focus(), values = data)
        self.tree.update_idletasks()

    def getRequests(self):
        data = []
        for child in self.tree.get_children():
            data.append(self.tree.item(child)["values"])
            
        return data
    

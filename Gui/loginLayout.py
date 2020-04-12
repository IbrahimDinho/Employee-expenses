import tkinter as tk
from .entryBox import EntryBox
from .frames import Frames
from .labels import Label
from .buttons import Buttons
from .selectionLayout import SelectionLayout
from tkinter import ttk as ttk
from Database import databaseTools
from Users import login as log
from Users import employee as em
from Users import expenseReviewer as ex
from Users import manager as m
from Users import admin as ad



class LoginLayout(tk.LabelFrame):
    
    def __init__(self, parent, bw, rlf):
        tk.LabelFrame.__init__(self, parent, bd = bw, relief = rlf,
                               text = "Login", font = ("Calibri", 30),
                               padx = 8, pady = 4)
        self.parent = parent
        self.place(relx = 0.50, rely = 0.30, anchor="center")
        
        self.layout()
        
    #Login Layout
    def layout(self):
        self.userEmail = EntryBox(self, "Email") # Username Input
        self.userEmail.pack()
        self.userPass = EntryBox(self, "Password") # Password Input
        self.userPass.pack(pady = 10)
        
        s = ttk.Style()

        # Login button placement and styling
        s.configure('loginButton.TButton', font=("Calibri", 15))
        self.loginButton = Buttons(self, "Login", style='loginButton.TButton', command = self.validateLogin)
        self.loginButton.pack(side = "right")

        # Incorrect details message.
        self.errorLabel = Label(self, "Email or Password is incorrect.", foreground = "#F0F0F0")

        # Forgotten password option.
        self.resetButton = tk.Button(self, text="Forgot Password?", relief="flat", foreground="blue")

        # Layout of above message and option.
        self.resetButton.pack(side = "bottom")
        self.errorLabel.pack(side = "bottom")

    #Login button functionality
    def validateLogin(self):
        email = self.userEmail.getValue() # Pulls user email input
        password = self.userPass.getValue() # Pulls user password input
        loginData = loginQuery(email, password) # Stores output of sql query
        
        if loginData != []: # If loginData is empty, login does not exist
            print(loginData)
            user = None
            accessLevel = loginData[0][0]
            repManager = loginData[0][1]
            
            # Checks user's access level and appropriate UI.
            if accessLevel == "Employee":
                user = em.Employee(email, repManager)
                login = log.Login(email, loginData[0][0], user) # Creates login session.
                self.destroy()
                SelectionLayout(self.parent, user)
                
            elif accessLevel == "ExpenseReviewer":
                user = ex.ExpenseReviewer(email, repManager)
                login = log.Login(email, loginData[0][0], user) # Creates login session.
                self.destroy()
                SelectionLayout(self.parent, user)
                
            elif accessLevel == "Manager":
                user = m.Manager(email, repManager)
                login = log.Login(email, loginData[0][0], user) # Creates login session.
                self.destroy()
                SelectionLayout(self.parent, user)
                
            elif accessLevel == "Admin":
                user = a.Admin(email, repManager)
                login = log.Login(email, loginData[0][0], user) # Creates login session.
                self.destroy()
                SelectionLayout(self.parent, user)
                
            else:
                pass
                # Access Denied Label to be placed.
                
        else:
            self.errorLabel.config(foreground="red")
            self.errorLabel.config(text = "Email or Password is incorrect.")
        
def loginQuery(email, password):
    cursor = databaseTools.conncursor(".\Database\login.db") # Creates database connection.
    
    # Insert SQL query to get login data of user.
    sql = 'SELECT accessLevel, reportingManager FROM employees WHERE email = ? AND password = ?'
    
    cursor.execute(sql,(email, password))
    loginData = cursor.fetchall() # Fetches data using the sql executed above.
    return loginData


from expensesApp import logoutClear
import tkinter as tk
from tkinter import messagebox

class Login(object):

    __instance = None
    def __new__(cls, workEmail, accessLevel, user):
        if cls.__instance is None:
            cls.__instance = super(Login, cls).__new__(cls)
            cls.workEmail = workEmail
            cls.accessLevel = accessLevel
            cls.user = user
        return cls.__instance

    def logout():
        if tk.messagebox.askquestion("Logout", "Logout?") == "yes":
            Login.__instance = None
            logoutClear()

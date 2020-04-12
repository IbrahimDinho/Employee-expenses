import sqlite3
from sqlite3 import Error
import os.path

def connection(database):
    try:
        conn = sqlite3.connect(database, isolation_level = None)
        return conn
    except Error as e:
        print(e)
        return conn

def conncursor(database):
    db = connection(database)
    cursor = db.cursor()
    return cursor

def insertLogin(inp):
    db_login = ".\Database\login.db"
    cursor = conncursor(db_login)
    sql = '''INSERT INTO employees(email,password,accessLevel,reportingManager) Values(?,?,?,?);'''
    cursor.execute(sql, inp)
    cursor.close()

def insertExpenseForm(inp):
    db_expense = ".\Database\expenses.db"
    db = connection(db_expense)
    cursor = conncursor(db_expense)
    sql = '''INSERT INTO expenseForm(dateSubmitted,requester,reportingManager,isReviewed,reviewAcceptance,isGivenApproval,approvalAcceptance)
Values(?,?,?,0,0,0,0);'''
    cursor.execute(sql, inp)
    cursor.close()

def insertExpenseClaim(inp):
    db_expense = ".\Database\expenses.db"
    db = connection(db_expense)
    cursor = conncursor(db_expense)
    sql = '''INSERT INTO expenseClaim(formID,claimID,expenseType,expenseDate,expenseCost,evidence) 
Values(?,?,?,?,?,?);'''
    cursor.execute(sql, inp)
    cursor.close()

def getLastForm(email):
    db_expense = ".\Database\expenses.db"
    cursor = conncursor(db_expense)
    sql = '''SELECT formID FROM expenseForm WHERE requester = ? ORDER BY formID DESC LIMIT 1'''

    cursor.execute(sql, [email])
    formID = cursor.fetchall()
    
    cursor.close()
    return formID[0][0]

    

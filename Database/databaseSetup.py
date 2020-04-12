import sqlite3
from sqlite3 import Error

def connection(database):
    try:
        conn = sqlite3.connect(database, isolation_level = None)
        return conn
    except Error as e:
        print(e)
        return conn

def conncursor(database):
    db = connection(database)
    db.execute("PRAGMA foreign_keys = 1")
    cursor = db.cursor()
    return cursor

def loginTableCreation(database):
    cursor = conncursor(database)
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(email TEXT NOT NULL PRIMARY KEY, password TEXT, accessLevel TEXT, reportingManager TEXT);''')
    cursor.close()

def insertLogin(inp):
    db_login = "login.db"
    cursor = conncursor(db_login)
    sql = '''INSERT INTO employees(email,password,accessLevel,reportingManager) Values(?,?,?,?);'''
    cursor.execute(sql, inp)
    cursor.close()

def expensesTableCreation(database):
    cursor = conncursor(database)
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenseForm
(formID INTEGER PRIMARY KEY,
dateSubmitted TEXT,
reviewComment TEXT,
managerComment TEXT,
requester TEXT,
reportingManager TEXT,
isReviewed INTEGER,
reviewAcceptance INTEGER,
isGivenApproval INTEGER,
approvalAcceptance INTEGER);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS expenseClaim
(formID INTEGER,
claimID INTEGER,
expenseType TEXT,
expenseDate TEXT,
expenseCost REAL,
evidence TEXT,
FOREIGN KEY (formID) REFERENCES EXPENSEFORM (formID),
PRIMARY KEY (formID, claimID));''')
    cursor.close()

def insertExpenseForm(inp):
    db_expense = "expenses.db"
    db = connection(db_expense)
    cursor = conncursor(db_expense)
    sql = '''INSERT INTO expenseForm(dateSubmitted,requester,reportingManager,isReviewed,reviewAcceptance,isGivenApproval,approvalAcceptance)
Values(?,?,?,?,?,?,?);'''
    cursor.execute(sql, inp)
    cursor.close()

def insertExpenseClaim(inp):
    db_expense = "expenses.db"
    db = connection(db_expense)
    cursor = conncursor(db_expense)
    sql = '''INSERT INTO expenseClaim(formID,claimID,expenseType,expenseDate,expenseCost,evidence) 
Values(?,?,?,?,?,?);'''
    cursor.execute(sql, inp)
    cursor.close()

#loginTableCreation("login.db")
#expensesTableCreation("expenses.db")
#insertLogin(["test@fdmgroup.com","password","Employee","testManager@fdmgroup.com"])
#insertLogin(["testManager@fdmgroup.com","password","Manager","test@fdmgroup.com"])
insertLogin(["testReviewer@fdmgroup.com","password","ExpenseReviewer","testManager@fdmgroup.com"])

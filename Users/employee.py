from Users.DAO import employeeDAOImp as dao

class Employee():

    def __init__(self, workMail, repManager):
        self.workEmail = workMail
        self.reportingManager = repManager

    def viewExpenseHistory(self):
        data = dao.EmployeeDAOImp.getExpenseHistory(self.workEmail)
        return data

    def viewExpense(self, expForm):
        data = dao.EmployeeDAOImp.getExpenseClaim(self.workEmail, expForm)
        return data

    def createNewExpenseForm():
        return

    def saveDraftExpenseForm():
        return False

    def loadDraftExpenseForm():
        return False

    def submitExpenseForm():
        return False

    def addNewExpenseClaim():
        return

    def printExpense():
        return

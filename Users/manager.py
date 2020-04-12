from Users import employee as e
from Users.DAO import expenseDAOImpManager as dao
from Users.DAO import employeeDAOImp as edao

class Manager(e.Employee):

    def __init__(self, workMail, repManager):
        super().__init__(workMail, repManager)

    def viewPendingExpenseList(self):
        data = dao.ExpenseDAOImpManager.getPendingExpenseList(self.workEmail)
        return data

    def viewPendingExpense(self, requester, expForm):
        data = edao.EmployeeDAOImp.getExpenseClaim(requester, expForm)
        return data

    def acceptExpense(self, formID, comment):
        dao.ExpenseDAOImpManager.updateExpense(formID, True, comment)
        return

    def denyExpense(self, formID, comment):
        dao.ExpenseDAOImpManager.updateExpense(formID, False, comment)
        return

    def viewAllSupervisedExpenses():
        return False

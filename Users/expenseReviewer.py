from Users import employee as e
from Users.DAO import expenseDAOImpExpenseReviewer as dao
from Users.DAO import employeeDAOImp as edao

class ExpenseReviewer(e.Employee):

    def __init__(self, workMail, repManager):
        super().__init__(workMail, repManager)

    def viewPendingExpenseList(self):
        data = dao.ExpenseDAOImpExpenseReviewer.getPendingExpenseList(self.workEmail)
        return data

    def viewPendingExpense(self, requester, expForm):
        data = edao.EmployeeDAOImp.getExpenseClaim(requester, expForm)
        return data

    def acceptExpense(self, formID, comment):
        dao.ExpenseDAOImpExpenseReviewer.updateExpense(formID, True, comment)
        return
    
    def denyExpense(self, formID, comment):
        dao.ExpenseDAOImpExpenseReviewer.updateExpense(formID, False, comment)
        return

    def viewAllReviewedExpenses():
        return False

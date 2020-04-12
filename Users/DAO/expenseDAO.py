import abc

class ExpenseDAO(abc.ABC):
    @abc.abstractmethod
    def getPendingExpenseList(emailID):
        pass
    
    @abc.abstractmethod
    def updateExpense(formID, expenseAcceptance, comment):
        pass

    @abc.abstractmethod
    def getAllAllowedExpense(emailID):
        pass

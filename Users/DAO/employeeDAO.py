import abc

class EmployeeDAO(abc.ABC):
    
    @abc.abstractmethod
    def getExpenseHistory(emailID):
        pass
    
    @abc.abstractmethod
    def getExpenseClaim(emailID):
        pass
    

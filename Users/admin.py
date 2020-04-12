from Users import employee as e

class Admin(e.Employee):

    def __init__(self, workMail, repManager):
        super().__init__(workMail, repManager)
        
    def createNewAccount(email, password, accessLevel):
        return False

    def revokeAccountAccess(email):
        return False

    def updateLimits(email):
        return False

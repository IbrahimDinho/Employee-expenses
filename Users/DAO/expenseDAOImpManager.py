from Users.DAO import expenseDAO as exD # the interface we're extending
from Database import databaseTools as data

class ExpenseDAOImpManager(exD.ExpenseDAO):

    #Managers see expenseForms where reviewAcceptance is True and isGivenApproval is False
    def getPendingExpenseList(emailID):

        # cursor creates the link to the database
        cursor = data.conncursor(".\Database\expenses.db")

        # sql is the query you will run
        sql = '''SELECT formID, dateSubmitted, requester FROM expenseForm
WHERE reviewAcceptance = 1 AND reportingManager = ? AND isGivenApproval = 0'''

        # cursor.execute executes the query. Pass through the query,
        # then the values which replace the ? in the query.
        cursor.execute(sql, [emailID])

        # Run cursor.fetchall to get the query results
        expenseForms = cursor.fetchall()

        # Close the database connection after finishing
        cursor.close()

        # return the results
        return expenseForms

    #Update isGivenApproval to True and approvalAcceptance + comment
    def updateExpense(formID, expenseAcceptance, comment):
        
        cursor = data.conncursor(".\Database\expenses.db")
        
        sql = '''UPDATE expenseForm SET isGivenApproval = 1,
approvalAcceptance = ?, managerComment = ? WHERE formID = ?'''
        
        cursor.execute(sql, [expenseAcceptance, comment, formID])

        # Commit any changes from update / insert / deletion queries
        cursor.connection.commit()
        
        cursor.close()

    #Get all expenses where they are are reportingManager
    def getAllAllowedExpense(emailID):
        cursor = data.conncursor(".\Database\expenses.db")

        sql = '''SELECT formID, requester, dateSubmitted FROM expenseForm
WHERE reportingManager = ?'''

        cursor.execute(sql, [emailID])

        expenseForms = cursor.fetchall()

        cursor.close()
        return expenseForms

    

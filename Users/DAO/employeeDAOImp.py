from Users.DAO import employeeDAO as em
from Database import databaseTools as data

class EmployeeDAOImp(em.EmployeeDAO):

    def getExpenseHistory(emailID):

        # cursor creates the link to the database
        cursor = data.conncursor(".\Database\expenses.db")

        # sql is the query you will run
        sql = '''SELECT formID, dateSubmitted, isGivenApproval, isReviewed, reviewAcceptance, approvalAcceptance, managerComment, reviewComment FROM expenseForm WHERE requester = ? ORDER BY formID DESC'''

        # cursor.execute executes the query. Pass through the query,
        # then the values which replace the ? in the query.
        cursor.execute(sql, [emailID])

        # Run cursor.fetchall to get the query results
        expenseForms = cursor.fetchall()

        # Close the database connection after finishing
        cursor.close()

        # return the results
        return expenseForms


    # Get claimID, expenseType, expenseDate, expenseCost, evidence
    # from expenseClaim Where requestor = emailID and formId = formID
    def getExpenseClaim(emailID, formID):
        
        # cursor creates the link to the database
        cursor = data.conncursor(".\Database\expenses.db")

        # sql is the query you will run
        sql = '''SELECT DISTINCT claimID, expenseType, expenseDate, expenseCost, evidence FROM expenseClaim, expenseForm WHERE expenseForm.requester = ? and expenseClaim.formID = ?'''

        # cursor.execute executes the query. Pass through the query,
        # then the values which replace the ? in the query.
        cursor.execute(sql, [emailID, formID])

        # Run cursor.fetchall to get the query results
        expenseForms = cursor.fetchall()

        # Close the database connection after finishing
        cursor.close()

        # return the results
        return expenseForms

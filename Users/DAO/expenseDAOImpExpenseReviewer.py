from Users.DAO import expenseDAO as exD # the interface we're extending
from Database import databaseTools as data

class ExpenseDAOImpExpenseReviewer(exD.ExpenseDAO):

    # Get formID, dateSubmitted, requester from expenseForm
    # where requester != emailID and isReviewed = False
    def getPendingExpenseList(emailID):
        
        # cursor creates the link to the database
        cursor = data.conncursor(".\Database\expenses.db")

        # sql is the query you will run
        sql = '''SELECT formID, dateSubmitted, requester FROM expenseForm WHERE requester != ? AND isReviewed = FALSE'''

        # cursor.execute executes the query. Pass through the query,
        # then the values which replace the ? in the query.
        cursor.execute(sql, [emailID])

        # Run cursor.fetchall to get the query results
        expenseForms = cursor.fetchall()

        # Close the database connection after finishing
        cursor.close()

        # return the results
        return expenseForms

    # Update expenseAcceptance to expenseAcceptance, reviewComment to comment
    # and isReviewed to True
    # where formID = formID
    def updateExpense(formID, expenseAcceptance, comment):
        
        # cursor creates the link to the database
        cursor = data.conncursor(".\Database\expenses.db")

        # sql is the query you will run
        sql = '''UPDATE expenseForm SET reviewAcceptance = ?, reviewComment = ?, isReviewed = TRUE WHERE formID = ?'''

        # cursor.execute executes the query. Pass through the query,
        # then the values which replace the ? in the query.
        cursor.execute(sql, [expenseAcceptance, comment, formID])

        # Run cursor.fetchall to get the query results
        expenseForms = cursor.fetchall()

        # Close the database connection after finishing
        cursor.close()

    # Get formID, dateSubmitted, requester, isReviewed, reviewAcceptance
    # from expenseForm where requester != emailID
    def getAllAllowedExpense(emailID):
        
        # cursor creates the link to the database
        cursor = data.conncursor(".\Database\expenses.db")

        # sql is the query you will run
        sql = '''SELECT formID, dateSubmitted, requester, isReviewed, reviewAcceptance FROM expenseForm WHERE requester != ?'''

        # cursor.execute executes the query. Pass through the query,
        # then the values which replace the ? in the query.
        cursor.execute(sql, [emailID])

        # Run cursor.fetchall to get the query results
        expenseForms = cursor.fetchall()

        # Close the database connection after finishing
        cursor.close()

        # return the results
        return expenseForms

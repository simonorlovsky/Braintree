'''
   CreditCard.py
   Simon Anatole Orlovsky, 2015-01-13

   Credit Card class modeling someone's credit card.
'''

class CreditCard:
	def __init__(self, firstName, cardNumber, creditLimit):
		self.fName = firstName
		self.cNumber = cardNumber
		self.cLimit = creditLimit
		self.currentBalance = 0

	def charge(amountDue):
		self.currentBalance -= amountDue

	def credit(amountOwed):
		self.currentBalance += amountOwed

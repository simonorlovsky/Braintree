'''
   CreditCard.py
   Simon Anatole Orlovsky, 2015-01-13

   Credit Card class modeling someone's credit card.
'''

class CreditCard:
	def __init__(self, firstName, cardNumber, creditLimit):
		self.fName = firstName
		self.cNumber = cardNumber
		self.cLimit = int(creditLimit[1:])
		self.currentBalance = 0

	def charge(self, amountDue):
		self.currentBalance = self.currentBalance+int(amountDue)

	def credit(self, amountOwed):
		self.currentBalance = self.currentBalance-int(amountOwed)

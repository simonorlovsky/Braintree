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
		self.currentBalance = 0 #new cards start with a 0 balance

	def charge(self, amountDue): #increase the balance of the card associated with the provided name by the amount specified
		self.currentBalance = self.currentBalance+int(amountDue)

	def credit(self, amountOwed): #decrease the balance of the card associated with the provided name by the amount specified
		self.currentBalance = self.currentBalance-int(amountOwed)

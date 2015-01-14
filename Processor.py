'''
   Processor.py
   Simon Anatole Orlovsky, 2015-01-13

   Reads lines from a file, understands what they mean, then processes them.
'''

import sys
from CreditCard import CreditCard

def load(inputFilePath):
	try:
	    inputFile = open(inputFilePath)
	except Exception, e:
	    print >>sys.stderr, 'Cannot open', inputFilePath
	    exit()

	cardsList = []
	creditsList = []
	chargesList = []
	for line in inputFile:
	    currentLine = line.split(" ")
	    # Want to make sure that I get everything into the right place
	    if currentLine[0]== "Add":
	    	newCard = CreditCard(currentLine[1], currentLine[2], currentLine[3])
	    	cardsList.append(newCard)
	    elif currentLine[0]== "Charge":
	    	chargesList.append(currentLine)
	    else:
	    	creditsList.append(currentLine)
	    	
	return cardsList, creditsList, chargesList

#this function goes through the chargesList and charges the proper cards.
def chargeAccounts(chargesList, cardsList):
	for i in range(len(chargesList)):
		
		currentCard = chargesList[i][1]
		amountDue = int(chargesList[i][2][1:])
		print currentCard, amountDue


def creditAccounts(creditsList, cardsList):
	for i in range(len(chargesList)):
		print chargesList[i]

def main():
	inputFilePath = sys.argv[1]
	cardsList, creditsList, chargesList = load(inputFilePath)
	chargeAccounts(chargesList, cardsList)

main()
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

	processes = []

	for line in inputFile:
	    currentLine = line.split(" ")
	    processes.append(currentLine)
	    	
	return processes

#luhn test
def luhn(n):
	r = [int(ch) for ch in str(n)][::-1]
	return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0

def merge(A,B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0].fName < B[0].fName:
        return [A[0]] + merge(A[1:],B)
    else:
        return [B[0]] + merge(A,B[1:])

def mergeSort(L):
    if len(L) <= 1:
        return L
    else:
        left = mergeSort(L[0:len(L)/2])
        right = mergeSort(L[len(L)/2:])
        return merge(left,right)

#this function goes through the chargesList and charges the proper cards.
def process(processes):
	cardsList = []
	cards = {}
	for i in range(len(processes)):
		if processes[i][0]== "Add":
			newCard = CreditCard(processes[i][1], processes[i][2], processes[i][3])
			if luhn(newCard.cNumber)== False:
				newCard.currentBalance = "error"
			cardsList.append(newCard)
			cards[newCard.fName] = newCard

		elif processes[i][0]== "Charge":
			personToCharge = processes[i][1]
			amountToCharge = processes[i][2][1:]

			cards[personToCharge]

			for j in range(len(cardsList)):
				if cardsList[j].fName == personToCharge:
					#Checking to see if card has enough credit for transaction
					if cardsList[j].cLimit> cardsList[j].currentBalance + int(amountToCharge) and cardsList[j].currentBalance!="error":
						cardsList[j].charge(amountToCharge)
						print "Charged", cardsList[j].fName, amountToCharge
					else:
						#card declined
						print "declined"
						

		elif processes[i][0]== "Credit":
			personToCredit = processes[i][1]
			amountToCredit = processes[i][2][1:]

			for j in range(len(cardsList)):
				if cardsList[j].fName == personToCredit and cardsList[j].currentBalance!="error":
					cardsList[j].credit(amountToCredit)
					print "Credited", cardsList[j].fName, amountToCredit

	return cardsList



def main():
	inputFilePath = sys.argv[1]
	processes = load(inputFilePath)
	cardsList = process(processes)
	cardsList = mergeSort(cardsList)
	for i in range(len(cardsList)):
		print cardsList[i].fName,":", cardsList[i].currentBalance

main()
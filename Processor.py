'''
   Processor.py
   Simon Anatole Orlovsky, 2015-01-13

   Reads lines from a file, understands what they mean, then processes them.
'''

import sys
from CreditCard import CreditCard


#Load function: Goes through space delimited input and creates list of processes
def load(inputFilePath):
	try:
	    inputFile = open(inputFilePath)
	except Exception, e:
	    print >>sys.stderr, 'Cannot open', inputFilePath #if the file isn't real through error
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

#using mergesort because it is O(n log n)
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

#this function goes through all of the processes and makes them all happen
def process(processes):
	#we're using a dictionary to take advantage of the O(1) look up rather than using a list
	cards = {}
	for i in range(len(processes)):
		if processes[i][0]== "Add":
			newCard = CreditCard(processes[i][1], processes[i][2], processes[i][3]) #instantiation of new card
			if luhn(newCard.cNumber)== False:
				newCard.currentBalance = "error"
			cards[newCard.fName] = newCard

		elif processes[i][0]== "Charge": #charging the card we need to charge
			personToCharge = cards[processes[i][1]]
			amountToCharge = processes[i][2][1:]
			if personToCharge.cLimit> personToCharge.currentBalance + int(amountToCharge) and personToCharge.currentBalance!="error": 
				#making sure that there is enough credit and the card is valid
				personToCharge.charge(amountToCharge)
						

		elif processes[i][0]== "Credit": #crediting the card we need to credit
			personToCredit = cards[processes[i][1]]
			amountToCredit = processes[i][2][1:]
			if personToCredit.currentBalance!="error": #making sure card passed the lun test
				personToCredit.credit(amountToCredit)

	return cards


def main():
	if sys.argv[1:].__len__()==0: #checking to make sure that the user is properly inputting commandline arguments
		print 'Usage: Processor.py <inputfile>' 

	else:
		inputFilePath = sys.argv[1]
		processes = load(inputFilePath)
		cardsList = process(processes)

		cardsToSort = []

		for i, v in enumerate(cardsList): #moving everything from the dictionary to the list so it's easier to iterate over
			cardsToSort.append(cardsList[v])

		cardsList = mergeSort(cardsToSort)
		f = open('output.txt', 'w')
		for i in range(len(cardsList)):
			print cardsList[i].fName+": "+ str(cardsList[i].currentBalance) #printing output
			f.write(cardsList[i].fName+": "+ str(cardsList[i].currentBalance)+ '\n')

main()
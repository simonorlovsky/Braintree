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
	    currentLine = line.split(",")
	    if currentLine[0]== "Add":
	    	creditsList.append(currentLine)
	    elif currentLine[0]== "Charge":
	    	chargesList.append(currentLine)
	    else:
	    	newCard = CreditCard(currentLine[0], currentLine[1], currentLine[2])
	    	cardsList.append(person)
	return cardsList, creditsList, chargesList

def main():
	inputFilePath = sys.argv[1]
	cardsList, creditsList, chargesList = load(inputFilePath)

main()
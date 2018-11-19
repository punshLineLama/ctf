#!/usr/bin/python3

import hash
import string
import sys

#generate a wordlist with ascii-uppercase letters with length 1-2
def generateWordList():
	wordList = []
	for j in string.ascii_uppercase:
		wordList.append(j)

	for i in string.ascii_uppercase:
		for j in string.ascii_uppercase:
			wordList.append(str(i+j))
	return wordList


hashTable = {}
print(string.printable)
for i in generateWordList():
	hashVal = hash.cictroHash(i)
	if(hashVal in hashTable.values()):
		print("This: "+str(i)+" collides with: "+ str(list(hashTable.keys())[list(hashTable.values()).index(hashVal)]))
		print("Found a collision!!!!")
		sys.exit("Found collision, yuuhuu")
	hashTable[i] = hashVal
print(hashTable)




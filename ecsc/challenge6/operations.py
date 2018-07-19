#!/usr/bin/python3.6
import sys

file = open("packets.txt")

def minus(times):
	print("-------minus-------")
	for i in range(len(times)-1):
		if(i%2 == 0):
			print(chr(abs(times[i]-times[i+1])), end = '')
	print(" ")

def xorOp(times):
	print("-------xor-------")
	for i in range(len(times)-1):
		if(i%2 == 0):
			print(chr(abs(times[i]^times[i+1])), end = '')
	print(" ")

def andOp(times):
	print("-------AND-------")
	for i in range(len(times)-1):
		if(i%2 == 0):
			print(chr(abs(times[i]&times[i+1])), end = '')
	print(" ")

def orOp(times):
	print("-------OR-------")
	for i in range(len(times)-1):
		if(i%2 == 0):
			print(chr(abs(times[i]|times[i+1])), end = '')
	print(" ")


times = []
for line in file:
	times.append(int(line.split('.')[1]))
minus(times)
xorOp(times)
andOp(times)
orOp(times)



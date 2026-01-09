import os
import random

from settings import Settings

def Naive(settings):
	return NaiveFunction(settings.start, settings.end)

def NaiveFunction(start, end):
	print("Finding primes from", start, "to", end)
	primes = []
	pQ = True
	for i in range(start, end):
		for j in range(2, int(i/2)+1):
			if i % j == 0:
				pQ = False
				break
		if pQ:
			primes.append(i)
		pQ = True
	return primes


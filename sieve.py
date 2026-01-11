import os
import random
import math

from settings import Settings

def Sieve(settings):
	return SieveFunction(settings.getStart(), settings.getEnd())

def SieveFunction(start, end):
	sieve = dict(zip(range(1, end), "o"*end))
	primes = []
	for p in range(2, int(math.sqrt(end)+0.5)):
		if sieve[p] != "m":
			pCount = 2*p
			while pCount <= end:
				sieve[pCount] = "m"
				pCount += p
	for i in range(start, end):
		if sieve[i] != "m":
			primes.append(i)
	return primes


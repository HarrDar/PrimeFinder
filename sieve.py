import os
import random

from settings import Settings

def Sieve(settings):
	return SieveFunction(settings.start, settings.end)

def SieveFunction(start, end):
	sieve = dict(zip(range(1, end), "o"*end))
	primes = []
	for p in range(2, end):
		if sieve[p] != "m":
			pCount = 2*p
			while pCount <= end:
				sieve[pCount] = "m"
				pCount += p
	for i in range(start, end):
		if sieve[i] != "m":
			primes.append(i)
	return primes


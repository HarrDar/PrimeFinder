import math

from settings import Settings

def SieveErat(settings):
	return sieveFunction(settings.getStart(), settings.getEnd())

def sieveFunction(start, end):
	l = int(math.sqrt(end)+0.5)
	sieve = [False]*end
	primes = []
	for p in range(2, l):
		if not sieve[p]:
			pCount = p*p
			while pCount < end:
				sieve[pCount] = True
				pCount += p
	for i in range(start, end):
		if not sieve[i]:
			primes.append(i)
	return primes


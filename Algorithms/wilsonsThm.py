import math

from settings import Settings

def WilsonsTheorem(settings):
	if settings.getEnd() >= 100000:
		print("WARNING: Wilson's Theorem uses extremely large numbers as it calculates on, so is not reccomended for high limits.")
	return wilsonFunction(settings.getStart(), settings.getEnd())

def wilsonFunction(start, end):
	primes = [2]
	p0 = 2
	fac = 1
	for n in range(3,end):
		fac *= (n-1)
		if fac % n == (n-1):
			primes.append(n)
	return primes


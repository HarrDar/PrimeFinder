import math

from settings import Settings

def SieveAtkin(settings):
	return sieveFunction(settings.getStart(), settings.getEnd())

def sieveFunction(start, end):
	l = int(math.sqrt(end))
	sieve = [False]*(end+1)
	primes = []
	if end >=2:
		primes.append(2)
	if end >=3:
		primes.append(3)
	for x in range(1, l+1):
		for y in range(1,l+1):
			c1 = (4*(x*x)) + (y*y)
			if c1 <= end and (c1 % 12 == 1 or c1 % 12 == 5):
				sieve[c1] = not sieve[c1]

			c2 = (3*(x*x)) + (y*y)
			if c2 <= end and (c2 % 12 == 7):
				sieve[c2] = not sieve[c2]

			c3 = (3*(x*x)) - (y*y)
			if x > y and c3 <= end and (c3 % 12 == 11):
				sieve[c3] = not sieve[c3]

	for p in range(5, l+1):
		q = p*p
		while q <= end:
			sieve[q] = False
			q += (p*p)

	for i in range(1, end):
		if sieve[i]:
			primes.append(i)
	return primes


import math

from settings import Settings

def SieveSund(settings):
	return sieveFunction(settings.getStart(), settings.getEnd())

def sieveFunction(start, end):
	l = int((end-1)/2)
	sieve = [False]*(l+1)
	primes = []
	for p in range(1, l+1):
		q = 1
		while(p+q+(2*p*q)) < l:
			sieve[p+q+(2*p*q)] = True
			q += 1

	#Edge case: 2 is never found in alg
	if start <=2:
		primes.append(2)
	for i in range(1, l):
		if not sieve[i] and (2*i)+1 >= start:
			primes.append((2*i)+1)
	return primes


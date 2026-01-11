import os
import time

from settings import Settings
from Algorithms.naive import Naive
from Algorithms.sieveErat import SieveErat

Algs = ["Naive (N)", "Sieve of Eratosthenes (SE)", "Sieve of Sundaram (SS)", "Settings (S)", "Exit (E)"]

def main():
	settings = Settings()
	primes = []
	tstart = 0
	tend = 0

	while True:
		print("Choose Algorithm (or Settings):")
		for a in Algs:
			print(a)
		alg = input()
		print("Finding primes from", settings.getStart(), "to", settings.getEnd())
		tstart = time.time()
		if alg.lower() == "n":
			primes = Naive(settings)
		elif alg.lower() == "se":
			primes = SieveErat(settings)
		elif alg.lower() == "s":
			print("Please input a new starting number then ending number:")
			start = input()
			end = input()
			settings.setStart(start)
			settings.setEnd(end)
		elif alg.lower() == "e":
			break
		else:
			print("Function not found")
		tend = time.time()
		print("Time Elapsed:", tend-tstart, "s")

		print(len(primes), "prime numbers found")
		if len(primes) > settings.getPrintAmount():
			for i in range(settings.getPrintLow()):
				print(primes[i], ", ", sep='', end='')
			print("....., ", end='')
			for i in range(len(primes)-(settings.getPrintHigh()+1), len(primes)-1):
				print(primes[i], ", ", sep='', end='')
			print('')
		else:
			print(primes)
		print("")
main()
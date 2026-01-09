import os
import time

from settings import Settings
from naive import Naive

def main():
	settings = Settings()
	primes = []
	tstart = 0
	tend = 0
	while True:
		print("Choose Algorithm (or Settings):\nNaive (N):\nSieve of Eratosthenes (SE):\nSettings(S):")
		alg = input()
		tstart = time.time()
		if alg.lower() == "n":
			primes = Naive(settings)
		elif alg.lower() == "s":
			print("Please input a new starting number then ending number:")
			start = input()
			end = input()
			settings.setStart(start)
			settings.setEnd(end)
		else:
			print("Function not found")
		tend = time.time()
		print("Time Elapsed:", tend-tstart, "s")
		print(len(primes), "prime numbers found")
		if len(primes) > settings.printAmount:
			for i in range(settings.printLow):
				print(primes[i], ", ", sep='', end='')
			print("....., ", end='')
			for i in range(len(primes)-(settings.printHigh+1), len(primes)-1):
				print(primes[i], ", ", sep='', end='')
			print('')
		else:
			print(primes)
main()
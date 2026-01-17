import os
import time

from settings import Settings
from Algorithms.naive import Naive
from Algorithms.sieveErat import SieveErat
from Algorithms.sieveSund import SieveSund
from Algorithms.sieveAtkin import SieveAtkin
from Algorithms.wilsonsThm import WilsonsTheorem

def settingsFunction(settings):
	print("Please input a new starting number then ending number:")
	start = input()
	end = input()
	settings.setStart(start)
	settings.setEnd(end)
	return "settings"

def exitProgram(settings):
	exit()

#Algorithms added in form Name, Tag, Function
Algs = [["Naive", "N", Naive], ["Sieve of Eratosthenes", "SE", SieveErat], ["Sieve of Sundaram", "SS", SieveSund], ["Sieve of Atkin", "SA", SieveAtkin], ["Wilson's Theorem", "W", WilsonsTheorem], ["Settings", "S", settingsFunction], ["Exit", "E", exitProgram]]

def main():
	settings = Settings()
	primes = []
	tstart = 0
	tend = 0

	while True:
		print("Choose Algorithm (or Settings):")
		for a in Algs:
			print(a[0], " (", a[1], ")", sep='')
		alg = input()
		tstart = time.time()
		foundFunc = False
		for a in Algs:
			if a[1] == alg.upper():
				if alg.upper() not in ["S","E"]:
					print("Finding primes from", settings.getStart(), "to", settings.getEnd())
				primes = a[2](settings)
				foundFunc = True
				break

		tend = time.time()
		if not foundFunc:
			print("Function not found")
		elif primes == "settings":
			primes = []
		elif len(primes) == 0:
			print("Range contains no primes")
		else:
			print("Time Elapsed:", tend-tstart, "s")
			print(len(primes), "prime numbers found")

			if len(primes) > settings.getPrintAmount():
				for i in range(settings.getPrintLow()):
					print(primes[i], ", ", sep='', end='')
				print("....., ", end='')
				for i in range(len(primes)-(settings.getPrintHigh()+1), len(primes)):
					print(primes[i], ", ", sep='', end='')
				print('')
			else:
				print(primes)
		print("")
main()
import os
import random

class Settings:
	start = 1
	end = 1000
	printAmount = 50
	printHigh = 25
	printLow = 25

	def __init__(self):
		pass

	def setStart(self, startPass):
		self.start = int(startPass)

	def setEnd(self, endPass):
	 	self.end = int(endPass)
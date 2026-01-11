import os
import random

class Settings:
	sets = {}

	def __init__(self):
		stream = open("settings.txt")
		line = stream.readline()
		while line:
			split = line.index(":")
			name = line[:split]
			val = line[split+1:]
			self.sets[name] = int(val)
			line = stream.readline()
		stream.close()

	def setStart(self, startPass):
		self.sets["start"] = int(startPass)

	def setEnd(self, endPass):
	 	self.sets["end"] = int(endPass)

	def getStart(self):
	 	return self.sets["start"]

	def getEnd(self):
	 	return self.sets["end"]

	def getPrintAmount(self):
	 	return self.sets["printAmount"]

	def getPrintHigh(self):
	 	return self.sets["printHigh"]

	def getPrintLow(self):
	 	return self.sets["printLow"]

	def err(self):
		print("ERROR: No Var Found")

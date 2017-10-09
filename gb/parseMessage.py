from Instruction import Instruction
from GBInstruction import GBInstruction
from DriverInstruction import DriverInstruction
from StrategyInstruction import StrategyInstruction
from SensorData import SensorData
from GPS import GPS
import re

""" Method for parsing incoming strings called messages """
def parseMessage(inputString):
	# Split the string in parts into a list
	splitUp = re.split(',', inputString)
	length = len(splitUp)

	# Create a driver instruction object from the message 
	if splitUp[0] == 'dr' and length == 4:
		try:
			d = DriverInstruction(splitUp[1], splitUp[2], splitUp[3])		
			return d

		except IndexError:
			print "Invalid driver instruction format, instruction not created" 

	# Create a strategy instruction object from the message 
	elif splitUp[0] == 'st' and length == 5:
		try:
			st = StrategyInstruction(splitUp[1], splitUp[2], splitUp[3], splitUp[4])
			return st
			
		except IndexError:
			print "Invalid strategy instruction format, instruction not created" 

	# Create a sensor data object from the message 
	elif splitUp[0] == 'se' and length == 5:
		try:
			se = SensorData(splitUp[1], splitUp[2], splitUp[3], splitUp[4])
			return se			
		
		except IndexError:
			print "Invalid strategy instruction format, instruction not created" 

	# Create a gps object from the message 
	elif splitUp[0] == 'gp' and length == 5:
		try:
			gp = GPS(splitUp[1], splitUp[2], splitUp[3], splitUp[4])
			return gp			
		
		except IndexError:
			print "Invalid strategy instruction format, instruction not created" 

	else:
		print('Invalid instruction input')

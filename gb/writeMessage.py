import boto.sqs
from boto.sqs.message import Message
from GBInstruction import GBInstruction
from SensorData import SensorData
from GPS import GPS


""" Write a message from ground base to the Ecorunner """
def writeMessage(objectToSend):
	
	# Write a message for the gb instruction object
	if isinstance(objectToSend, GBInstruction):
		mString = "gb," + str(objectToSend.getFcPower()) + "," + str(objectToSend.getThrottleAdv()) + "," + str(objectToSend.getSteerAdv()) + "," + str(objectToSend.getMotorSet()) + "," + str(objectToSend.getTimestamp())
		return mString

	# If for some reason another object is given, do nothing
	else:
		pass

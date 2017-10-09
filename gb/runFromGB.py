from Instruction import Instruction
from GBInstruction import GBInstruction
from DriverInstruction import DriverInstruction
from StrategyInstruction import StrategyInstruction
from SensorData import SensorData
from GPS import GPS
from parseMessage import parseMessage
from readMessage import nextMessage
from addToGBDatabase import addToDatabase
from cleardb import cleardb
import sys
import re
import time
import boto.sqs
from boto.sqs.message import Message
import MySQLdb

# Connect to the queue server
conn = boto.sqs.connect_to_region("eu-central-1", aws_access_key_id = "AKIAI5H2RJ4GG4VZGLDQ", aws_secret_access_key = "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")
receiveQueue = conn.get_queue('Eco2GB')

# Clear the database before running
cleardb()
# clear alle queue's 

while(True):	
	try:
		message = nextMessage(receiveQueue)
		addToDatabase(message)

		time.sleep(.001)

	
	
	except KeyboardInterrupt:
		sys.exit()


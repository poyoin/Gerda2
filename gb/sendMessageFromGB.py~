from GBInstruction import GBInstruction
from Instruction import Instruction
import sys
import re
import boto.sqs
from boto.sqs.message import Message
from datetime import datetime
from writeMessage import writeMessage
from addToGBDatabase import addToDatabase


""" 99% foolproof method to send a gb instruction to the EcoRunner """
# Connect to the queue server
conn = boto.sqs.connect_to_region("eu-central-1", aws_access_key_id = "AKIAI5H2RJ4GG4VZGLDQ", aws_secret_access_key = "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")
sendQueue = conn.get_queue('GB2Eco')

while True:	
	try:
		# Ask for user input, which is a simplified form of the gb instruction
		instruction = raw_input("New FC Power: ")
	
		# Parse the simple form to values for a gb instruction
		# splitUp = re.split(instruction)
		fcpower = int(instruction)
		# throttleAdv = int(splitUp[1])
		# steerAdv = int(splitUp[2])
		# motorSet = int(splitUp[3])

		# If the input has the right format, make a gb instruction
		if fcpower > 0 and fcpower < 100:
			timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
			gb = GBInstruction(fcpower, -1, -1, -1, timestamp)

			# Send the instruction to the EcoRunner
			m = Message()
			m.set_body(writeMessage(gb))	
			sendQueue.write(m)
			print gb.toString() + " Sent to the EcoRunner"

			# Add the instruction to the GB database for logging
			addToDatabase(gb)

		else:
			print "Value out of bounds, nothing sent"
		

	except IndexError:
		print "Wrong input format, nothing sent"

	except ValueError:
		print "Wrong input format, nothing sent"

	except NameError:
		print "Wrong input format, nothing sent"

	except KeyboardInterrupt:
		sys.exit(0)
	

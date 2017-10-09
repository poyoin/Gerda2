import unittest
import sys
import MySQLdb

from Instruction import Instruction
from DriverInstruction import DriverInstruction
from GBInstruction import GBInstruction
from StrategyInstruction import StrategyInstruction
from SensorData import SensorData
from GPS import GPS
from addToGBDatabase import addToDatabase
from cleardb import cleardb
from parseMessage import parseMessage
from writeMessage import writeMessage
from nmeaToDecimal import toDecimal

""" Test class for the DriverInstruction module """
class TestDriverInstruction(unittest.TestCase):

	# Test if the right object is created
	def testTypeOfDriverInstruction(self):
		self.assertTrue(isinstance(DriverInstruction(4, 5, 2), Instruction))

	# Test the get throttle method
	def testGetThrottle(self):
		self.assertEquals(DriverInstruction(4, 5, 2).getThrottle(), 4)

	# Test the get display switch method
	def testGetDisplaySwitch(self):
		self.assertEquals(DriverInstruction(4, 5, 2).getDisplaySwitch(), 5)

	# Test the get timestamp method
	def testGetTimeStamp(self):
		self.assertEquals(DriverInstruction(4, 5, 2).getTimestamp(), 2)

	# Test the toString method
	def testToString(self):
		self.assertEquals(DriverInstruction(4, 5, 2).toString(), "type: Driver, throttle: 4, displaySwitch: 5, timestamp: 2")


""" Test class for the DriverInstruction module """
class TestGBInstruction(unittest.TestCase):

	# Test if the right object is created
	def testTypeOfGBInstruction(self):
		self.assertTrue(isinstance(GBInstruction(14, 5, 7, 9, 2), Instruction))

	# Test the get fc power method
	def testGetFcPower(self):
		self.assertEquals(GBInstruction(4, 5, 7, 9, 2).getFcPower(), 4)

	# Test the get throttle advice method
	def testGetThrottleAdv(self):
		self.assertEquals(GBInstruction(4, 5, 7, 9, 2).getThrottleAdv(), 5)

	# Test the get steer advice method
	def testGetSteerAdv(self):
		self.assertEquals(GBInstruction(4, 5, 7, 9, 2).getSteerAdv(), 7)

	# Test the get timestamp method
	def testGetTimeStamp(self):
		self.assertEquals(GBInstruction(4, 5, 7, 9, 2).getTimestamp(), 2)

	# Test the toString method
	def testToString(self):
		self.assertEquals(GBInstruction(4, 5, 7, 9, 2).toString(), "type: GB, fc Power: 4, throttle advice: 5, Steer advice: 7, motor settings: 9, timestamp: 2")


""" Test class for the DriverInstruction module """
class TestStrategyInstruction(unittest.TestCase):

	# Test if the right object is created
	def testTypeOfStrategyInstruction(self):
		self.assertTrue(isinstance(StrategyInstruction(4, 5, 7, 2), Instruction))

	# Test the get fc power method
	def testGetFcPower(self):
		self.assertEquals(StrategyInstruction(4, 5, 7, 2).getFcPower(), 4)

	# Test the get throttle advice method
	def testGetThrottleAdv(self):
		self.assertEquals(StrategyInstruction(4, 5, 7, 2).getThrottleAdv(), 5)

	# Test the get motor settings method
	def testGetMotorSet(self):
		self.assertEquals(StrategyInstruction(4, 5, 7, 2).getMotorSet(), 7)

	# Test the get timestamp method
	def testGetTimeStamp(self):
		self.assertEquals(StrategyInstruction(4, 5, 7, 2).getTimestamp(), 2)

	# Test the toString method
	def testToString(self):
		self.assertEquals(StrategyInstruction(4, 5, 7, 2).toString(), "type: Strategy, fc Power: 4, throttle advice: 5, motor settings: 7, timestamp: 2")

""" Test class for the sensor data module """
class TestSensorData(unittest.TestCase):

	# Test if the right object is created
	def testTypeOfSensorData(self):
		self.assertTrue(isinstance(SensorData("1", "power", 5, "123.456"), SensorData))

	# Test the get throttle method
	def testGetSensorId(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getSensorId(), "1")

	# Test the get display switch method
	def testGetMsgType(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getMsgType(), "power")

	# Test the get timestamp method
	def testGetData(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getData(), 5)

	# Test the get timestamp method
	def testGetTimeStamp(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getTimestamp(), "123.456")

	# Test the toString method
	def testToString(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").toString(), "SensorId: 1, MessageType: power, Data: 5, timestamp: 123.456")


""" Test class for the gps module """
class TestGPS(unittest.TestCase):

	# Test if the right object is created
	def testTypeOfGPS(self):
		self.assertTrue(isinstance(GPS("1234.567890", "0987.654321", 5.10, "123.456"), GPS))

	# Test the get throttle method
	def testGetLongtitude(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getLongtitude(), "1234.567890")

	# Test the get display switch method
	def testGetLattitude(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getLattitude(), "0987.654321")

	# Test the get timestamp method
	def testGetSpeed(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getSpeed(), 5.10)

	# Test the get timestamp method
	def testGetTimeStamp(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getTimestamp(), "123.456")

	# Test the toString method
	def testToString(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").toString(), "GPS: Longtitude: 1234.567890, Lattitude: 0987.654321, Speed: 5.1, Timestamp: 123.456")




""" Test class for the module addToGBDatabase """
class TestAddToDB(unittest.TestCase):
	
	# Test adding driver instructions to the database
	def testAddDriverInstruction(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = DriverInstruction(5, 6, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM DriverInstructions")
		result = cursor.fetchone()
		dbId = result[0]
		dbThrottle = result[1]
		dbDisplaySwitch = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbThrottle == 5 and dbDisplaySwitch == 6 and dbTimestamp == "123.456.789")


	# Test adding strategy instructions to the database
	def testAddStrategyInstruction(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = StrategyInstruction(5, 6, 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM StrategyInstructions")
		result = cursor.fetchone()
		dbId = result[0]
		dbFCPower = result[1]
		dbThrottleAdv = result[2]
		dbMotorSet = result[3]
		dbTimestamp = result[4]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbFCPower == 5 and dbThrottleAdv == 6 and dbMotorSet == 7 and dbTimestamp == "123.456.789")


	# Test adding gb instructions to the database
	def testAddGBInstruction(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = GBInstruction(5, 6, 7, 8, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM GBInstructions")
		result = cursor.fetchone()
		dbId = result[0]
		dbFCPower = result[1]
		dbThrottleAdv = result[2]
		dbSteerAdv = result[3]
		dbMotorSet = result[4]
		dbTimestamp = result[5]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbFCPower == 5 and dbThrottleAdv == 6 and dbSteerAdv == 7 and dbMotorSet == 8 and dbTimestamp == "123.456.789")


	# Test adding data from the first power sensor to the database
	def testAddPower1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("1", "power", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Power1")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "power" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the second power sensor to the database
	def testAddPower2(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("2", "power", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Power2")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "power" and dbData == "7" and dbTimestamp == "123.456.789")

	
	# Test adding data from the third power sensor to the database
	def testAddPower3(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("3", "power", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Power3")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "power" and dbData == "7" and dbTimestamp == "123.456.789")


	
	# Test adding data from the first rpm sensor to the database
	def testAddRPM1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("4", "rpm", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Rpm1")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "rpm" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the second rpm sensor to the database
	def testAddRPM2(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("5", "rpm", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Rpm2")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "rpm" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the third rpm sensor to the database
	def testAddRPM3(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("6", "rpm", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Rpm3")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "rpm" and dbData == "7" and dbTimestamp == "123.456.789")

	
	# Test adding data from the first voltage sensor to the database
	def testAddVoltage1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("7", "voltage", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Voltage1")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "voltage" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the first voltage sensor to the database
	def testAddVoltage2(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("8", "voltage", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Voltage2")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "voltage" and dbData == "7" and dbTimestamp == "123.456.789")


		# Test adding data from the first voltage sensor to the database
	def testAddVoltage1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("9", "current", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Current1")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "current" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the first voltage sensor to the database
	def testAddVoltage1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("10", "current", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Current2")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "current" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the first voltage sensor to the database
	def testAddGPS(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()

		# Add a information to the database
		dr = GPS("1234.567865", "098765.4321", 7.20, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM GPS")
		result = cursor.fetchone()
		dbId = result[0]
		dbLong = result[1]
		dbLat = result[2]
		dbSpe = result[3]
		dbTimestamp = result[4]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbLong == "1234.567865" and dbLat == "098765.4321" and dbSpe == 7.20 and dbTimestamp == "123.456.789")


""" Test class for the parse message module """
class TestParseMessage(unittest.TestCase):

	# Test if the right gps object is created
	def testTypeOfGPS(self):
		self.assertTrue(isinstance(parseMessage('gp,2,3,4,5'), GPS))

	# Test for a correct instantiation of gps input
	def testCorrectGPS(self):
        	self.assertEqual(parseMessage('gp,2,3,4,5').toString(), 'GPS: Longtitude: 2, Lattitude: 3, Speed: 4, Timestamp: 5')

	# Test for an incorrect instantiation of gps input
	def testIncorrectGPS(self):
        	self.assertNotEqual(parseMessage('gp,2,3,4,5'), 'GPS: Longtitude: 3, Lattitude: 4, Speed: 5, Timestamp: 6')

	# Test for an incorrect length of gps input
	def testIncorrectGPSLength(self):
        	self.assertEqual(parseMessage('gp,2,3,4,5,6'), None)


	# Test if the right sensor object is created
	def testTypeOfSensor(self):
		self.assertTrue(isinstance(parseMessage('se,1,"power",4,5'), SensorData))

	# Test for a correct instantiation of sensor input
	def testCorrectSensor(self):
        	self.assertEqual(parseMessage('se,1,"power",4,5').toString(), 'SensorId: 1, MessageType: "power", Data: 4, timestamp: 5')

	# Test for an incorrect instantiation of sensor input
	def testIncorrectSensor(self):
        	self.assertNotEqual(parseMessage('se,1,"power",4,5'), 'SensorId: 1, MessageType: "power", Data: 5, timestamp: 6')

	# Test for an incorrect length of sensor input
	def testIncorrectDriverLength(self):
        	self.assertEqual(parseMessage('se,1,"power",4,5,6'), None)

	
	# Test if the right driver instruction object is created
	def testTypeOfDriver(self):
		self.assertTrue(isinstance(parseMessage('dr,1,4,5'), DriverInstruction))

	# Test for a correct instantiation of driver instruction
	def testCorrectDriver(self):
        	self.assertEqual(parseMessage('dr,1,4,5').toString(), 'type: Driver, throttle: 1, displaySwitch: 4, timestamp: 5')

	# Test for an incorrect instantiation of driver instruction
	def testIncorrectDriver(self):
        	self.assertNotEqual(parseMessage('dr,1,4,5'), 'type: Driver, throttle: 3, displaySwitch: 5, timestamp: 6')

	# Test for an incorrect length of driver input
	def testIncorrectDriverLength(self):
        	self.assertEqual(parseMessage('dr,1,4,5,6'), None)


	# Test if the right strategy instruction object is created
	def testTypeOfStrategy(self):
		self.assertTrue(isinstance(parseMessage('st,1,4,5,6'), StrategyInstruction))

	# Test for a correct instantiation of strategy instruction
	def testCorrectStrategy(self):
        	self.assertEqual(parseMessage('st,1,4,5,6').toString(), 'type: Strategy, fc Power: 1, throttle advice: 4, motor settings: 5, timestamp: 6')

	# Test for an incorrect instantiation of strategy instruction
	def testIncorrectStrategy(self):
        	self.assertNotEqual(parseMessage('st,1,4,5,6'), 'type: Strategy, fc Power: 2, throttle advice: 5, motor settings: 6, timestamp: 7')

	# Test for an incorrect length of strategy input
	def testIncorrectStrategyLength(self):
        	self.assertEqual(parseMessage('st,1,4,5,6,7'), None)


	# Test if the right exception is handled on incorrect input
	def testCatchIncorrectOveralFormat(self):
		self.assertRaises(IndexError, parseMessage('Some incorrect input'))


""" Test class for the writeMessage module """
class TestWriteMessage(unittest.TestCase):		

	# Test for an incorrect object
	def testIncorrectObject(self):
		st = StrategyInstruction(1, 2, 3, 4)
  	      	self.assertEqual(writeMessage(st), None)

	# Test with a correct gb instruction object
	def testCorrectGPS(self):
		gb = GBInstruction(1, 2, 3, 4, 5)
		self.assertEqual(writeMessage(gb), "gb,1,2,3,4,5")


""" Test class for the nmea to decimal conversion module """
class TestNmeaToDecimal(unittest.TestCase):

	# Test for a correct lattitude
	def testCorrectLat(self):
		self.assertEqual(toDecimal("5159.991278", "lat"), 51.999854633333335)

	# Test for a correct longtitude
	def testCorrectLon(self):
		self.assertEqual(toDecimal("00422.572693", "lon"), 4.37621155)

	# Test for an incorrect type
	def testIncorrectType(self):
		self.assertEqual(toDecimal("00422.572693", "trombone"), None)

	# Test for a correct type but incorrect value
	def testIncorrectType(self):
		self.assertEqual(toDecimal("trombone", "lat"), None)


if __name__ == '__main__':
    unittest.main()

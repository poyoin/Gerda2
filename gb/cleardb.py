import MySQLdb

"""" Clear all data from every table """
def cleardb():
	db = MySQLdb.connect("localhost","root","reverse","mydata")
	cursor = db.cursor()

	cursor.execute("""TRUNCATE TABLE GBInstructions""")
	cursor.execute("""TRUNCATE TABLE StrategyInstructions""")
	cursor.execute("""TRUNCATE TABLE Power1""")
	cursor.execute("""TRUNCATE TABLE Power2""")
	cursor.execute("""TRUNCATE TABLE Power3""")
	cursor.execute("""TRUNCATE TABLE Rpm1""")
	cursor.execute("""TRUNCATE TABLE Rpm2""")
	cursor.execute("""TRUNCATE TABLE Rpm3""")
	cursor.execute("""TRUNCATE TABLE DriverInstructions""")
	cursor.execute("""TRUNCATE TABLE Voltage1""")
	cursor.execute("""TRUNCATE TABLE Voltage2""")
	cursor.execute("""TRUNCATE TABLE Current1""")
	cursor.execute("""TRUNCATE TABLE Current2""")
	cursor.execute("""TRUNCATE TABLE GPS""")
	db.close()


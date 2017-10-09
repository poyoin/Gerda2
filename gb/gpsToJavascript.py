from flask import Flask
from flask import render_template
from nmeaToDecimal import toDecimal
import MySQLdb
import time
import sys

app = Flask(__name__)

def getData():
	db = MySQLdb.connect("localhost","root","reverse","mydata" )
	cursor = db.cursor()
	cursor.execute("SELECT * FROM GPS ORDER BY id DESC LIMIT 1;")
	lastRow = cursor.fetchall()
	lt = str(lastRow[0][2])
	ln = str(lastRow[0][1])
	db.close()
	return toDecimal(lt, "lat") , toDecimal(ln, "lon")


@app.route('/', methods = ['GET'])
def updateGPS():
		lt, ln = getData()
		print "New location sent"
		return render_template("index.html", lat = lt, lon = ln)

if __name__ == "__main__":
	app.run(debug = True)

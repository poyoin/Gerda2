import gmplot
from nmeaToDecimal import toDecimal
import sys
import time
import urllib
import urllib2
import MySQLdb

while True:
	try:	
		gmap = gmplot.GoogleMapPlotter(52.422386, 4.700596, 17)
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()
		cursor.execute("SELECT * FROM GPS ORDER BY id DESC LIMIT 1;")
		lastRow = cursor.fetchall()
		lon = str(lastRow[0][1])
		lat = str(lastRow[0][2])

		gmap.marker(toDecimal(lat, "lat"), toDecimal(lon, "lon"), color='#FF0000', c=None, title="no implementation")

		gmap.draw("mymap.html")
		time.sleep(5)

	except IndexError:
		time.sleep(4)

	except KeyboardInterrupt:
		sys.exit(0)

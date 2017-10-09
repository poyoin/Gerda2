import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sys
import MySQLdb
import math

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim([0,100])
plt.axis('equal')

lines = []
x = 0

def animate(i):
	try:	
		db = MySQLdb.connect("localhost","root","reverse","mydata")
		cursor = db.cursor()
		global x
		x = int(x) + 1
		cursor.execute("SELECT * FROM Rpm1 ORDER BY id DESC LIMIT 1;")
		lastRow = cursor.fetchall()
		rpm = float(lastRow[0][2])
		ms = rpm*0.475*math.pi/60
		frank = ms*3.6
		y = str(frank)

		lines.append(str(x) + "," + y)
	
		xs = []
		ys = []	
		for line in lines:
			if len(line) > 1 and frank < 300:
				x, y = line.split(',')
				xs.append(x)
				ys.append(y)

		ax1.clear()
		ax1.plot(xs, ys)

	except IndexError:
		pass

	except AttributeError:
		pass


try:
	ani = animation.FuncAnimation(fig, animate, interval=500)
	plt.show()

except KeyboardInterrupt:
	sys.exit()




import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sys
import MySQLdb

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
# To-do: Fix adequate ratios
plt.ylim(plt.ylim()[0], 200)
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
		y = str(lastRow[0][2])
		lines.append(str(x) + "," + y)
	
		xs = []
		ys = []	
		for line in lines:
			if len(line) > 1:
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

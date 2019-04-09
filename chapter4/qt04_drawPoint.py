import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Drawing(QWidget):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		self.setWindowTitle('在窗口中画点')
		self.resize(300, 200)

	def paintEvent(self, event):
		qpen = QPainter(self)
		qpen.begin(self)
		self.drawPoint(event, qpen)
		qpen.end()

	def drawPoint(self, event, qpen):
		qpen.setPen(Qt.red)
		size = self.size()

		for i in range(1000):
			x = 100*(-1+2.0*i/1000)+size.width()/2.0
			y = -50*math.sin((x-size.width()/2.0)*math.pi/50) + size.height()/2.0
			qpen.drawPoint(x,y)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Drawing()
	demo.show()
	sys.exit(app.exec())

import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt


class Drawing(QWidget):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 280, 270)
		self.setWindowTitle('钢笔样式例子')

	def paintEvent(self, event):
		qpen = QPainter(self)
		qpen.begin(self)
		self.drawLines(qpen)
		qpen.end()

	def drawLines(self, qpen):
		pen = QPen(Qt.black, 2, Qt.SolidLine)
		qpen.setPen(pen)
		qpen.drawLine(20, 40, 250, 40)

		pen.setStyle(Qt.DashLine)
		qpen.setPen(pen)
		qpen.drawLine(20, 80, 250, 80)

		pen.setStyle(Qt.DashDotLine)
		qpen.setPen(pen)
		qpen.drawLine(20, 120, 250, 120)

		pen.setStyle(Qt.DotLine)
		qpen.setPen(pen)
		qpen.drawLine(20, 160, 250, 160)

		pen.setStyle(Qt.DashDotDotLine)
		qpen.setPen(pen)
		qpen.drawLine(20, 200, 250, 200)

		pen.setStyle(Qt.CustomDashLine)
		pen.setDashPattern([1, 4, 5, 4])
		qpen.setPen(pen)
		qpen.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Drawing()
	demo.show()
	sys.exit(app.exec())

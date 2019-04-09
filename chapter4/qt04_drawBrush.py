import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt


class Drawing(QWidget):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 365, 280)
		self.setWindowTitle('画刷例子')
		self.show()

	def paintEvent(self, event):
		qpen = QPainter(self)
		qpen.begin(self)
		self.drawLines(qpen)
		qpen.end()

	def drawLines(self, qpen):
		brush = QBrush(Qt.SolidPattern)
		qpen.setBrush(brush)
		qpen.drawRect(10,15,90,60)

		brush = QBrush(Qt.Dense1Pattern)
		qpen.setBrush(brush)
		qpen.drawRect(130,15,90,60)

		brush = QBrush(Qt.Dense2Pattern)
		qpen.setBrush(brush)
		qpen.drawRect(250,15,90,60)

		brush = QBrush(Qt.Dense3Pattern)
		qpen.setBrush(brush)
		qpen.drawRect(10,105,90,60)

		brush = QBrush(Qt.DiagCrossPattern)
		qpen.setBrush(brush)
		qpen.drawRect(10,105,90,60)

		brush = QBrush(Qt.Dense5Pattern)
		qpen.setBrush(brush)
		qpen.drawRect(130,105,90,60)

		brush = QBrush(Qt.Dense6Pattern)
		qpen.setBrush(brush)
		qpen.drawRect(250,105,90,60)

		brush = QBrush(Qt.HorPattern)
		qpen.setBrush(brush)
		qpen.drawRect(10,195,90,60)

		brush = QBrush(Qt.VerPattern)
		qpen.setBrush(brush)
		qpen.drawRect(130,195,90,60)

		brush = QBrush(Qt.BDiagPattern)
		qpen.setBrush(brush)
		qpen.drawRect(250,195,90,60)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Drawing()
	demo.show()
	sys.exit(app.exec())

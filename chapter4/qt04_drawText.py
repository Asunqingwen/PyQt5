import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Drawing(QWidget):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		self.setWindowTitle('在窗口中绘制文字')
		self.resize(300, 200)
		self.text = '欢迎学习PyQt5'

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.begin(self)
		self.drawText(event, painter)
		painter.end()

	def drawText(self, event, qpen):
		qpen.setPen(QColor(168, 34, 3))
		qpen.setFont(QFont('SimSun', 30))
		qpen.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Drawing()
	demo.show()
	sys.exit(app.exec())

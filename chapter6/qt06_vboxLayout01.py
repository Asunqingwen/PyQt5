import sys
from PyQt5.QtWidgets import *


class Winform(QWidget):
	def __init__(self, parent=None):
		super(Winform, self).__init__(parent)
		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		self.setLayout(grid)

		names = ['Cls', 'Back', '', 'Close',
		         '7', '8', '9', '/',
		         '4', '5', '6', '*',
		         '1', '2', '3', '-',
		         '0', '.', '=', '+']

		positions = [(i, j) for i in range(5) for j in range(4)]

		for position, name in zip(positions, names):
			if name == '':
				continue

			button = QPushButton(name)
			grid.addWidget(button, *position)
		self.move(300, 150)
		self.setWindowTitle('网格布局管理例子')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Winform()
	win.show()
	sys.exit(app.exec())

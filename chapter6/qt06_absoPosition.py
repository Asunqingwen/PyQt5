import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		lab1 = QLabel('欢迎', self)
		lab1.move(15, 10)

		lab2 = QLabel('学习', self)
		lab2.move(35, 40)

		lab3 = QLabel('PyQt5!', self)
		lab3.move(55, 70)

		self.setGeometry(300, 300, 320, 120)
		self.setWindowTitle('绝对位置布局例子')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Example()
	demo.show()
	sys.exit(app.exec())

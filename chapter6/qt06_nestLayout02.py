import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setWindowTitle('嵌套布局示例')

		# 全局布局
		wwg = QWidget(self)

		wlayout = QHBoxLayout(wwg)

		hlayout = QHBoxLayout()
		vlayout = QVBoxLayout()
		glayout = QGridLayout()
		formlayout = QFormLayout()

		hlayout.addWidget(QPushButton(str(1)))
		hlayout.addWidget(QPushButton(str(2)))
		vlayout.addWidget(QPushButton(str(3)))
		vlayout.addWidget(QPushButton(str(4)))
		glayout.addWidget(QPushButton(str(5)), 0, 0)
		glayout.addWidget(QPushButton(str(6)), 0, 1)
		glayout.addWidget(QPushButton(str(7)), 1, 0)
		glayout.addWidget(QPushButton(str(8)), 1, 1)
		formlayout.addWidget(QPushButton(str(9)))
		formlayout.addWidget(QPushButton(str(10)))
		formlayout.addWidget(QPushButton(str(11)))
		formlayout.addWidget(QPushButton(str(12)))

		wlayout.addLayout(hlayout)
		wlayout.addLayout(vlayout)
		wlayout.addLayout(glayout)
		wlayout.addLayout(formlayout)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = MyWindow()
	form.show()
	sys.exit(app.exec())

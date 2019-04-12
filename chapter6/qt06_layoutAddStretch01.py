from PyQt5.QtWidgets import *
import sys


class WindowDemo(QWidget):
	def __init__(self):
		super(WindowDemo, self).__init__()

		btn1 = QPushButton(self)
		btn2 = QPushButton(self)
		btn3 = QPushButton(self)

		btn1.setText('button 1')
		btn2.setText('button 2')
		btn3.setText('button 3')

		hbox = QHBoxLayout()
		# 设置伸缩量1
		hbox.addStretch(1)
		hbox.addWidget(btn1)

		hbox.addStretch(1)
		hbox.addWidget(btn2)

		hbox.addStretch(1)
		hbox.addWidget(btn3)

		hbox.addStretch(1)

		self.setLayout(hbox)
		self.setWindowTitle('addStretch例子')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = WindowDemo()
	win.show()
	sys.exit(app.exec())

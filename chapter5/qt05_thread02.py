import sys
import timer

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec = 0

class WorkThread(QThread):
	trigger = pyqtSignal()
	def __init__(self):
		super(WorkThread, self).__init__()
	def run(self):
		for i in range(200000000):
			pass
		self.trigger.emit()

def setTime():
	global sec
	sec += 1
	lcdNumber.display(sec)


def work():
	timer.start(1000)
	workThread.start()
	workThread.trigger.connect(timeStop)
def timeStop():
	timer.stop()
	print('运行结束用时',lcdNumber.value())
	global sec
	sec = 0


if __name__ == '__main__':
	app = QApplication(sys.argv)
	top = QWidget()
	top.resize(300, 120)

	layout = QVBoxLayout(top)
	lcdNumber = QLCDNumber()
	layout.addWidget(lcdNumber)
	btn = QPushButton('测试')
	layout.addWidget(btn)

	timer = QTimer()
	workThread = WorkThread()
	timer.timeout.connect(setTime)
	btn.clicked.connect(work)

	top.show()
	sys.exit(app.exec())

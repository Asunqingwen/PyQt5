from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinForm(QWidget):
	def __init__(self, parent=None):
		super(WinForm, self).__init__(parent)
		self.setWindowTitle('QTimer demo')
		self.listFile = QListWidget()
		self.label = QLabel('显示当前时间')
		self.startBtn = QPushButton('开始')
		self.endBtn = QPushButton('结束')
		layout = QGridLayout(self)

		# 初始化定时器
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.showTime)

		layout.addWidget(self.label, 0, 0, 1, 2)
		layout.addWidget(self.startBtn, 1, 0)
		layout.addWidget(self.endBtn, 1, 1)

		self.startBtn.clicked.connect(self.startTimer)
		self.endBtn.clicked.connect(self.endTimer)

		self.setLayout(layout)

	def showTime(self):
		time = QDateTime.currentDateTime()
		timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
		self.label.setText(timeDisplay)

	def startTimer(self):
		self.timer.start(1000)
		self.startBtn.setEnabled(False)
		self.endBtn.setEnabled(True)

	def endTimer(self):
		self.timer.stop()
		self.startBtn.setEnabled(True)
		self.endBtn.setEnabled(False)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = WinForm()
	form.show()
	sys.exit(app.exec())

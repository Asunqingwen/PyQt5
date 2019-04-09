import sys

from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class FileDialogDemo(QWidget):
	def __init__(self, parent=None):
		super(FileDialogDemo, self).__init__(parent)
		self.setWindowTitle('File Dialog例子')
		layout = QVBoxLayout()
		self.setLayout(layout)

		self.btn = QPushButton('加载图片')
		self.btn.clicked.connect(self.getfile)
		self.le = QLabel("")
		layout.addWidget(self.btn)
		layout.addWidget(self.le)

		self.btn1 = QPushButton('加载文本文件')
		self.btn1.clicked.connect(self.getfiles)
		self.contents = QTextEdit()
		layout.addWidget(self.btn1)
		layout.addWidget(self.contents)

	def getfile(self):
		fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', 'Image files (*.jpg *.gif *.png)')
		self.le.setPixmap(QPixmap(fname))

	def getfiles(self):
		dlg = QFileDialog()
		dlg.setFileMode(QFileDialog.AnyFile)
		dlg.setFilter(QDir.Files)

		if dlg.exec():
			filenames = dlg.selectedFiles()
			f = open(filenames[0], 'r')

			with f:
				data = f.read()
				self.contents.setText(data)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	myshow = FileDialogDemo()
	myshow.show()
	sys.exit(app.exec())

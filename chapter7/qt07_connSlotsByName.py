from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class CustWidget(QWidget):
	def __init__(self, parent=None):
		super(CustWidget, self).__init__(parent)

		self.okButton = QPushButton('OK', self)
		# 使用setObjectName设置对象名称
		self.okButton.setObjectName('okButton')
		layout = QHBoxLayout()
		layout.addWidget(self.okButton)
		QtCore.QMetaObject.connectSlotsByName(self)

	@pyqtSlot()
	def on_okButton_clicked(self):
		print('单击了OK按钮')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = CustWidget()
	form.show()
	sys.exit(app.exec())

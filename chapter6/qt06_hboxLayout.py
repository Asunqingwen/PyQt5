import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class Winform(QWidget):
	def __init__(self, parent=None):
		super(Winform, self).__init__(parent)
		self.setWindowTitle('水平布局管理例子')

		# 水平布局按照从左到右的顺序添加按钮控件
		hlayout = QHBoxLayout()
		# hlayout.addWidget(QPushButton(str(1)))
		# hlayout.addWidget(QPushButton(str(2)))
		# hlayout.addWidget(QPushButton(str(3)))
		# hlayout.addWidget(QPushButton(str(4)))
		# hlayout.addWidget(QPushButton(str(5)))
		# 水平居左，垂直靠上对齐
		hlayout.addWidget(QPushButton(str(1)), 0, Qt.AlignTop)
		hlayout.addWidget(QPushButton(str(2)), 0, Qt.AlignLeft | Qt.AlignTop)
		hlayout.addWidget(QPushButton(str(3)))

		# 水平居左，垂直靠下对齐
		hlayout.addWidget(QPushButton(str(4)), 0, Qt.AlignLeft | Qt.AlignBottom)
		hlayout.addWidget(QPushButton(str(5)), 0, Qt.AlignLeft | Qt.AlignBottom)
		# 设置控件间距
		# hlayout.setSpacing(14)

		self.setLayout(hlayout)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Winform()
	demo.show()
	sys.exit(app.exec())

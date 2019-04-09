import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QWidget()
	lab1 = QLabel()
	lab1.setPixmap(QPixmap('./images/python.jpg'))
	vbox = QVBoxLayout()
	vbox.addWidget(lab1)
	win.setWindowTitle('QPixmap例子')
	win.setLayout(vbox)
	win.show()
	sys.exit(app.exec())

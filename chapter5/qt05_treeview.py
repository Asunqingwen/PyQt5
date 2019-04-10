import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
	app = QApplication(sys.argv)
	model = QDirModel()
	tree = QTreeView()
	tree.setModel(model)
	tree.setWindowTitle('QTreeView例子')
	tree.resize(640, 480)
	tree.show()
	sys.exit(app.exec())

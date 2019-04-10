import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class treeWidgetDemo(QMainWindow):
	def __init__(self, parent=None):
		super(treeWidgetDemo, self).__init__(parent)
		self.setWindowTitle('TreeWidget例子')
		layout = QVBoxLayout()
		self.tree = QTreeWidget()
		self.tree.setColumnCount(2)
		self.tree.setHeaderLabels(['Key', 'Value'])

		root = QTreeWidgetItem(self.tree)
		root.setText(0, 'root')
		root.setIcon(0, QIcon('./images/roog.png'))
		self.tree.setColumnWidth(0, 160)

		child1 = QTreeWidgetItem(root)
		child1.setText(0, 'child1')
		child1.setText(1, 'IOS')
		child1.setIcon(0, QIcon('./images/IOS.png'))

		child2 = QTreeWidgetItem(child1)
		child2.setText(0, 'child2')
		child2.setText(1, 'Android')
		child2.setIcon(0, QIcon('./images/android.png'))

		child3 = QTreeWidgetItem(child2)
		child3.setText(0, 'child3')
		child3.setText(1, 'music')
		child3.setIcon(0, QIcon('./images/music.png'))

		self.tree.addTopLevelItem(root)
		self.tree.expandAll()
		self.setCentralWidget(self.tree)
		layout.addWidget(self.tree)
		self.setLayout(layout)

		self.tree.clicked.connect(self.onTreeClicked)

	def onTreeClicked(self, qmodelindex):
		item = self.tree.currentItem()
		print('key=%s,value=%s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = treeWidgetDemo()
	demo.show()
	sys.exit(app.exec())

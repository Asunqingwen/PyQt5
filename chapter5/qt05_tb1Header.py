import sys
from PyQt5.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QHeaderView, \
	QAbstractItemView


class Table(QWidget):
	def __init__(self):
		super(Table, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('QTableWidget例子')
		self.resize(400, 300)
		conLayout = QHBoxLayout()
		tableWidget = QTableWidget()
		tableWidget.setRowCount(4)
		tableWidget.setColumnCount(3)
		conLayout.addWidget(tableWidget)
		tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
		# tableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])
		# tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		# tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		# tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

		# tableWidget.resizeColumnsToContents()
		# tableWidget.resizeRowsToContents()
		# tableWidget.verticalHeader().setVisible(False)

		newItem = QTableWidgetItem('张三')
		tableWidget.setItem(0, 0, newItem)

		newItem = QTableWidgetItem('男')
		tableWidget.setItem(0, 1, newItem)

		newItem = QTableWidgetItem('160')
		tableWidget.setItem(0, 2, newItem)

		self.setLayout(conLayout)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	table = Table()
	table.show()
	sys.exit(app.exec())

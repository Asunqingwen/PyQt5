import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.setWindowTitle('设置窗口样式例子')
        # 设置无边框窗口样式
        self.setWindowFlags(Qt.FramelessWindowHint)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgetApp = MainWindow()
    widgetApp.show()
    sys.exit(app.exec())

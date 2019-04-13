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

        #为了便于显示，设置窗口背景颜色(采用QSS)
        self.setStyleSheet('''background-color:blue;''')
    def showMaximized(self):
        #最大化窗口
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgetApp = MainWindow()
    widgetApp.showMaximized()
    sys.exit(app.exec())

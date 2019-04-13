from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()
        self.setWindowTitle('paintEvent设置背景色')

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setBrush(Qt.black)
        painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec())

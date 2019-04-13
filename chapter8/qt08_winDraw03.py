import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle('双缓冲绘图例子')

        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()

        # 辅助画布
        self.tempPix = QPixmap()
        # 标志是否正在绘图
        self.isDrawing = False
        self.initUI()

    def initUI(self):
        self.resize(600, 500)
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x() - x
        h = self.endPoint.y() - y
        if self.isDrawing:
            # 将以前pix中的内容复制到tempPix中，保证以前的内容不消失
            self.tempPix = self.pix
            pp = QPainter(self.tempPix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.pix)
        else:
            pp = QPainter(self.pix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            self.isDrawing = True

    def mouseReleaseEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()
            self.isDrawing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgetApp = Winform()
    widgetApp.show()
    sys.exit(app.exec())

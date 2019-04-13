from PyQt5.QtWidgets import *
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()
        self.initUI()

    def initUI(self):
        combo = QComboBox(self)
        combo.setObjectName('myQComboBox')
        combo.addItem('Window')
        combo.addItem('Ubuntu')
        combo.addItem('RedHat')
        combo.move(50, 50)
        self.setGeometry(250, 200, 320, 150)
        self.setWindowTitle('QComboBox样式')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    qssStyle = '''
            QComboBox#myQComboBox::drop-down{
                image:url(./images/open.png)
            }
    '''
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec())

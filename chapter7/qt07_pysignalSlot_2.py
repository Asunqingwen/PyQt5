from PyQt5.QtCore import *


# 信号对象
class QTypeSignal(QObject):
	# 定义一个信号
	sendmsg = pyqtSignal(str,str)

	def __init__(self):
		super(QTypeSignal, self).__init__()

	def run(self):
		# 发射信号
		# self.sendmsg.emit('Hello Pyqt5')
		self.sendmsg.emit('第一个参数', '第二个参数')


# 槽对象
class QTypeSlot(QObject):
	def __init__(self):
		super(QTypeSlot, self).__init__()

	# 槽对象中的槽函数
	def get(self, msg1, msg2):
		# print('QSlot get msg =>' + msg)
		print('QSlot get msg =>' + msg1 + ' ' + msg2)


if __name__ == '__main__':
	send = QTypeSignal()
	slot = QTypeSlot()

	print('---把信号绑定到槽函数上---')
	send.sendmsg.connect(slot.get)
	send.run()

	print('---把信号与槽函数的连接断开---')
	send.sendmsg.disconnect(slot.get)
	send.run()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWinSignalSlot02.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(801, 699)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 301))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 351, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberSpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.horizontalLayout.addWidget(self.numberSpinBox)
        self.styleCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.styleCombo.setObjectName("styleCombo")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.horizontalLayout.addWidget(self.styleCombo)
        self.printButton = QtWidgets.QPushButton(self.layoutWidget)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 70, 154, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewStatus = QtWidgets.QCheckBox(self.layoutWidget1)
        self.previewStatus.setObjectName("previewStatus")
        self.horizontalLayout_2.addWidget(self.previewStatus)
        self.previewButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 10, 361, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.resultLabel = QtWidgets.QLabel(self.groupBox_2)
        self.resultLabel.setGeometry(QtCore.QRect(130, 120, 54, 12))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "打印控制"))
        self.label_2.setText(_translate("Form", "纸张类型:"))
        self.label.setText(_translate("Form", "打印份数:"))
        self.styleCombo.setItemText(0, _translate("Form", "A4"))
        self.styleCombo.setItemText(1, _translate("Form", "A3"))
        self.styleCombo.setItemText(2, _translate("Form", "A5"))
        self.printButton.setText(_translate("Form", "打印"))
        self.previewStatus.setText(_translate("Form", "全屏预览"))
        self.previewButton.setText(_translate("Form", "预览"))
        self.groupBox_2.setTitle(_translate("Form", "操作结果"))
        self.resultLabel.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))


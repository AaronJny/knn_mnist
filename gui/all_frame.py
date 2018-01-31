# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_frame.ui'
#
# Created: Tue Jan 30 19:59:37 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 483)
        self.tip_label_1 = QtWidgets.QLabel(Form)
        self.tip_label_1.setGeometry(QtCore.QRect(50, 10, 351, 41))
        self.tip_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.tip_label_1.setScaledContents(False)
        self.tip_label_1.setWordWrap(True)
        self.tip_label_1.setObjectName("tip_label_1")
        self.cnt_label = QtWidgets.QLabel(Form)
        self.cnt_label.setGeometry(QtCore.QRect(0, 60, 421, 41))
        self.cnt_label.setTextFormat(QtCore.Qt.AutoText)
        self.cnt_label.setScaledContents(False)
        self.cnt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cnt_label.setWordWrap(True)
        self.cnt_label.setObjectName("cnt_label")
        self.count_label = QtWidgets.QLabel(Form)
        self.count_label.setGeometry(QtCore.QRect(30, 150, 371, 311))
        self.count_label.setText("")
        self.count_label.setTextFormat(QtCore.Qt.AutoText)
        self.count_label.setScaledContents(False)
        self.count_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.count_label.setWordWrap(True)
        self.count_label.setObjectName("count_label")
        self.tip_label_2 = QtWidgets.QLabel(Form)
        self.tip_label_2.setGeometry(QtCore.QRect(30, 110, 231, 31))
        self.tip_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.tip_label_2.setScaledContents(False)
        self.tip_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tip_label_2.setWordWrap(True)
        self.tip_label_2.setObjectName("tip_label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "验证全部数据"))
        self.tip_label_1.setText(_translate("Form", "  数据集较大，花费时间较长，请耐心等待..."))
        self.cnt_label.setText(_translate("Form", "获取数据中..."))
        self.tip_label_2.setText(_translate("Form", "统计数据："))


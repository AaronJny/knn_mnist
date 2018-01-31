# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_frame.ui'
#
# Created: Tue Jan 30 19:59:48 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 80)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.write_btn = QtWidgets.QPushButton(self.centralwidget)
        self.write_btn.setGeometry(QtCore.QRect(310, 10, 141, 61))
        self.write_btn.setObjectName("write_btn")
        self.random_btn = QtWidgets.QPushButton(self.centralwidget)
        self.random_btn.setGeometry(QtCore.QRect(160, 10, 141, 61))
        self.random_btn.setObjectName("random_btn")
        self.all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.all_btn.setGeometry(QtCore.QRect(10, 10, 141, 61))
        self.all_btn.setObjectName("all_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.all_btn.clicked.connect(MainWindow.all_btn_clicked)
        self.random_btn.clicked.connect(MainWindow.random_btn_clicked)
        self.write_btn.clicked.connect(MainWindow.write_btn_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于KNN和bgging算法的数字识别"))
        self.write_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>手写一个数字，进行识别</p></body></html>"))
        self.write_btn.setText(_translate("MainWindow", "手写验证"))
        self.random_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>随机运行一部分测试数据，可以指定测试数据数目</p></body></html>"))
        self.random_btn.setText(_translate("MainWindow", "随机验证"))
        self.all_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>运行全部测试数据</p></body></html>"))
        self.all_btn.setText(_translate("MainWindow", "全部验证"))


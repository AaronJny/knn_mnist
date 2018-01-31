# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'random_frame.ui'
#
# Created: Tue Jan 30 20:03:41 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_second_form(object):
    def setupUi(self, second_form):
        second_form.setObjectName("second_form")
        second_form.resize(1161, 676)
        second_form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line = QtWidgets.QFrame(second_form)
        self.line.setGeometry(QtCore.QRect(510, 0, 20, 681))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(second_form)
        self.line_2.setGeometry(QtCore.QRect(820, 0, 20, 681))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.img_matrix_label = QtWidgets.QLabel(second_form)
        self.img_matrix_label.setGeometry(QtCore.QRect(0, 0, 521, 541))
        self.img_matrix_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.img_matrix_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.img_matrix_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_matrix_label.setObjectName("img_matrix_label")
        self.line_3 = QtWidgets.QFrame(second_form)
        self.line_3.setGeometry(QtCore.QRect(0, 530, 521, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.finnal_label = QtWidgets.QLabel(second_form)
        self.finnal_label.setGeometry(QtCore.QRect(1, 534, 521, 141))
        self.finnal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.finnal_label.setObjectName("finnal_label")
        self.bagging_label = QtWidgets.QLabel(second_form)
        self.bagging_label.setGeometry(QtCore.QRect(520, 80, 311, 271))
        self.bagging_label.setText("")
        self.bagging_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bagging_label.setObjectName("bagging_label")
        self.knn_label = QtWidgets.QLabel(second_form)
        self.knn_label.setGeometry(QtCore.QRect(850, 60, 291, 611))
        self.knn_label.setText("")
        self.knn_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.knn_label.setObjectName("knn_label")
        self.line_4 = QtWidgets.QFrame(second_form)
        self.line_4.setGeometry(QtCore.QRect(520, 370, 311, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.count_label = QtWidgets.QLabel(second_form)
        self.count_label.setGeometry(QtCore.QRect(520, 430, 311, 231))
        self.count_label.setText("")
        self.count_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.count_label.setObjectName("count_label")
        self.bagging_label_2 = QtWidgets.QLabel(second_form)
        self.bagging_label_2.setGeometry(QtCore.QRect(520, 20, 311, 21))
        self.bagging_label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bagging_label_2.setObjectName("bagging_label_2")
        self.count_label_2 = QtWidgets.QLabel(second_form)
        self.count_label_2.setGeometry(QtCore.QRect(520, 400, 311, 31))
        self.count_label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.count_label_2.setObjectName("count_label_2")
        self.bagging_label_3 = QtWidgets.QLabel(second_form)
        self.bagging_label_3.setGeometry(QtCore.QRect(850, 20, 291, 21))
        self.bagging_label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bagging_label_3.setObjectName("bagging_label_3")

        self.retranslateUi(second_form)
        QtCore.QMetaObject.connectSlotsByName(second_form)

    def retranslateUi(self, second_form):
        _translate = QtCore.QCoreApplication.translate
        second_form.setWindowTitle(_translate("second_form", "随机识别程序"))
        self.img_matrix_label.setToolTip(_translate("second_form", "用以显示当前识别的数字的像素矩阵"))
        self.img_matrix_label.setText(_translate("second_form", "数字像素矩阵展示"))
        self.finnal_label.setToolTip(_translate("second_form", "<html><head/><body><p>用以展示当前数字的正确标签</p></body></html>"))
        self.finnal_label.setText(_translate("second_form", "数字标签展示"))
        self.bagging_label.setToolTip(_translate("second_form", "<html><head/><body><p>用以展示bugging算法识别的过程数据及结果</p></body></html>"))
        self.knn_label.setToolTip(_translate("second_form", "<html><head/><body><p>用以展示knn算法的识别过程</p></body></html>"))
        self.count_label.setToolTip(_translate("second_form", "<html><head/><body><p>用以展示算法正确率的相关统计数据</p></body></html>"))
        self.bagging_label_2.setToolTip(_translate("second_form", "<html><head/><body><p>用以展示bugging算法识别的过程数据及结果</p></body></html>"))
        self.bagging_label_2.setText(_translate("second_form", "bagging算法识别过程"))
        self.count_label_2.setToolTip(_translate("second_form", "<html><head/><body><p>用以展示算法正确率的相关统计数据</p></body></html>"))
        self.count_label_2.setText(_translate("second_form", "统计数据"))
        self.bagging_label_3.setToolTip(_translate("second_form", "<html><head/><body><p>用以展示bugging算法识别的过程数据及结果</p></body></html>"))
        self.bagging_label_3.setText(_translate("second_form", "knn算法识别过程"))


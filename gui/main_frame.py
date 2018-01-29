# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import PyQt5
from PyQt5 import QtWidgets
import settings
import utils
from algorithm import bagging, knn
from all_frame import *


class MainFrame(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(500, 150)
        self.setWindowTitle(u'基于Bagging算法和KNN算法的数字识别')
        main_ground=QtWidgets.QWidget()
        self.setCentralWidget(main_ground)
        grid=QtWidgets.QGridLayout()
        QtWidgets.QPushButton()
        all_button=QtWidgets.QPushButton(u'全部测试')
        all_button.setToolTip(u'运行全部测试数据')
        all_button.clicked.connect(self.all_button_clicked)
        random_button=QtWidgets.QPushButton(u'随机测试')
        random_button.setToolTip(u'随机运行一部分测试数据，可以指定测试数据数目')
        random_button.clicked.connect(self.random_button_clicked)
        write_button=QtWidgets.QPushButton(u'手写测试')
        write_button.setToolTip(u'手写一个数字，进行识别')
        grid.addWidget(all_button)
        grid.addWidget(random_button)
        grid.addWidget(write_button)
        main_ground.setLayout(grid)


    def closeEvent(self, QCloseEvent):
        """
        重写关闭事件
        :param QCloseEvent:
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self, u'确认退出', u'确定要退出吗？', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply==QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


    def all_button_clicked(self):
        self.all_frame=All_Frame()

    def random_button_clicked(self):
        self.random_frame=Random_Frame()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_frame = MainFrame()
    main_frame.show()
    sys.exit(app.exec_())

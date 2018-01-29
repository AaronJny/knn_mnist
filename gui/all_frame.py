#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import utils
import settings
from algorithm import bagging
from algorithm import knn
from PyQt5 import QtWidgets


class All_Frame(QtWidgets.QWidget):

    def __init__(self,parent=None):
        super(All_Frame,self).__init__(parent)
        self.resize(1000,800)
        self.show()

    def run_classify(self):
        bagginger=bagging.Bagging()
        bagginger.run(test_num=-1)


class Random_Frame(QtWidgets.QWidget):

    def __init__(self,parent=None):
        super(Random_Frame,self).__init__(parent)
        self.resize(1000,800)
        self.show()
        while True:
            text,ok=QtWidgets.QInputDialog.getText(self,u'设置测试数据数目',u'设置一个数目，程序将随机选取指定数目的测试数据')
            if ok:
                try:
                    test_num=int(text)
                    break
                except:
                    continue
            else:
                self.close()
                break


    def run_classify(self):
        bagginger=bagging.Bagging()
        bagginger.run(test_num=-1)
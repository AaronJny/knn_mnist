#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from PyQt5 import QtCore,QtGui
import time
from algorithm.bagging2 import Bagging

class RandomClassifyThread(QtCore.QThread):

    def __init__(self,frame,test_num,parent=None):
        super(RandomClassifyThread,self).__init__(parent)
        self.frame=frame
        self.test_num=test_num

    def run(self):
        baggingner = Bagging()
        baggingner.classify_random(self.frame, test_num=self.test_num)


class AllClassifyThread(QtCore.QThread):

    def __init__(self,frame,parent=None):
        super(AllClassifyThread,self).__init__(parent)
        self.frame=frame

    def run(self):
        baggingner=Bagging()
        baggingner.classify_all(self.frame)


class WriteClassifyThread(QtCore.QThread):

    def __init__(self,frame,filename,parent=None):
        super(WriteClassifyThread,self).__init__(parent)
        self.frame=frame
        self.filename=filename

    def run(self):
        baggingner=Bagging()
        baggingner.classify_write(self.frame,self.filename)
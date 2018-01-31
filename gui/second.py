# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from gui.random_frame import Ui_second_form as random_form
from gui.all_frame import Ui_Form as all_form
from gui.write_frame import Ui_second_form as write_form
from PyQt5 import QtWidgets


class RandomFrame(QtWidgets.QWidget, random_form):
    def __init__(self):
        super(RandomFrame, self).__init__()
        self.setupUi(self)
        self.show()
        # 获取要验证的测试数据的数目
        text = self.get_test_num()
        # 进行验证
        self.classify(int(text))

    def get_test_num(self):
        """
        读取用户输入的测试数据数目
        :return: 测试数据数目
        """
        test_num = 0
        while True:
            text, ok = QtWidgets.QInputDialog.getText(self, u'设置测试数据数目', u'设置一个数目，程序将随机选取指定数目的测试数据')
            if ok:
                try:
                    test_num = int(text)
                    break
                except:
                    continue
            else:
                self.close()
                break
        return test_num

    def classify(self, test_num):
        """
        对测试数据进行验证
        :param test_num: 测试数据的数目
        :return:
        """
        from gui.threads import RandomClassifyThread
        # 创建线程
        self.rct = RandomClassifyThread(self, test_num)
        # 启动线程
        self.rct.start()


class AllFrame(QtWidgets.QWidget, all_form):
    def __init__(self):
        super(AllFrame, self).__init__()
        self.setupUi(self)
        self.show()
        self.classify()

    def classify(self):
        from gui.threads import AllClassifyThread
        self.act = AllClassifyThread(self)
        self.act.start()


class WriteFrame(QtWidgets.QWidget, write_form):
    def __init__(self, filename):
        super(WriteFrame, self).__init__()
        self.setupUi(self)
        self.show()
        self.filename = filename
        self.classify()

    def classify(self):
        from gui.threads import WriteClassifyThread
        self.wct = WriteClassifyThread(self, self.filename)
        self.wct.start()

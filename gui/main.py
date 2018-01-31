# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from gui.main_frame import Ui_MainWindow
from PyQt5 import QtWidgets
from gui.second import RandomFrame, AllFrame, WriteFrame


class MainFrame(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        初始化信息
        """
        super(MainFrame, self).__init__()
        self.setupUi(self)

    def all_btn_clicked(self):
        """
        验证所有测试数据
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self, u'确认执行', u'全部测试集非常大，将耗时100分钟，您确定要继续吗？', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.all_frame = AllFrame()

    def random_btn_clicked(self):
        """
        验证指定数量的随机测试数据
        :return:
        """
        self.random_frame = RandomFrame()

    def write_btn_clicked(self):
        """
        验证人工手写的数字识别情况
        :return:
        """
        filename = QtWidgets.QFileDialog.getOpenFileName(self, u'打开文件', r"C:\Users\Administrator\Desktop/")[0]
        self.write_frame = WriteFrame(filename)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_frame = MainFrame()
    main_frame.show()
    sys.exit(app.exec_())

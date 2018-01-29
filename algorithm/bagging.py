# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from  knn import KNNClassify
import settings
import utils
import numpy as np
from random import randint
import time
from multiprocessing import Pool


class Bagging(object):
    def __init__(self):
        """
        初始化参数
        """
        # 是否打印过程信息
        self.print_info = False
        # 配置使用分类器的数量
        self.knn_num = settings.CLASSIFY_NUM
        # 测试总次数
        self.total_cnt = 0
        # 测试正确次数
        self.true_cnt = 0
        # 获取logger
        self.logger_string = u''
        # 训练数据
        self.train_data = self.read_train_data()
        # 测试数据
        self.test_data, self.test_labels = self.read_test_data()
        # knn分类器列表
        self.knn_list = self.create_knn_list()
        # 进行测试
        self.run()

    def read_train_data(self):
        """
        读取训练数据及其标签
        :return:
        """
        data, labels = utils.load_mnist(path='dataset', kind='train')
        lenth = len(labels)
        train_data = {}
        for i in range(10):
            train_data[i] = []
        for i in range(lenth):
            train_data[labels[i]].append(data[i])
        for i in range(10):
            train_data[i] = np.array(train_data[i])
        return train_data

    def read_test_data(self):
        """
        读取测试数据及其标签
        :return:
        """
        data, labels = utils.load_mnist(path='dataset', kind='t10k')
        return data, labels

    def print_log(self, msg):
        """
        记录并输出日志信息
        :param msg:
        :return:
        """
        self.logger_string += utils.print_log(msg)

    def create_knn_list(self):
        """
        运行bugging算法进行分类
        :return:
        """
        # knn分类器的列表，初始为空
        knn_list = []
        # 创建knn_num个knn分类器，加入到列表中
        for i in range(self.knn_num):
            # 对第i个分类器的数据集进行初始化
            train_data = None
            train_labels = None
            # 对0-9的数据集进行评分
            for j in range(10):
                # 每个分类器应拿到num个标签为j的数据
                num = len(self.train_data[j]) / self.knn_num
                tmp_data = self.train_data[j][i * num:i * num + num]
                # 将该分类器的0-9的数据集整合到一起
                if train_data is None:
                    train_data = np.zeros(shape=tmp_data.shape, dtype=np.float32)
                    train_labels = np.zeros(shape=(num, 1), dtype=np.int8)
                    train_data += tmp_data
                    train_labels += j
                else:
                    train_data = np.row_stack((train_data, tmp_data))
                    tmp_labels = np.zeros(shape=(num, 1), dtype=np.int8) + j
                    train_labels = np.row_stack((train_labels, tmp_labels))
                    # print '-' * 60
                    # print i, j, train_data.shape, train_labels.shape
            knner = KNNClassify(train_data, train_labels)
            knn_list.append(knner)
        return knn_list

    def create_test_img_set(self, test_num=-1):
        """
        创建用于测试的数据集
        :param test_num: 测试集大小 为-1则使用所有测试数据
        :return:
        """
        if test_num == -1 or test_num > 9999:
            return self.test_data, self.test_labels
        else:
            rand_num = randint(0, len(self.test_data) - test_num)
            return self.test_data[rand_num:rand_num + test_num], self.test_labels[rand_num:rand_num + test_num]

    def run(self):
        """
        使用bagging算法验证测试数据
        :return:
        """
        tic = time.time()
        # 初始化测试次数
        self.total_cnt = 0
        self.true_cnt = 0
        # 获取测试数据集
        test_data, test_labels = self.create_test_img_set(10000)
        # 计算测试数据集大小
        lenth = len(test_data)
        # 对测试数据集中的所有数据逐一进行计算
        for i in range(lenth):
            if i % 100 == 0:
                self.print_log(u'正在处理第{}张图片...'.format(i))
            if self.print_info:
                self.print_log(u'第{}张图片识别结果：\n'.format(i))
            kind_probability = np.array([0 for x in range(10)], dtype=np.float32)
            # 每个knn分类器分别进行分类，并返回最终结果
            for x in range(len(self.knn_list)):
                tmp_kind = self.knn_list[x].classify(test_data[i], test_labels[i], knn_bh=x)
                kind_probability[tmp_kind] += 1
            # 计算最终概率
            kind_probability = kind_probability / self.knn_num
            final_kind = -1
            final_probability = -1
            for x in range(len(kind_probability)):
                if kind_probability[x] > final_probability:
                    final_probability = kind_probability[x]
                    final_kind = x
            classify_true = final_kind == test_labels[i]
            # 记录测试结果
            self.total_cnt += 1
            if classify_true:
                self.true_cnt += 1
            # 输出结果
            if self.print_info:
                output = ''
                for x in range(10):
                    if kind_probability[x] != 0:
                        self.print_log(u'数字{}的概率为{:.2f}%\n'.format(x, kind_probability[x] * 100))
                self.print_log(u'最终识别结果为{},概率为{:.2f}%,正确答案为{}\n'.format(final_kind, kind_probability[final_kind] * 100,
                                                                        test_labels[i]))
                self.print_log(u'是否识别正确：{}'.format(classify_true))
                self.print_log(u'{}'.format('-' * 80))
        # output = '\n\n'
        for x in range(len(self.knn_list)):
            knner = self.knn_list[x]
            self.print_log(u'{}号knn分类器共识别{}次，正确{}次，正确率{:.2f}%'.format(x, knner.total_cnt, knner.true_cnt,
                                                                      knner.true_cnt * 100.0 / knner.total_cnt))
        self.print_log(u'Bagging算法共识别{}次，正确{}次，正确率{:.2f}%'.format(self.total_cnt, self.true_cnt,
                                                                  self.true_cnt * 100.0 / self.total_cnt))
        # self.logger.info(u'{}'.format(output))
        toc = time.time()
        print tic, toc, (toc - tic) * 1.0 / 60


if __name__ == '__main__':
    Bagging()

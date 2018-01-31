# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from  knn2 import KNNClassify
import settings
import utils
import numpy as np
from random import randint
import time


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

    def read_train_data(self):
        """
        读取训练数据及其标签
        :return:
        """
        data, labels = utils.load_mnist(path='../dataset', kind='train')
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
        data, labels = utils.load_mnist(path='../dataset', kind='t10k')
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
        创建knn_num个knn分类器，分别为它们分配训练数据，加入到knn_list列表中
        :return:存储这些Knn分类器的列表
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
            knner = KNNClassify(train_data, train_labels)
            knn_list.append(knner)
        return knn_list

    def create_test_img_set(self, test_num=-1):
        """
        创建用于测试的数据集
        :param test_num: 测试集大小 为-1则使用所有测试数据
        :return:
        """
        if test_num == -1 or test_num > 9999:  # 分配全部测试数据
            return self.test_data, self.test_labels
        else:  # 分配指定数量的测试数据
            rand_num = randint(0, len(self.test_data) - test_num)
            return self.test_data[rand_num:rand_num + test_num], self.test_labels[rand_num:rand_num + test_num]

    def get_img_matrix(self, img):
        """
        根据传入的图像信息，转化出其数字像素矩阵
        :param img: 1*784的图像灰度矩阵
        :return: 图像像素矩阵
        """
        output = u'当前数字像素矩阵：\n'
        for i in range(len(img)):
            if i % 28 == 0:
                output += u'\n'
            if img[i] == 0:
                output += u'- '
            else:
                output += u'* '
        output += '\n'
        return output

    def classify_random(self, frame, test_num=50):
        """
        使用bagging算法验证测试数据
        对应于GUI中的验证指定数量的随机测试数据功能
        :return:
        """
        # 初始化测试次数
        self.total_cnt = 0
        self.true_cnt = 0
        # 获取测试数据集
        self.tmp_test_data, self.tmp_test_labels = self.create_test_img_set(test_num)
        # 计算测试数据集大小
        lenth = len(self.tmp_test_data)
        # 对测试数据集中的所有数据逐一进行计算
        for i in range(lenth):
            frame.img_matrix_label.setText(self.get_img_matrix(self.tmp_test_data[i]))
            frame.finnal_label.setText(u'当前图片的正确标签为：{}'.format(self.tmp_test_labels[i]))
            frame.knn_label.setText(u'')
            kind_probability = np.array([0 for x in range(10)], dtype=np.float32)
            # 每个knn分类器分别进行分类，并返回最终结果
            output = u''
            for x in range(len(self.knn_list)):
                tmp_kind, knn_output = self.knn_list[x].classify(self.tmp_test_data[i], self.tmp_test_labels[i],
                                                                 knn_bh=x)
                kind_probability[tmp_kind] += 1
                output += u'knn分类器{}号认为，当前数字为{}\n'.format(x, tmp_kind)
                frame.knn_label.setText(frame.knn_label.text() + knn_output)
                frame.bagging_label.setText(output)
            # 计算最终概率
            kind_probability = kind_probability / self.knn_num
            final_kind = -1
            final_probability = -1
            for x in range(len(kind_probability)):
                if kind_probability[x] > final_probability:
                    final_probability = kind_probability[x]
                    final_kind = x
            classify_true = final_kind == self.tmp_test_labels[i]
            # 记录测试结果
            self.total_cnt += 1
            if classify_true:
                self.true_cnt += 1
            # 输出结果
            # if self.print_info:
            output = u'bagging算法认为，对于当前图像：\n\n'
            for x in range(10):
                if kind_probability[x] != 0:
                    output += u'是数字{}的概率为{:.2f}%\n'.format(x, kind_probability[x] * 100)
            output += (u'\n最终识别结果为{},概率为{:.2f}%\n\n'.format(final_kind, kind_probability[final_kind] * 100))
            output += (u'是否识别正确：{}'.format(classify_true))
            frame.bagging_label.setText(frame.bagging_label.text() + u'\n\n' + output)
            output = u''
            for x in range(len(self.knn_list)):
                knner = self.knn_list[x]
                output += (u'{}号knn分类器:\n共识别{}次，正确{}次，正确率{:.2f}%\n\n'.format(x, knner.total_cnt, knner.true_cnt,
                                                                             knner.true_cnt * 100.0 / knner.total_cnt))
            output += (u'Bagging算法:\n共识别{}次，正确{}次，正确率{:.2f}%'.format(self.total_cnt, self.true_cnt,
                                                                     self.true_cnt * 100.0 / self.total_cnt))
            frame.count_label.setText(output)
            time.sleep(1)

    def get_data_by_filename(self, filename):
        """
        根据文件名获取数据
        用于获取真人手写数字图像的数据集
        :param filename:文件路径
        :return:文件路径对应的数据，标签
        """
        # 获取数据
        data = utils.deal_with_hand_write_img(filename)
        # 获取标签
        if '-' not in filename:
            r_index = filename.rindex('.')
        else:
            r_index = filename.rindex('-')
        l_index = filename.rindex('/')
        label = int(filename[l_index + 1:r_index])
        return data, [label, ]

    def classify_write(self, frame, filename):
        """
        使用bagging算法验证测试数据
        对应于GUI中的验证真人手写数字的功能
        :param frame:显示窗口
        :param filename:文件路径
        :return:
        """
        # 初始化测试次数
        self.total_cnt = 0
        self.true_cnt = 0
        # 获取测试数据集
        frame.img_matrix_label.setText(u'正在对输入图像进行预处理，请稍等...')
        self.tmp_test_data, self.tmp_test_labels = self.get_data_by_filename(filename)
        # 计算测试数据集大小
        lenth = len(self.tmp_test_data)
        # 对测试数据集中的所有数据逐一进行计算
        for i in range(lenth):
            frame.img_matrix_label.setText(self.get_img_matrix(self.tmp_test_data[i]))
            frame.finnal_label.setText(u'当前图片的正确标签为：{}'.format(self.tmp_test_labels[i]))
            frame.knn_label.setText(u'')
            kind_probability = np.array([0 for x in range(10)], dtype=np.float32)
            # 每个knn分类器分别进行分类，并返回最终结果
            output = u''
            for x in range(len(self.knn_list)):
                tmp_kind, knn_output = self.knn_list[x].classify(self.tmp_test_data[i], self.tmp_test_labels[i],
                                                                 knn_bh=x)
                kind_probability[tmp_kind] += 1
                output += u'knn分类器{}号认为，当前数字为{}\n'.format(x, tmp_kind)
                frame.knn_label.setText(frame.knn_label.text() + knn_output)
                frame.bagging_label.setText(output)
            # 计算最终概率
            kind_probability = kind_probability / self.knn_num
            final_kind = -1
            final_probability = -1
            for x in range(len(kind_probability)):
                if kind_probability[x] > final_probability:
                    final_probability = kind_probability[x]
                    final_kind = x
            classify_true = final_kind == self.tmp_test_labels[i]
            # 记录测试结果
            self.total_cnt += 1
            if classify_true:
                self.true_cnt += 1
            # 输出结果
            output = u'bagging算法认为，对于当前图像：\n\n'
            for x in range(10):
                if kind_probability[x] != 0:
                    output += u'是数字{}的概率为{:.2f}%\n'.format(x, kind_probability[x] * 100)
            output += (u'\n最终识别结果为{},概率为{:.2f}%\n\n'.format(final_kind, kind_probability[final_kind] * 100))
            output += (u'是否识别正确：{}'.format(classify_true))
            frame.bagging_label.setText(frame.bagging_label.text() + u'\n\n' + output)
            output = u''
            for x in range(len(self.knn_list)):
                knner = self.knn_list[x]
                output += (u'{}号knn分类器:\n共识别{}次，正确{}次，正确率{:.2f}%\n\n'.format(x, knner.total_cnt, knner.true_cnt,
                                                                             knner.true_cnt * 100.0 / knner.total_cnt))
            output += (u'Bagging算法:\n共识别{}次，正确{}次，正确率{:.2f}%'.format(self.total_cnt, self.true_cnt,
                                                                     self.true_cnt * 100.0 / self.total_cnt))
            frame.count_label.setText(output)
            time.sleep(1)

    def classify_all(self, frame):
        """
        使用bagging算法验证测试数据
        对应于GUI中验证全部测试数据的功能
        :param frame:显示窗口
        :return:
        """
        flash_times = 100
        test_num = -1
        # 初始化测试次数
        self.total_cnt = 0
        self.true_cnt = 0
        # 获取测试数据集
        self.tmp_test_data, self.tmp_test_labels = self.create_test_img_set(test_num)
        # 计算测试数据集大小
        lenth = len(self.tmp_test_data)
        # 对测试数据集中的所有数据逐一进行计算
        for i in range(lenth):
            i_1 = i + 1
            if i_1 % flash_times == 1:
                frame.cnt_label.setText(utils.print_log(u'正在处理第{}张图片...'.format(i_1)))
                # self.print_log(u'正在处理第{}张图片...'.format(i))
            kind_probability = np.array([0 for x in range(10)], dtype=np.float32)
            # 每个knn分类器分别进行分类，并返回最终结果
            for x in range(len(self.knn_list)):
                tmp_kind, knn_output = self.knn_list[x].classify(self.tmp_test_data[i], self.tmp_test_labels[i],
                                                                 knn_bh=x)
                kind_probability[tmp_kind] += 1
            # 计算最终概率
            kind_probability = kind_probability / self.knn_num
            final_kind = -1
            final_probability = -1
            for x in range(len(kind_probability)):
                if kind_probability[x] > final_probability:
                    final_probability = kind_probability[x]
                    final_kind = x
            classify_true = final_kind == self.tmp_test_labels[i]
            # 记录测试结果
            self.total_cnt += 1
            if classify_true:
                self.true_cnt += 1

            if i_1 % flash_times == 0:
                output = u''
                for x in range(len(self.knn_list)):
                    knner = self.knn_list[x]
                    output += (u'{}号knn分类器:\n共识别{}次，正确{}次，正确率{:.2f}%\n\n'.format(x, knner.total_cnt, knner.true_cnt,
                                                                                 knner.true_cnt * 100.0 / knner.total_cnt))
                output += (u'Bagging算法:\n共识别{}次，正确{}次，正确率{:.2f}%'.format(self.total_cnt, self.true_cnt,
                                                                         self.true_cnt * 100.0 / self.total_cnt))
                frame.count_label.setText(output)
        frame.cnt_label.setText(utils.print_log(u'验证完成'))
        output = u''
        for x in range(len(self.knn_list)):
            knner = self.knn_list[x]
            output += (u'{}号knn分类器:\n共识别{}次，正确{}次，正确率{:.2f}%\n\n'.format(x, knner.total_cnt, knner.true_cnt,
                                                                         knner.true_cnt * 100.0 / knner.total_cnt))
        output += (u'Bagging算法:\n共识别{}次，正确{}次，正确率{:.2f}%'.format(self.total_cnt, self.true_cnt,
                                                                 self.true_cnt * 100.0 / self.total_cnt))
        frame.count_label.setText(output)

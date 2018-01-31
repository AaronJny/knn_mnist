# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import numpy as np
import utils
import settings
import Queue


class KNNClassify(object):
    def __init__(self, train_data, train_labels, print_info=False):
        """
        初始化参数
        """
        self.print_info = print_info
        self.k_num = settings.KNN_PARAMS_K
        self.train_data = train_data
        self.labels = train_labels
        self.true_cnt = 0
        self.total_cnt = 0

    def read_train_data(self):
        """
        获取训练数据
        :return:
        """
        return np.matrix([])

    def get_k_minist_labels(self, dist_array):
        """
        获取距离最小的前k个标签
        :return:
        """
        # 创建一个优先队列
        que = Queue.PriorityQueue()
        # 找出最小的前K个样本的距离值和下标
        for i in range(len(dist_array)):
            if que.qsize() < self.k_num:
                que.put((-dist_array[i], i))
            else:
                val, pos = que.get()
                if dist_array[i] < -val:
                    que.put((-dist_array[i], i))
                else:
                    que.put((val, pos))
        # 根据队列得出最小的标签列表
        min_labels_list = []
        while not que.empty():
            val, pos = que.get()
            label = self.labels[pos]
            min_labels_list.append(label[0])
        return min_labels_list

    def classify(self, img_matrix, img_label, knn_bh=1):
        """
        对输入的图片进行分类进行分类
        :return:
        """
        # 求所有训练数据和输入的差值
        diff_matrix = self.train_data - img_matrix
        # 对差值求平方，算出所有距离的平方
        square_dist_matrix = diff_matrix ** 2
        # 对距离按行相加
        dist_sum = np.sum(square_dist_matrix, axis=1)
        # 对距离平方开根号
        dist = dist_sum ** 0.5
        # 得出距离最小的前K个标签列表
        min_labels = self.get_k_minist_labels(dist)
        # 计算当前图片分别属于10个数字的概率
        probability_array = np.array([0 for i in range(10)], dtype=np.float32)
        for i in min_labels:
            probability_array[i] += 1
        probability_array = probability_array / self.k_num
        # 决策出最终识别结果
        final_kind = -1
        final_probability = -1
        for i in range(len(probability_array)):
            if probability_array[i] > final_probability:
                final_probability = probability_array[i]
                final_kind = i
        # 记录本次识别结果
        self.total_cnt += 1
        if final_kind == img_label:
            self.true_cnt += 1
        output = u'knn分类器{}号认为：\n\n'.format(knn_bh)
        for x in range(len(probability_array)):
            if probability_array[x] != 0:
                output += u'数字{}的概率为{:.2f}%\n'.format(x, probability_array[x] * 100)
        output += u'\n最终识别结果为{},概率为{:.2f}%,识别{}\n\n\n'.format(final_kind, probability_array[final_kind] * 100,
                                                        u'正确' if final_kind == img_label else u'错误')
        return final_kind,output

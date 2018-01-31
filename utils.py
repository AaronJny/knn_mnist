# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import os
import struct
import numpy as np
import time
from PIL import Image


def load_mnist(path, kind='train'):
    """
    加载mnist数据集
    :param path: 数据文件存放路径
    :param kind: 数据种类
    :return: 数据矩阵，标签矩阵
    """
    # 生成路径
    labels_path = os.path.join(path,
                               '%s-labels.idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images.idx3-ubyte'
                               % kind)
    # 读取标签信息
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)
    # 读取图像矩阵
    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels


def print_log(msg):
    """
    格式化输出提示信息（加上时间提示）
    :param msg: 要输出的提示信息
    :return: 格式化后的信息
    """
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    msg = u'{} {}'.format(time_str, msg)
    # print msg
    return msg


def deal_with_hand_write_img(filename):
    """
    读取指定图片，并将其先灰度化，再转化为像素矩阵，并返回一个长度为1*784的矩阵
    :param filename:图片路径
    :return:1*784的矩阵
    """
    # 读取图片
    img = Image.open(filename)
    # 更改图片尺寸为28*28，与训练数据一致
    out = img.resize((28, 28), Image.ANTIALIAS)
    # 将图片灰度化
    out = out.convert('L')
    # 将灰度图转化为28*28的图像矩阵
    data = np.array(out)
    # 对矩阵的灰度值进行调整
    for i in range(28):
        for j in range(28):
            data[i][j] = 255 - data[i][j]
            if data[i][j] > 10:
                data[i][j] = 255
    # 将矩阵大小更改为1*784并返回
    return data.reshape((1, 784))


if __name__ == '__main__':
    print_log()

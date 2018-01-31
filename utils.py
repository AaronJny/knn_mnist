# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import os
import struct
import numpy as np
import logging
import io
import time
from PIL import Image


def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels.idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images.idx3-ubyte'
                               % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels


def print_log(msg):
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
    img = Image.open(filename)
    out = img.resize((28, 28), Image.ANTIALIAS)
    out = out.convert('L')
    data = np.array(out)
    for i in range(28):
        for j in range(28):
            data[i][j]=255-data[i][j]
            if data[i][j]>10:
                data[i][j]=255
    return data.reshape((1, 784))


if __name__ == '__main__':
    print_log()

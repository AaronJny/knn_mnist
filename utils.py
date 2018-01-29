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
    print msg
    return msg


if __name__ == '__main__':
    print_log()

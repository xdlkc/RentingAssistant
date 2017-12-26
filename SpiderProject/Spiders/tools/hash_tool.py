# coding=utf-8
__author__ = 'lkc'

import hashlib


def hash_str(s):
    """
    压缩长字符串
    :param s:
    :return:
    """
    md5 = hashlib.md5(s)
    return md5.hexdigest()

if __name__ == '__main__':
    print(hash_str('https://xa.lianjia.com/zufang/101102392753.html'))
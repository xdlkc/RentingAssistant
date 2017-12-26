# coding=utf-8
__author__ = 'lkc'
import psycopg2
import json
import os
import sys


def read_from_json():
    """
    配置postgres数据库
    :return:
    """
    with open(os.path.split(os.path.realpath(__file__))[0] + "/sql.json", "r") as f:
        conf = json.load(f)
    conn = psycopg2.connect(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'])
    return conn


if __name__ == '__main__':
    pass

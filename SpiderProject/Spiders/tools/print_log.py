# coding=utf-8
__author__ = 'lkc'

import logging
import os
import time

date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
dir = '{}/Spiders/logs'.format(os.getcwd())
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')

info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)
info_handler = logging.FileHandler('{}/infos/{}.log'.format(dir, date))
info_handler.setFormatter(formatter)
info_logger.addHandler(info_handler)

error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler('{}/errors/{}.log'.format(dir, date))
error_handler.setFormatter(formatter)
error_logger.addHandler(error_handler)

warning_logger = logging.getLogger('warning_logger')
warning_logger.setLevel(logging.WARNING)
warning_handler = logging.FileHandler('{}/warnings/{}.log'.format(dir, date))
warning_handler.setFormatter(formatter)
warning_logger.addHandler(warning_handler)


def get_error_logger():
    return error_logger


def get_info_logger():
    return info_logger

# coding=utf-8
__author__ = 'lkc'
from enum import Enum


class RentWayEnum(Enum):
    """
    租赁方式
    """
    ALL = 0
    SINGLE = 1


class SourceEnum(Enum):
    """
    房屋来源
    """
    # 58
    WB = '58'
    # 链家
    LJ = 'lj'
    # 自如
    ZR = 'zr'

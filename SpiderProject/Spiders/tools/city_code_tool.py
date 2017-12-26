# coding=utf-8
__author__ = 'lkc'
import json
import os
from ..tools.print_log import *


def search_city_code_by_name(city_name):
    try:
        f = os.getcwd() + '/Spiders/jsons/city.json'
        with open(f) as fi:
            data = json.load(fi)
            for d in data:
                if d['city_name'] == city_name:
                    return int(d['city_code'])
    except Exception as e:
        get_error_logger().error(e)
        return -1

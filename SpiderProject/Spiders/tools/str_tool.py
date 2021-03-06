# coding=utf-8
import re
import requests
from bs4 import BeautifulSoup

def replace_space(s):
    """
    去除所有空格，制表符
    :param s:
    :return:
    """
    return s.replace(
        '\r',
        '').replace(
        '\t',
        '').replace(
            '\n',
            '').replace(
                ' ',
        '').strip()


def extract_no(s):
    return re.findall(r'[0-9]*\.?[0-9]+', s)


def chinese_to_number(no):
    d = {
        '零': 0,
        '一': 1,
        '二': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9,
        '十': 10,
        '十一': 11,
        '十二': 12,
        '十三': 13,
        '十四': 14,
        '十五': 15}
    return d['no']

def build_bs(link):
    hea = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    html = requests.get(link, headers=hea).content
    return BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

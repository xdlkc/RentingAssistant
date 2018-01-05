# coding:utf-8
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    html = requests.get('http://www.ziroom.com/z/vr/60919477.html',headers=hea)
    print html.text
# coding:utf-8
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':

    html = requests.get('https://bj.lianjia.com/zufang/101102173916.html').content
    bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    container = bs.find('div', class_="content zf-content")
    zf_room = container.find('div', class_="zf-room").find_all('p')
    temp = zf_room[4].get_text()
    print temp
    
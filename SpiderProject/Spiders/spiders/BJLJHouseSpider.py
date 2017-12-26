# coding=utf-8
import scrapy
from ..items import HouseItem
from ..tools.str_tool import *
import re
from ..tools.hash_tool import *
from bs4 import BeautifulSoup
import requests
from ..enums import *
from ..tools.city_code_tool import *

class BJLJHouseSpider(scrapy.Spider):
    """
    链家网北京租房信息爬取
    """
    name = "ljbj"
    allowed_domains = ['https://bj.lianjia.com']
    start_urls = ["https://bj.lianjia.com/zufang/"]

    def __init__(self, **kwargs):
        super(BJLJHouseSpider, self).__init__(**kwargs)
        init_url = "https://bj.lianjia.com/zufang/"
        for i in range(2, 100, 1):
            self.start_urls.append(init_url + "pg" + str(i))

    def parse(self, response):
        house_list = response.xpath('//ul[@class="house-lst"]//li')
        items = []
        for house in house_list:
            item = HouseItem()
            house_info = house.xpath('.//div[@class="info-panel"]')
            item['title'] = replace_space(house_info.xpath('.//h2//a/text()')[0].extract())
            item['house_link'] = replace_space(house_info.xpath('.//h2//a/@href')[0].extract())
            item['hash_link'] = hash_str(item['house_link'])
            info_1 = house.xpath('.//div[@class="col-1"]')
            where = info_1.xpath('.//div[@class="where"]')
            temp = where.xpath('.//span[@class="meters"]/text()')[0].extract()
            item['meters'] = float(extract_no(temp)[0])
            info_2 = house.xpath('.//div[@class="col-2"]')
            item['people_sum'] = int(info_2.xpath('.//div[@class="square"]/div/span/text()')[0].extract())
            item['source'] = 'lj'
            item['city_code'] = search_city_code_by_name(u'北京市')

            html = requests.get(item['house_link']).content
            bs = BeautifulSoup(html,'html.parser', from_encoding='utf-8')
            container = bs.find('div',class_="content zf-content")
            item['price'] = int(container.find('div',class_="price ").find('span',class_="total").get_text())
            zf_room = container.find('div',class_="zf-room").find_all('p')
            temp = zf_room[1].get_text()
            item['detail'] = temp
            zone = extract_no(temp)
            if u'整租' in temp:
                item['rent_way'] = RentWayEnum.ALL.value
            else:
                item['rent_way'] = RentWayEnum.SINGLE.value
            item['bedroom'] = int(zone[0])
            item['living_room'] = int(zone[1])
            item['toilet'] = int(zone[2])
            temp = zf_room[4].get_text()
            temp = extract_no(temp)
            if len(temp) < 2:
                item['subway'] = -1
            else:
                item['subway'] = int(temp[0])
            item['village'] = zf_room[5].find('a').get_text()

            temp = zf_room[6].find_all('a')
            item['region_hi'] = temp[0].get_text()
            item['region_lo'] = temp[1].get_text()
            items.append(item)
        return items

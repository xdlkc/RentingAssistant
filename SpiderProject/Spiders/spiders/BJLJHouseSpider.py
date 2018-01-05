# coding=utf-8
import requests
import scrapy
from bs4 import BeautifulSoup

from ..enums import *
from ..items import HouseItem
from ..tools.city_code_tool import *
from ..tools.hash_tool import *
from ..tools.str_tool import *
from ..tools.print_log import *
import traceback
from ..sql.sql_config import *


class BJLJHouseSpider(scrapy.Spider):
    """
    链家网租房信息爬取
    """
    name = "lj"
    allowed_domains = [
        'https://bj.lianjia.com',
        'https://xa.lianjia.com/zufang/',
        'http://sh.lianjia.com/zufang/']
    start_urls = [
        "https://bj.lianjia.com/zufang/",
        'https://xa.lianjia.com/zufang',
        'http://sh.lianjia.com/zufang/d1rs',
        'https://sz.lianjia.com/zufang/']

    def __init__(self, **kwargs):
        super(BJLJHouseSpider, self).__init__(**kwargs)
        init_url = "https://bj.lianjia.com/zufang/"
        for i in range(2, 100, 1):
            self.start_urls.append(init_url + str(i))
        init_url = 'https://xa.lianjia.com/zufang/pg'
        for i in range(1, 76, 1):
            self.start_urls.append(init_url + str(i))
        init_url = 'http://sh.lianjia.com/zufang/d'
        for i in range(2, 100, 1):
            self.start_urls.append(init_url + str(i) + 'rs')
        init_url = 'https://sz.lianjia.com/zufang/pg'
        for i in range(2, 100, 1):
            self.start_urls.append(init_url + str(i))

    def parse(self, response):
        house_list = response.xpath('//ul[@class="house-lst"]//li')
        items = []
        for house in house_list:
            item = HouseItem()
            house_info = house.xpath('.//div[@class="info-panel"]')
            item['title'] = replace_space(
                house_info.xpath('.//h2//a/text()')[0].extract())
            item['house_link'] = replace_space(
                house_info.xpath('.//h2//a/@href')[0].extract())
            item['hash_link'] = hash_str(item['house_link'])
            if judge_link(item['hash_link']) is not None:
                continue
            try:
                city_name = response.xpath(
                    '//div[@class="fl l-txt"]//span//text()')[1].extract()[:-2] + u"市"
                item['city_code'] = search_city_code_by_name(city_name)

                info_1 = house.xpath('.//div[@class="col-1"]')
                where = info_1.xpath('.//div[@class="where"]')
                temp = where.xpath(
                    './/span[@class="meters"]/text()')[0].extract()
                item['meters'] = float(extract_no(temp)[0])
                info_2 = house.xpath('.//div[@class="col-2"]')
                item['people_sum'] = int(
                    info_2.xpath('.//div[@class="square"]/div/span/text()')[0].extract())
                item['source'] = 'lj'
                bs = build_bs(item['house_link'])
                container = bs.find('div', class_="content zf-content")
                item['price'] = int(
                    container.find(
                        'div', class_="price ").find(
                        'span', class_="total").get_text())
                zf_room = container.find('div', class_="zf-room").find_all('p')
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
            except Exception:
                get_error_logger().error(
                    "{} link:{}".format(
                        traceback.format_exc(),
                        item['house_link']))
        # return items

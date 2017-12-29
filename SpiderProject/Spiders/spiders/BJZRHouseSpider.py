# -*- coding: utf-8 -*-
import traceback
import scrapy
from bs4 import BeautifulSoup
from urllib import urlopen
from ..items import HouseItem
from ..tools.hash_tool import *
from ..tools.print_log import *
from ..tools.str_tool import *


class BJZRHouseSpider(scrapy.Spider):
    """
    自如北京租房信息爬取
    """
    name = 'zrbj'
    allowed_domains = ['http://www.ziroom.com/']
    start_urls = ['http://www.ziroom.com/z/nl/z2.html?qwd=&p=1','http://www.ziroom.com/z/nl/z1.html?p=1',
                  'http://www.ziroom.com/z/nl/z6.html?p=1']

    def __init__(self, **kwargs):
        super(BJZRHouseSpider, self).__init__(**kwargs)
        # 友家合租
        url_1 = 'http://www.ziroom.com/z/nl/z2.html?qwd=&p='
        # 自如整租
        url_2 = 'http://www.ziroom.com/z/nl/z1.html?p='
        # 业主直租
        url_3 = 'http://www.ziroom.com/z/nl/z6.html?p='
        # for i in range(2, 50, 1):
        #     # self.start_urls.append(url_1 + str(i))
        #     self.start_urls.append(url_2+str(i))
        # for i in range(2,16,1):
        #     self.start_urls.append(url_3+str(i))

    def parse(self, response):
        house_list = response.xpath('//ul[@id="houseList"]')
        items = []
        for house in house_list.xpath('.//li[@class="clearfix"]'):
            item = HouseItem()
            txt = house.xpath('.//div[@class="txt"]')
            item['house_link'] = 'http:' + txt.xpath('.//h3//a/@href')[0].extract()
            try:
                item['hash_link'] = hash_str(item['house_link'])
                item['title'] = txt.xpath('.//h3//a/text()')[0].extract()
                item['region_hi'] = txt.xpath('.//h4/a/text()')[0].extract()
                info = txt.xpath('.//div[@class="detail"]')
                detail = info.xpath('.//p/span/text()')
                temp = extract_no(detail[2].extract())
                item['bedroom'] = int(temp[0])
                item['living_room'] = int(temp[1])
                item['meters'] = float(extract_no(detail[0].extract())[0])
                temp = house.xpath(
                    './/div[@class="priceDetail"]/p[@class="price"]/text()')[0].extract()
                item['price'] = int(extract_no(replace_space(temp))[0])
                item['source'] = 'zr'

                item['people_sum'] = 0
                # items.append(item)
            except Exception:
                get_error_logger().error("{} link:{}".format(traceback.format_exc(), item['house_link']))
        # return items

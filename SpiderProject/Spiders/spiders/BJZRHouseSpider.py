# -*- coding: utf-8 -*-
import traceback
import scrapy
from bs4 import BeautifulSoup
from ..items import HouseItem
from ..tools.hash_tool import *
from ..tools.print_log import *
from ..tools.str_tool import *
from ..tools.city_code_tool import *
import requests
from ..enums import RentWayEnum
from ..sql.sql_config import *


class BJZRHouseSpider(scrapy.Spider):
    """
    自如租房信息爬取

    """
    name = 'zr'
    allowed_domains = ['http://www.ziroom.com/']
    start_urls = [
        'http://www.ziroom.com/z/nl/z2.html?p=1',
        'http://www.ziroom.com/z/nl/z1.html?p=1',
        'http://www.ziroom.com/z/nl/z6.html?p=1',
        'http://sh.ziroom.com/z/nl/z2.html?p=1',
        'http://sh.ziroom.com/z/nl/z1.html?p=1',
        'http://sz.ziroom.com/z/nl/z2.html?p=1',
        'http://sz.ziroom.com/z/nl/z1.html?p=1']

    def __init__(self, **kwargs):
        super(BJZRHouseSpider, self).__init__(**kwargs)
        url_1_bj = 'http://www.ziroom.com/z/nl/z2.html?p='
        url_2_bj = 'http://www.ziroom.com/z/nl/z1.html?p='
        url_3_bj = 'http://www.ziroom.com/z/nl/z6.html?p='
        url_1_sh = 'http://sh.ziroom.com/z/nl/z2.html?p='
        url_2_sh = 'http://sh.ziroom.com/z/nl/z1.html?p='
        url_1_sz = 'http://sz.ziroom.com/z/nl/z2.html?p='
        url_2_sz = 'http://sz.ziroom.com/z/nl/z1.html?p='
        for i in range(2, 50, 1):
            # self.start_urls.append(url_1_bj + str(i))
            # self.start_urls.append(url_2_bj+str(i))
            self.start_urls.append(url_1_sh + str(i))
            self.start_urls.append(url_2_sh + str(i))
            self.start_urls.append(url_1_sz + str(i))
            self.start_urls.append(url_2_sz + str(i))
        for i in range(2,23,1):
            self.start_urls.append(url_3_bj+str(i))

    def parse(self, response):
        house_list = response.xpath('//ul[@id="houseList"]')
        items = []
        for house in house_list.xpath('.//li[@class="clearfix"]'):
            item = HouseItem()
            txt = house.xpath('.//div[@class="txt"]')
            item['house_link'] = 'http:' + \
                txt.xpath('.//h3//a/@href')[0].extract()
            item['hash_link'] = hash_str(item['house_link'])
            if judge_link(item['hash_link']) is not None:
                continue
            try:
                village = txt.xpath('.//h4//a//text()')[0].extract()
                item['village'] = village.split(']')[0][1:]
                city_name = response.xpath(
                    '//span[@id="curCityName"]//text()')[0].extract() + u'市'
                item['title'] = txt.xpath('.//h3//a/text()')[0].extract()
                item['region_hi'] = txt.xpath('.//h4/a/text()')[0].extract()
                info = txt.xpath('.//div[@class="detail"]')
                detail = info.xpath('.//p/span/text()')
                temp = info.xpath('.//p')[1].xpath('.//span//text()')
                if len(temp) > 0:
                    temp = temp[0].extract()
                    item['detail'] = temp
                    temp = extract_no(temp)
                    if len(temp) < 2:
                        item['subway'] = -1
                    else:
                        item['subway'] = int(temp[0])
                else:
                    item['detail'] = ''
                    item['subway'] = -1
                area = extract_no(detail[2].extract())
                item['bedroom'] = int(area[0])
                item['living_room'] = int(area[1])
                item['toilet'] = 1
                item['meters'] = float(extract_no(detail[0].extract())[0])
                area = house.xpath(
                    './/div[@class="priceDetail"]/p[@class="price"]/text()')[0].extract()
                item['price'] = int(extract_no(replace_space(area))[0])
                item['source'] = 'zr'
                item['people_sum'] = 0
                item['city_code'] = search_city_code_by_name(city_name)
                bs = build_bs(item['house_link'])
                area = bs.find(
                    'div', class_='node_infor area').find_all('a')[1].get_text()

                if u'整租' in area:
                    item['rent_way'] = RentWayEnum.SINGLE.value
                else:
                    item['rent_way'] = RentWayEnum.ALL.value
                con = bs.find('div', class_='room_detail_right')
                item['region_lo'] = re.split(
                    r'(\d+)',
                    replace_space(
                        con.find(
                            'div',
                            class_='room_name').find('h2').get_text()))[0]
                items.append(item)
            except Exception:
                get_error_logger().error(
                    "{} link:{}".format(
                        traceback.format_exc(),
                        item['house_link']))
        return items

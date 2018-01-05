# coding=utf-8
import requests
import scrapy
from bs4 import BeautifulSoup

from ..enums import *
from ..items import HouseItem
from ..tools.city_code_tool import *
from ..tools.hash_tool import *
from ..tools.print_log import *
from ..tools.str_tool import *
import traceback
from ..sql.sql_config import *


class BJ58HouseSpider(scrapy.Spider):
    """
    58网北京租房信息
    """
    name = "58bj"
    allowed_domains = ["http://bj.58.com/"]
    start_urls = ["http://bj.58.com/chuzu/pn1/"]

    def __init__(self, **kwargs):
        super(BJ58HouseSpider, self).__init__(**kwargs)
        init_url = "http://bj.58.com/chuzu/pn"
        for i in range(2, 7, 1):
            self.start_urls.append(init_url + str(i) + "/")

    def parse(self, response):
        house_list = response.xpath('//ul[@class="listUl"]//li')
        items = []
        for house in house_list:
            item = HouseItem()
            des = house.xpath('.//div[@class="des"]')
            house_link = des.xpath('.//h2//a/@href')
            item['title'] = replace_space(
                des.xpath('.//a//text()')[0].extract())
            item['house_link'] = replace_space(house_link[0].extract())
            get_info_logger().info(u"title:{},link:{}".format(item['title'],item['house_link']))
            if len(house_link) == 0:
                continue
            item['hash_link'] = hash_str(item['house_link'])
            if judge_link(item['hash_link']) is not None:
                continue
            try:
                html = requests.get(item['house_link']).content
                bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
                people = bs.find(id='totalcount')
                if people is None:
                    item['people_sum'] = -1
                else:
                    item['people_sum'] = int(people.get_text())
                container = bs.find(
                    'div', class_='house-basic-desc')
                # 价格
                price = int(
                    container.find_all(
                        'b', class_='f36')[0].get_text())

                item['price'] = price
                info_list = container.find_all('ul', class_='f14')[
                    0].find_all('li')
                # 租赁方式
                rent_way = info_list[0].find_all('span')[1].get_text()
                if u'整租' in rent_way:
                    item['rent_way'] = RentWayEnum.ALL.value
                else:
                    item['rent_way'] = RentWayEnum.SINGLE.value
                house_type = info_list[1].find_all('span')[1].get_text()
                temp = re.findall(u'\d+', house_type)
                item['bedroom'] = int(temp[0])
                item['living_room'] = int(temp[1])
                item['toilet'] = int(temp[2])
                item['meters'] = float(temp[3])
                item['village'] = info_list[3].find_all('span')[1].find('a')        .get_text()
                temp = info_list[4].find_all(
                    'span')[1].find_all('a', class_='c_333 ah')
                item['region_hi'] = temp[0].get_text()
                item['region_lo'] = temp[1].get_text()
                subway = info_list[4].find_all('em', class_='dt c_888 f12')
                if len(subway) != 0:
                    subway = subway[0].get_text()
                    judge = re.findall(u'\d+', subway)
                    if len(judge) < 2:
                        temp = -1
                    else:
                        temp = int(judge[0])
                    item['subway'] = temp
                    item['detail'] = subway
                else:
                    item['subway'] = -1
                item['source'] = SourceEnum.WB.value
                item['city_code'] = search_city_code_by_name(u'北京市')
                items.append(item)
            except Exception:
                get_error_logger().error(
                    "{} link:{}".format(traceback.format_exc(), item['house_link']))
                continue
        return items

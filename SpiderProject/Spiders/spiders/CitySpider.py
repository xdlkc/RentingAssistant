# -*- coding: utf-8 -*-
import scrapy
from ..items import *
from ..tools.str_tool import *


class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['http://www.ccb.com/']
    start_urls = [
        'http://www.ccb.com/cn/OtherResource/bankroll/html/code_help.html']

    def parse(self, response):
        items = []
        code_list = []
        container_list = response.xpath('//div[@class="fall"]')
        for container in container_list:
            province_list = container.xpath('.//div[@class="addlist"]')
            for province in province_list:
                province_name = province.xpath('.//h3//text()')[0].extract()
                for city in province.xpath('.//tr')[1:]:
                    item = CityItem()
                    temp = city.xpath('.//td//text()')
                    city_code = int(replace_space(temp[0].extract()))
                    city_name = replace_space(temp[1].extract())
                    if city_code not in code_list:
                        item['province_name'] = province_name
                        item['city_name'] = city_name
                        item['city_code'] = city_code
                        code_list.append(city_code)
                        items.append(item)
        return items

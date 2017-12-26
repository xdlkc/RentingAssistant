# coding=utf-8
__author__ = 'lkc'
from ..items import *

class ProxySpider(scrapy.Spider):
    """
    免费ip代理服务
    """
    name = "proxy"
    allowed_domains = ["http://31f.cn/"]
    start_urls = ["http://31f.cn/"]


    def parse(self, response):
        ip_list = response.xpath('//table[@class="table table-striped"]')[0].xpath('.//tr')[1:]
        items = []
        for ip in ip_list:
            item = ProxyItem()
            temp = ip.xpath('.//td//text()')
            item['ip'] = temp[1].extract().encode('ascii')
            item['port'] = temp[2].extract().encode('ascii')
            items.append(item)
        return items
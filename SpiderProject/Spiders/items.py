# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 房屋标题
    title = scrapy.Field()
    # 房屋链接
    house_link = scrapy.Field()
    # 由房屋链接计算的哈希（md5）
    hash_link = scrapy.Field()
    # 房屋大小
    meters = scrapy.Field()
    # 卧室
    bedroom = scrapy.Field()
    # 客厅
    living_room = scrapy.Field()
    # 卫生间
    toilet = scrapy.Field()
    # 评价人数
    people_sum = scrapy.Field()
    # 房屋来源:zr/58/lj todo：其他来源
    source = scrapy.Field()
    # 租赁方式：0整租/1合租
    rent_way = scrapy.Field()
    # 所在城市代码
    city_code = scrapy.Field()
    # 所在区（大级别）
    region_hi = scrapy.Field()
    # 所在区（小级别）
    region_lo = scrapy.Field()
    # 房屋价格（元/月）
    price = scrapy.Field()
    # 附近地铁
    subway = scrapy.Field()
    # 其他细节
    detail = scrapy.Field()
    # 小区
    village = scrapy.Field()


class CityItem(scrapy.Item):
    """
    城市类
    """
    city_name = scrapy.Field()
    province_name = scrapy.Field()
    city_code = scrapy.Field()


class LocationItem(scrapy.Item):
    """
    行政区类
    """
    region_name = scrapy.Field()
    city_name = scrapy.Field()

class ProxyItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
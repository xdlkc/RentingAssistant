# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Spiders.sql.init_sql import *
from sql.sql_config import *


class SpidersPipeline(object):

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        pass

    def close_spider(self, spider):
        pass


class HouseDataPipeline(object):
    """
    将租房信息写入数据库
    """

    def open_spider(self, spider):
        judge_table_sql = '''SELECT tablename FROM pg_tables WHERE tablename='house';'''
        create_table_sql = '''CREATE TABLE house(
                            id SERIAL PRIMARY KEY,
                            title VARCHAR(50) NOT NULL ,
                            house_link text NOT NULL ,
                            hash_link VARCHAR(32) NOT NULL ,
                            meters FLOAT NOT NULL ,
                            bedroom INT,
                            living_room INT,
                            toilet INT,
                            people_sum INT DEFAULT 0,
                            source VARCHAR(10) NOT NULL ,
                            rent_way INT NOT NULL ,
                            city_code INT NOT NULL REFERENCES city(city_code),
                            region_lo VARCHAR(50) NOT NULL ,
                            region_hi VARCHAR(50) NOT NULL ,
                            subway INT NOT NULL ,
                            price INT NOT NULL ,
                            detail VARCHAR(50),
                            village VARCHAR(20)
                            );'''
        create_index_sql = '''CREATE INDEX ON house(region_hi);CREATE INDEX ON house(village);CREATE UNIQUE INDEX ON house(hash_link);'''
        init_table(judge_table_sql, create_table_sql, create_index_sql)

    def process_item(self, item, spider):
        insert_sql = '''INSERT INTO house (title, house_link, hash_link, meters, bedroom, living_room, toilet,
                        people_sum, source, rent_way, city_code, region_lo, region_hi, subway, price, detail, village)
                        VALUES ('%s','%s','%s','%f','%d','%d','%d',
                        '%d','%s','%d','%d','%s','%s','%d','%d','%s','%s');''' % (item['title'],
                                                                                  item['house_link'],
                                                                                  item['hash_link'],
                                                                                  item['meters'],
                                                                                  item['bedroom'],
                                                                                  item['living_room'],
                                                                                  item['toilet'],
                                                                                  item['people_sum'],
                                                                                  item['source'],
                                                                                  item['rent_way'],
                                                                                  item['city_code'],
                                                                                  item['region_lo'],
                                                                                  item['region_hi'],
                                                                                  item['subway'],
                                                                                  item['price'],
                                                                                  item['detail'],
                                                                                  item['village'],
                                                                                  )
        insert_table(insert_sql)
        return item

    def close_spider(self, spider):
        pass


class CityDataPipeline(object):
    """
    城市信息写入数据库
    """

    def open_spider(self, spider):
        if spider.name != 'city':
            return
        judge_table_sql = '''SELECT tablename FROM pg_tables WHERE tablename='city';'''
        create_table_sql = '''CREATE TABLE city(
          id SERIAL PRIMARY KEY ,
          province_name VARCHAR(20) NOT NULL ,
          city_name VARCHAR(20) NOT NULL ,
          city_code INT
        );'''
        create_index_sql = '''CREATE INDEX ON city(city_name);CREATE UNIQUE INDEX ON city(city_code);'''
        init_table(judge_table_sql, create_table_sql, create_index_sql)

    def process_item(self, item, spider):
        if spider.name != 'city':
            return
        insert_sql = '''INSERT INTO city (province_name, city_name, city_code) VALUES ('%s','%s','%d');'''\
                     % (item['province_name'], item['city_name'], item['city_code'])
        get_info_logger().info(insert_sql)
        insert_table(insert_sql)
        return item

    def close_spider(self, spider):
        pass


class JsonPipeline(object):
    def open_spider(self, spider):
        self.filename = open(
            "{}/Spiders/jsons/{}.json".format(os.getcwd(), spider.name), "wb")
        self.filename.write('[')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.write(']')
        self.filename.close()

class ProxyPipeline(object):
    def open_spider(self, spider):
        self.filename = open(
            "{}/Spiders/ips/ips.txt".format(os.getcwd()), "wb")
        self.filename.write('[')

    def process_item(self, item, spider):
        if spider.name != 'proxy':
            return
        text = json.dumps(dict(item)) + ",\n"
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.write(']')
        self.filename.close()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql


class BossZpPipeline(object):
    def __init__(self):
        DATABASE = {
            "host": "23.83.251.245",
            "port": 3306,
            "user": "user1",
            "passwd": "123456",
            "db": "Boss_zp_xx",
            "charset": "utf8"
        }
        self.db = pymysql.connect(**DATABASE)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):

        sql = """insert into boss_python(name,link,salary,location,company,education,year)values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"""
        try:
            self.cur.execute(sql.format(item['name'], item['link'], item['salary'], item['location'], item['company'],
                                        item['education'], item['year']))
            print("插入成功")
            self.db.commit()
        except Exception as e:
            print("发生异常", e)
            self.db.rollback()

        return item

    def close_spider(self, spider):
        self.db.close()


class BooszpJavaPipeline(object):
    def __init__(self):
        DATABASE = {
            "host": "23.83.251.245",
            "port": 3306,
            "user": "user1",
            "passwd": "123456",
            "db": "Boss_zp_xx",
            "charset": "utf8"
        }

        self.db = pymysql.connect(**DATABASE)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = """inset into boss_java(name, link, salary, location, company, education, year)values('{}','{}','{}','{}','{}','{}','{}')"""
        try:
            self.cur.execute(sql.format(item['name'], item['link'], item['salary'], item['location'], item['company'],
                                        item['education'], item['year']))
        except Exception as e:
            print("出现异常{}".format(e))
            self.db.rollback()

    def close_spider(self):
        self.db.close()
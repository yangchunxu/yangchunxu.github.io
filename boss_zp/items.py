# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossZpItem(scrapy.Item):
    # 工作名称
    name = scrapy.Field()
    # 详情链接
    link = scrapy.Field()
    # 工资待遇
    salary = scrapy.Field()
    #  工作地址
    location = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 学历要求
    education = scrapy.Field()
    # 工作经验
    year = scrapy.Field()
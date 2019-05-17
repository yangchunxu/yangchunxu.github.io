import scrapy
from boss_zp.items import BossZpItem
import time


class BosszpSpider(scrapy.Spider):
    name = 'bs'
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=100109']

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        li = response.xpath("//div[@class='job-list']//ul//li")
        a = 0
        for i in li:
            name = i.xpath("//div[@class='info-primary']//h3//a//div[@class='job-title']/text()")[a].extract()
            link = i.xpath("//div[@class='info-primary']//h3//a/@href")[a].extract()
            salary = i.xpath("//div[@class='info-primary']//h3//a//span[@class='red']/text()")[a].extract()
            location = i.xpath("//div[@class='info-primary']//p/text()[1]")[a].extract()
            company = i.xpath("//div[@class='job-primary']//div[@class='company-text']//h3//a/text()")[a].extract()
            education = i.xpath("//div[@class='info-primary']//p/text()[3]")[a].extract()
            year = i.xpath("//div[@class='info-primary']//p/text()[2]")[a].extract()
            item = BossZpItem()
            item["name"] = name
            item["link"] = "https://www.zhipin.com" + link
            item["salary"] = salary
            item["location"] = location
            item["company"] = company
            item["education"] = education
            item["year"] = year
            yield item
            a += 1

        next_page = response.xpath(
            "//div[@class='job-list']//div[@class='page']//a[@class='next']/@href").extract_first()
        if next_page != None:
            url = "https://www.zhipin.com" + next_page
            yield scrapy.Request(url=url, callback=self.parse)


# class BosszpJavaSpider(scrapy.Spider):
#     name = 'java'
#     start_urls = []
#
#     def start_requests(self):
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
#         }
#         for url in self.start_urls:
#             yield scrapy.Request(url=url, headers=headers)
#
#     def parse(self, response):
#         li = response.xpath("//div[@class='job-list']//ul//li")
#         a = 0
#         for i in li:
#             name = i.xpath("//div[@class='info-primary']//h3//a//div[@class='job-title']/text()")[a].extract()
#             link = i.xpath("//div[@class='info-primary']//h3//a/@href")[a].extract()
#             salary = i.xpath("//div[@class='info-primary']//h3//a//span[@class='red']/text()")[a].extract()
#             location = i.xpath("//div[@class='info-primary']//p/text()[1]")[a].extract()
#             company = i.xpath("//div[@class='job-primary']//div[@class='company-text']//h3//a/text()")[a].extract()
#             education = i.xpath("//div[@class='info-primary']//p/text()[3]")[a].extract()
#             year = i.xpath("//div[@class='info-primary']//p/text()[2]")[a].extract()
#             item = BossZpItem()
#             item["name"] = name
#             item["link"] = "https://www.zhipin.com" + link
#             item["salary"] = salary
#             item["location"] = location
#             item["company"] = company
#             item["education"] = education
#             item["year"] = year
#             yield item
#             a += 1
#
#         next_page = response.xpath(
#             "//div[@class='job-list']//div[@class='page']//a[@class='next']/@href").extract_first()
#         if next_page != None:
#             url = "https://www.zhipin.com" + next_page
            yield scrapy.Request(url=url, callback=self.parse)
# -*- coding: utf-8 -*-
__author__ = 'Guixuan'

import re
import scrapy
from doubanbook.items import FangtianxiaItem


class FangtianxiaSpider(scrapy.Spider):
    name = 'fangtianxia'
    # allowed_domains = ['https://fz.anjuke.com/sale/?from=rentrec']
    start_urls = ['https://fz.anjuke.com/sale/?from=rentrec/']

    def __init__(self):
        self.count = 1

    def parse(self, response):
        houses = response.xpath('//ul[@id="houselist-mod-new"]/li[@class="list-item"]')
        item = FangtianxiaItem()

        for each_house in houses:
            des = each_house.xpath('div[@class="house-details"]/div[@class="house-title"]/a/@title').extract_first("null")
            structure = each_house.xpath('div[@class="house-details"]/div[@class="details-item"][1]/span[1]/text()').extract_first("null")
            areasize = each_house.xpath('div[@class="house-details"]/div[@class="details-item"][1]/span[2]/text()').extract_first("null")
            selling_price = each_house.xpath('div[@class="pro-price"]/span[@class="price-det"]/strong/text()').extract_first("null")
            address = each_house.xpath('div[@class="house-details"]/div[@class="details-item"][2]/span[@class="comm-address"]/@title').extract_first("null").replace("&nbsp;", " ")
            areasize = re.match(r'(\d+).+', areasize).group(1)
            address = address.replace("\xa0", " ")

            item['num'] = self.count
            item['des'] = des
            item['structure'] = structure
            item['areasize'] = areasize
            item['selling_price'] = selling_price
            item['address'] = address                          
            self.count += 1
            
            yield item

        next_page = response.xpath('//a[@class="aNxt"]/@href').extract_first("")
        if next_page:
            print(next_page)
            yield scrapy.http.Request(next_page, callback=self.parse)
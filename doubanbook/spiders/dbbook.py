# -*- coding: utf-8 -*-
__author__ = 'Guixuan'

import re
import scrapy
from doubanbook.items import DoubanbookItem


class DbbookSpider(scrapy.Spider):
    name = 'dbbook'
    # allowed_domains = ['https://www.douban.com/doulist/1264675/']
    start_urls = ['https://www.douban.com/doulist/1264675//']

    def __init__(self):
        self.count = 1

    def parse(self, response):
        books = response.xpath('//div[@class="bd doulist-subject"]')
        item = DoubanbookItem()

        for each_book in books:
            title = each_book.xpath('div[@class="title"]/a/text()').extract_first("null").replace("\n", "").replace(" ", "")
            author = each_book.xpath('div[@class="abstract"]/text()').extract_first("null").replace("\n", "").replace(" ", "").replace('\"', "")
            rate = each_book.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract_first("null")
            author = re.match(r'.+:(.*)', author).group(1).replace('\"', "")

            item['num'] = self.count
            item['title'] = title
            item['author'] = author
            item['rate'] = rate
            self.count += 1

            yield item


        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first("")
        if next_page:
            print(next_page)
            yield scrapy.http.Request(next_page, callback=self.parse)
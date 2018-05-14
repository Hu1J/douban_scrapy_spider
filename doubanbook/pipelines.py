# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from doubanbook.db.dbhelper import DoubanDBHelper, FangtianxiaDBHelper

class DoubanbookPipeline(object):

    # 连接数据库
    def __init__(self):
        self.db = DoubanDBHelper()
    
    def process_item(self, item, spider):
        # 解决多个爬虫混乱问题        
        if spider.name == 'dbbook':
            # 插入数据库
            self.db.insert(item)
        return item


class FangtianxiaPipeline(object):

    # 连接数据库
    def __init__(self):
        self.db = FangtianxiaDBHelper()
    
    def process_item(self, item, spider):
        # 解决多个爬虫混乱问题
        if spider.name == 'fangtianxia':
            # 插入数据库
            self.db.insert(item)
        return item
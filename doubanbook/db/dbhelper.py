import pymysql
from scrapy.utils.project import get_project_settings  #导入seetings配置


class DoubanDBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):
        settings = get_project_settings()  #获取settings配置，设置需要的信息
        self.db = pymysql.connect(
            settings['MYSQL_HOST'],
            settings['MYSQL_USER'],
            settings['MYSQL_PASSWD'],
            settings['MYSQL_DBNAME'],
            charset='utf8'
            )
        # 获取游标操作数据库
        self.cursors = self.db.cursor()

    #插入数据
    def insert(self, item):
        sql = "replace into dbbook(num, title, author, rate) values(%s,%s,%s,%s)"
        params = (
            item['num'], 
            item['title'], 
            item['author'], 
            item['rate']
            )
        #插入数据库
        try:
            self.cursors.execute(sql, args=params)
            self.db.commit()
        except:
            print('----------------Insert Error!----------------')
            self.db.rollback()
        
        return item


class FangtianxiaDBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):
        settings = get_project_settings()  #获取settings配置，设置需要的信息
        self.db = pymysql.connect(
            settings['MYSQL_HOST'],
            settings['MYSQL_USER'],
            settings['MYSQL_PASSWD'],
            settings['MYSQL_DBNAME'],
            charset='utf8'
            )
        # 获取游标操作数据库
        self.cursors = self.db.cursor()

    def insert(self, item):
        sql = "replace into Fang(num, des, structure, areasize, selling_price, address) values(%s,%s,%s,%s,%s,%s)"
        params = (
            item['num'],
            item['des'], 
            item['structure'], 
            item['areasize'], 
            item['selling_price'], 
            item['address']
            )
        #插入数据库
        try:
            self.cursors.execute(sql, args=params)
            self.db.commit()
        except:
            print('----------------Insert Error!----------------')
            self.db.rollback()

        return item
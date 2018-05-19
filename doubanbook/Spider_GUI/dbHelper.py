import pymysql

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'dbbook'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'AQ7C8359'

class DBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            password=MYSQL_PASSWD,
            charset='utf8'
        )
        # 获取游标操作数据库
        self.cursors = self.db.cursor()

    # 查询数据库
    def Confirm_user(self, userinfo):
        sql = "select password from login where username = '" + userinfo['username'] + "'"

        try:
            self.cursors.execute(sql)
            result = self.cursors.fetchone()
            if result[0] == userinfo['password']:
                return True
            else:
                return False
        except:
            pass


    def Regist_user(self, userinfo):
        sql = "insert into login value('" + userinfo['username'] + "', '" + userinfo['password'] +"')"

        try:
            self.cursors.execute(sql)
            self.db.commit()

            return "注册成功"
        except:
            print('----------------Insert Error!----------------')
            self.db.rollback()
            return "该用户已存在"

    def Query_by_condition(self, dbname, condition):
        if dbname == "dbbook":
            sql = "select title, author, rate from " + dbname
        else:
            sql = "select des, structure, areasize, selling_price, address from " + dbname
            
        if condition:
            sql += " where " + condition
        
        try:
            self.cursors.execute(sql)
            results = self.cursors.fetchall()
            return results
        except:
            return None

    def Delete_by_condition(self, dbname, condition):
        if not condition:
            return False
        
        sql = "delete from " + dbname + " where " + condition
        try:
            self.cursors.execute(sql)
            self.db.commit()

            return True
        except:
            self.db.rollback()
            return False 
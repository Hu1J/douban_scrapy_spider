import pymysql

db = pymysql.connect('localhost', 'root', 'AQ7C8359', 'dbbook')
#操作数据库的游标对象
cursor = db.cursor()

# execute()方法执行sql
# cursor.execute('select VERSION()')

# fetchone()获取一条数据
# data = cursor.fetchone()

# print(data)

# 数据库插入
# sql = "insert into test value('sssssad')"

# try:
#     # 执行sql
#     cursor.execute(sql)
#     # 提交到数据库
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()


# 数据库查询
# sql = 'select * from test'

# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()

#     for row in results:
#         print(row)

# except:
#     print('Unable to fetch data')


# SQL 更新语句  
# sql = "UPDATE user SET name = 'Bob' WHERE id = 1"  
# try:  
#     # 执行SQL语句  
#     cursor.execute(sql)  
#     # 提交到数据库执行  
#     db.commit()  
# except:  
#     # 发生错误时回滚  
#     db.rollback()




# 关闭数据库
db.close()
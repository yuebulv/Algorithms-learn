import pymysql.cursors

connection = pymysql.connect(host='localhost', port=3306, user='root', password='sunday', db='girls', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = connection.cursor()
    sql = "select * from boys"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
except Exception:
    print("查询失败")
cursor.close()
connection.close()
#import mysqldb
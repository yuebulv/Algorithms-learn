import re
from pymysql import connect
#  建立链接
conn = connect(host='localhost', port=3306, db='python_test_1', user='root', password='mysql', charset='utf8')
# 获取游标
cur = conn.cursor()
# 打开文件，读取所有文件存成列表
with open("/home/python/Desktop/code/data01.txt", "r") as file:
    # 可以选择readline或者read的方式,但下面的代码要有所变化
    data_list = file.readlines()
    # 遍历列表
    for t in data_list:
        # 正则方式匹配处理字符串
        text_list = re.split(r"\n", t)
        text = re.split(r"\t", text_list[0])
        # print(text)
        # sql语句
        sql = "insert into test_db values (0,%s,%s,%s,%s,%s)"
        print(sql)
        # 参数化方式传参
        row_count = cur.execute(sql,[text[0],text[1],text[2],text[3],text[4]])
        # 显示操作结果
        print("SQL语句影响的行数为%d" % row_count)
# 统一提交
conn.commit()
# 关闭游标　
cur.close()
# 关闭连接
conn.close()
import pymysql
import datetime, time

today = time.strftime('%Y%m%d', time.localtime(time.time()))
infohash_today_table = "infohash_" + today
infohash_file_name = "A.lj" #+ today
infohash_file_path = r"F:/mysql"
WriteInToTable = "LJ"

# 执行语句
def db_excute(sql):
    # local_infile = 1 执行load data infile
    db = pymysql.connect("localhost", "root", "sunday", "road", local_infile=1)
    db.set_charset('utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e)
    finally:
        db.close()


# 导入infohash数据到mysql xl_log_analysis 表
def LoadFile1(infohash_file_path='./output', infohash_file_name='',WriteInToTable=''):
    '''load data local infile "/root/test/infohash.txt_20180603" into table xl_log_analysis.infohash_20180603   LINES TERMINATED BY '\r\n'  (infohash);'''
    '''LINES TERMINATED BY \\r\\n WIN 为\\r,LINUX 为\\n'''

    sql = " load data local infile '" \
        + infohash_file_path + "/" \
        + infohash_file_name + "'" + \
        " into table " \
        + WriteInToTable
          # " LINES TERMINATED BY '\\r\\n' "
            #+ infohash_today_table + \
            #" (infohash); "
    db_excute(sql)
    print(sql)


if __name__ == '__main__':
    # 创建新表
    # createtable_sql = "create table if not exists `" + infohash_today_table + "` (" \
    #                                                                           "  `id` int(12) NOT NULL AUTO_INCREMENT COMMENT 'id'," + \
    #                   "  `infohash` varchar(40) DEFAULT NULL COMMENT 'infohash'," + \
    #                   "  PRIMARY KEY (`id`)" + \
    #                   ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    # db_excute(createtable_sql)  # 创建新表
    # print(createtable_sql)
    LoadFile1(infohash_file_path, infohash_file_name,WriteInToTable)  # 导入infohash_file_name数据到WriteInToTable 表
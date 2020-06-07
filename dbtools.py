import pymysql

def find(sql):
    """
    查询mysql数据库 只能select  不要delete、update、insert
    """
    # pymysql 连接数据库
    db = pymysql.connect(host="192.144.148.91",user="admin",password="adminDB123+",db="ljtestdb")
    # db = pymysql.connect(host="localhost",user="root",password="",db="testdb")
    cur = db.cursor()   # 获取游标  查询窗口

    # 执行SQL语句
    # sql = "select * from t_user where id = 255"
    cur.execute(sql)
    # 得到执行结果
    res = cur.fetchall()
    db.close()

    return res

# sql = "select * from t_class where id = 2 "
# a = find(sql)
# print(a)
# print(len(a))


def commit(sql):
    """
    增加/删除/修改方法：insert/delete/update 不要select
    """
    # 打开数据库
    # db = pymysql.connect(host="localhost",user="root",password="",db="testdb")
    db = pymysql.connect(host="192.144.148.91",user="admin",password="adminDB123+",db="ljtestdb")
    cur = db.cursor()   # 获取游标  查询窗口

    # 执行SQL语句
    # sql = "select * from t_user where id = 255"
    cur.execute(sql)
    db.commit()
    db.close()

    return True

# update方法
# sql = "update t_class set classname = '火箭班' where id = 4 " 

# insert  
# sql = "insert into t_class (id,classname,teacher) values (5,'就业班','王莉')"

# delete 
# sql = "delete from t_class where id = 5"
# commit(sql)


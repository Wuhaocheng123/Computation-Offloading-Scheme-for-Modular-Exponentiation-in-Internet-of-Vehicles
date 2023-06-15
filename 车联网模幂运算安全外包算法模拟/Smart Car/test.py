import mysql.connector

# 创建数据库连接
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="smart_car"
)

# 创建一个游标对象
cursor = cnx.cursor()

# 执行SQL查询
query = "DELETE FROM verification"
cursor.execute(query)
cnx.commit()



cursor.close()
cnx.close()

import gmpy2
from tool.tools import *
import mysql.connector
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="mec"
)
# 创建一个游标对象
cursor = cnx.cursor()
select_query = "SELECT ans,modular FROM sub_result"

# 执行查询语句
cursor.execute(select_query)

# 获取查询结果
results = cursor.fetchall()
print(results)
# 处理查询结果
ans1 = gmpy2.mpz(mod_mul(gmpy2.mpz(results[0][0]),gmpy2.mpz(results[1][0]),gmpy2.mpz(results[0][1])))
ans1 = gmpy2.mpz(mod_mul(ans1,gmpy2.mpz(results[2][0]),gmpy2.mpz(results[0][1])))
delete_query = "DELETE FROM sub_result"
cursor.execute(delete_query)
cnx.commit()
delete_query = "DELETE FROM task"
cursor.execute(delete_query)
cnx.commit()
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="smart_car"
)
cursor = cnx.cursor()
select_query = "SELECT N_key FROM verification"
# 执行查询语句
cursor.execute(select_query)

# 获取查询结果
result= cursor.fetchall()
print(result)
N = gmpy2.mpz(result[0][0])


print("RealAnswer:",gmpy2.mod(ans1,N))

#清空所有数据库，任务结束
delete_query = "DELETE FROM datafromsa"
cursor.execute(delete_query)
cnx.commit()
delete_query = "DELETE FROM verification"
cursor.execute(delete_query)
cnx.commit()

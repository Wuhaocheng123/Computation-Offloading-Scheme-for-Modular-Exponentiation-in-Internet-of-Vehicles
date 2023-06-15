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

# 处理查询结果
ans1 = mod_mul(results[0][0],results[1][0],results[0][1])
ans1 = mod_mul(ans1,results[2][0],results[0][1])

ans2 = mod_mul(results[3][0],results[4][0],results[0][1])
ans2 = mod_mul(ans2,results[5][0],results[0][1])


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="smart_car"
)

cursor = cnx.cursor()
select_query = "SELECT random_r FROM verification"

# 执行查询语句
cursor.execute(select_query)

# 获取查询结果
result= cursor.fetchall()
r = gmpy2.mpz(result[0][0])
print(r)

if mod_mul(ans1,r,results[0][1]) == ans2:
    print("结果正确")
else:
    print("结果错误")
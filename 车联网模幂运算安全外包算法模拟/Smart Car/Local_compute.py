from tool.tools import *
import gmpy2
import random
import mysql.connector
import socket
import pickle
def generatea(N): #生成u乘法循环群内的元素
    group = []
    for i in range(1, N):
        if gcd(i, N) == 1:
            group.append(i)
        if len(group)>10:
            return random.choice(group)
    g = random.choice(group)
    return gmpy2.mpz(g)
'''
智能汽车从数据库中读取SA传输的u,y,p,N
'''
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="smart_car"
)

# 创建一个游标对象
cursor = cnx.cursor()
select_query = "SELECT u, y, p, N FROM datafromsa"

# 执行查询语句
cursor.execute(select_query)

# 获取查询结果
results = cursor.fetchall()

# 处理查询结果
for row in results:
    u = gmpy2.mpz(row[0])
    y = gmpy2.mpz(row[1])
    p = gmpy2.mpz(row[2])
    N = gmpy2.mpz(row[3])
L = gmpy2.mpz(p*N)
#delete_query = "DELETE FROM datafromsa"
#cursor.execute(delete_query)
cnx.commit()


k,g ,gg = RandN(L)
k1,g1 = k[0],g[0]
k2,g2 = k[1],g[1]
k3,g3 = k[2],g[2]
k4,g4 = k[2],g[2]
'''生成四对随机数对'''


a = gmpy2.mpz(generatea((N-1)*(p-1)))


w1 = gmpy2.mpz(mod_mul(y,inverse(g1,L),L))

#求阶
ordLg  = order(gg,L)

ordLw1 = order(w1,L)
ak1 = mod_mul(a,k1,ordLg)
eulark3 = mod_mul(p-1,k3,ordLg)

t1y1 = mod_sub(ak1,eulark3,ordLg)#求得t1y1
m1 = mod_sub(a,t1y1,ordLw1) #求得w1



#求a的逆元d
d = gmpy2.mpz(inverse(a,(p-1)*(N-1)))

#选择随机数r
r = gmpy2.mpz(random.randint(2,N-1))
rd = gmpy2.mpz(mod_pow(r,d,L))
insert_query = "INSERT INTO verification (random_r,N_key) VALUES (%s,%s)"
data = (int(r),int(N))
cursor.execute(insert_query, data)
cnx.commit()

yp = gmpy2.mpz(mod_mul(y,rd,L))

w2 = gmpy2.mpz(mod_mul(yp,gmpy2.mpz(inverse(g2,L)),L))


ordLw2 = order(w2,L)


ak2 = mod_mul(a,k2,ordLg)

eulark4 = mod_mul(p-1,k4,ordLg)
t2y2 = mod_sub(ak2,eulark4,ordLg)#求得t2y2

m2 = mod_sub(a,t2y2,ordLw2) #求得w2

'''本地计算结束'''






'''
计算结果发送至MEC服务器
'''
# 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义服务器的主机名和端口号
host = '127.0.0.1'
port = 8888

# 连接服务器
client_socket.connect((host, port))


numbers = []
task1 = []
task1.append(g3)
task1.append(p-1)
task1.append(L)
numbers.append(task1)
task1 = []
task1.append(mod_mul(gg,w1,L))
task1.append(gmpy2.mpz(t1y1))
task1.append(L)
numbers.append(task1)
task1 = []
task1.append(w1)
task1.append(m1)
task1.append(L)
numbers.append(task1)
task1 = []
task1.append(g4)
task1.append(p-1)
task1.append(L)
numbers.append(task1)
task1 = []
task1.append(mod_mul(gg,w2,L))
task1.append(t2y2)
task1.append(L)
numbers.append(task1)
task1 = []
task1.append(w2)
task1.append(m2)
task1.append(L)
numbers.append(task1)
# 将数字转换为字符串，并用逗号分隔
serialized_data = pickle.dumps(numbers)

# 发送数据
client_socket.send(serialized_data)

# 关闭连接
client_socket.close()


















import socket
import pickle
import gmpy2
from tool.tools import *
import mysql.connector
# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="mec"
)
# 创建一个游标对象
cursor = cnx.cursor()
# 定义服务器的主机名和端口号
host = '127.0.0.1'
port = 8888

# 绑定服务器地址
server_socket.bind((host, port))

# 监听连接
server_socket.listen(1)

# 等待客户端连接
client_socket, addr = server_socket.accept()
print('客户端已连接：', addr)

# 接收数据
data = client_socket.recv(4096)

# 反序列化接收到的数据
received_array = pickle.loads(data)

# 处理接收到的二维数组
print('接收到的二维数组：')
for row in received_array:
    print(row)

# 关闭连接
client_socket.close()
server_socket.close()
L =gmpy2.mpz(0)
ans = []
# 定义插入数据的SQL语句
insert_query = "INSERT INTO sub_result (ans, modular) VALUES (%s, %s)"
for row in received_array:
    L = row[2]
    ans1 = gmpy2.mpz(mod_pow(gmpy2.mpz(row[0]),gmpy2.mpz(row[1]),gmpy2.mpz(row[2])))
    ans.append(ans1)
    data = (int(ans1),int(L))
    cursor.execute(insert_query, data)
    cnx.commit()

# 关闭游标和数据库连接
cursor.close()
cnx.close()



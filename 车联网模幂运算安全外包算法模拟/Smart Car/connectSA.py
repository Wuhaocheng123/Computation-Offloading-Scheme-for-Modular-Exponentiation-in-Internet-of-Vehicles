import socket
import mysql.connector
# 设置服务器主机和端口
HOST = 'localhost'
PORT = 8806

# 创建TCP套接字并绑定到指定的主机和端口
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# 监听连接
server_socket.listen(1)
print('等待客户端连接...')

# 接受连接
client_socket, addr = server_socket.accept()
print('连接成功：', addr)

try:
    # 接收客户端发送的数据
    data = client_socket.recv(1024)
    if not data:
        raise ValueError('无效的输入')

    # 解码收到的数据，并将其拆分为数字列表
    numbers_str = data.decode()
    numbers = [int(num) for num in numbers_str.split(',')]
    print('接收到的数字列表：', numbers)
except ValueError as e:
    print('无效的输入:', str(e))
#按 u y p N 的顺序接收
# 创建数据库连接
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="smart_car"
)

# 创建一个游标对象
cursor = cnx.cursor()

# 定义插入数据的SQL语句
insert_query = "INSERT INTO datafromsa (u, y, p, N) VALUES (%s, %s, %s, %s)"

# 要插入的数据
u_value = numbers[0]
y_value = numbers[1]
p_value = numbers[2]
N_value = numbers[3]

# 执行插入数据的SQL语句
data = (u_value, y_value, p_value, N_value)
cursor.execute(insert_query, data)

# 提交事务
cnx.commit()

# 关闭游标和数据库连接
cursor.close()
cnx.close()




# 关闭连接
client_socket.close()
server_socket.close()

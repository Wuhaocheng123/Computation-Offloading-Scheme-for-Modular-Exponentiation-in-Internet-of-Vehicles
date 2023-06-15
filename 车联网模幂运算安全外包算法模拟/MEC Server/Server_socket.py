import socket

# 创建套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名和端口号
host = socket.gethostname()
port = 12345

# 绑定套接字到本地主机和端口号
server_socket.bind((host, port))

# 监听连接
server_socket.listen(1)

# 等待客户端连接
print('等待客户端连接...')
client_socket, addr = server_socket.accept()
print('已连接：', addr)

# 接收来自客户端的数据
data = client_socket.recv(1024)
print('接收到的数据：', data.decode())

# 发送响应给客户端
response = 'Hello from server'
client_socket.send(response.encode())

# 关闭连接
client_socket.close()
server_socket.close()

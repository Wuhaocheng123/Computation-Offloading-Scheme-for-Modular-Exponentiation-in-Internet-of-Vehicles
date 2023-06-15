import gmpy2
import random
def is_prime(n, k=10): #检验数字是否是素数
    """
    Miller-Rabin 素性测试
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_prime(bits):#生成素数
    """
    生成指定位数的大素数
    """
    while True:
        n = random.randrange(2**(bits-1), 2**bits)
        if is_prime(n):
            return n

def gcd(a, b):#求最小公因数
    while b != 0:
        a, b = b, a % b
    return a

def random_int_in_residue(n):#生成随机的u
    # 生成范围为[0, n-1]的随机整数
    x = random.randint(0, n-1)
    # 返回x
    return x

def generateu(N): #生成u乘法循环群内的元素
    group = []
    k = []
    g = []
    for i in range(1, N):
        if gcd(i, N) == 1:
            group.append(i)
    g = random.choice(group)
    return g
N =  gmpy2.mpz(generate_prime(16))#模数N是64位大素数
p =  gmpy2.mpz(generate_prime(8))#素数p是32位小素数
print(p)
'''考虑运行效率问题，这里位数各缩小四倍'''

L = gmpy2.mpz(gmpy2.mul(N,p)) #L是两个素数相乘
u = gmpy2.mpz(generateu(N))
k = random.randint(0,N-1)
y = gmpy2.mpz(u +gmpy2.mul(k,N))
y = gmpy2.mpz(gmpy2.mod(y,L))

print("初始化后的参数：")
print("u:",u)
print("y:",y)
print("N:",N)
print("L:",L)
import socket

# 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义服务器的主机名和端口号
host = '127.0.0.1'
port = 8806

# 连接服务器
client_socket.connect((host, port))

# 要发送的数字列表
numbers = []
numbers.append(u)
numbers.append(y)
numbers.append(p)
numbers.append(N)

# 将数字转换为字符串，并用逗号分隔
numbers_str = ','.join(str(num) for num in numbers)

# 发送数据
client_socket.send(numbers_str.encode())

# 关闭连接
client_socket.close()
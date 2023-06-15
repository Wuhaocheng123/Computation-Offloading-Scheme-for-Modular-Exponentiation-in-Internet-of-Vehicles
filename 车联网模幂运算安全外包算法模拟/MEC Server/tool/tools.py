import gmpy2
import random

def mod_pow(a,b,p): #模幂运算
    return gmpy2.powmod(a,b,p)


def inverse(a,p): #求逆元
    return gmpy2.invert(a,p)


def mod_mul(a,b,p): #模乘法
    c =a*b
    return c%p


def gcd(a, b):#求最小公因数
    while b != 0:
        a, b = b, a % b
    return a


def RandN(N): #RandN程序
    group = []
    k = []
    ans = []
    for i in range(1, N):
        if gcd(i, N) == 1:
            group.append(gmpy2.mpz(i))
    g = gmpy2.mpz(random.choice(group))
    k1 = gmpy2.mpz(random.randint(0, N-1))
    k2 = gmpy2.mpz(random.randint(0, N-1))
    k3 = gmpy2.mpz(random.randint(0, N-1))
    k4 = gmpy2.mpz(random.randint(0, N-1))
    k.append(k1)
    k.append(k2)
    k.append(k3)
    k.append(k4)
    ans.append(gmpy2.mpz(mod_pow(g,k1,N)))
    ans.append(gmpy2.mpz(mod_pow(g,k2,N)))
    ans.append(gmpy2.mpz(mod_pow(g,k3,N)))
    ans.append(gmpy2.mpz(mod_pow(g,k4,N)))
    return k,ans,gmpy2.mpz(g)


def mod_sub(a,b,p):
        return gmpy2.mod(a-b,p)


def order(a, N):
    result = a
    order = 1

    while result != 1:
        result = (result * a) % N
        order += 1

    return gmpy2.mpz(order)


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
if __name__=='__main__':
    print(mod_sub(1,9,6))

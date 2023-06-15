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


N =  gmpy2.mpz(generate_prime(16))#模数N是64位大素数
p =  gmpy2.mpz(generate_prime(8))#素数p是32位小素数
print(p)
'''考虑运行效率问题，这里位数各缩小四倍'''

L = gmpy2.mpz(gmpy2.mul(N,p)) #L是两个素数相乘
u = gmpy2.mpz(generateu(N))
k = random.randint(0,N-1)
y = gmpy2.mpz(u +gmpy2.mul(k,N))
y = gmpy2.mpz(gmpy2.mod(y,L))


#p = gmpy2.mpz(generate_prime(6))#对应论文中的q


k,g ,gg = RandN(L)
k1,g1 = k[0],g[0]
k2,g2 = k[1],g[1]
k3,g3 = k[2],g[2]
k4,g4 = k[2],g[2]
'''生成四对随机数对'''


a = gmpy2.mpz(generatea((N-1)*(p-1)))

print("Realanswer:",gmpy2.mpz(mod_pow(u,a,N)))


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



yp = gmpy2.mpz(mod_mul(y,rd,L))

w2 = gmpy2.mpz(mod_mul(yp,gmpy2.mpz(inverse(g2,L)),L))


ordLw2 = order(w2,L)


ak2 = mod_mul(a,k2,ordLg)

eulark4 = mod_mul(p-1,k4,ordLg)
t2y2 = mod_sub(ak2,eulark4,ordLg)#求得t2y2

m2 = mod_sub(a,t2y2,ordLw2) #求得w2

'''本地计算结束'''












#MEC服务器计算内容
ans1 =gmpy2.mpz( mod_pow(g3,p-1,L))
ans2 =gmpy2.mpz(mod_pow(mod_mul(gg,w1,L),t1y1,L))
ans3 =gmpy2.mpz(mod_pow(w1,m1,L))

ans11 =gmpy2.mpz(mod_pow(g4,p-1,L))
ans22 =gmpy2.mpz(mod_pow(mod_mul(gg,w2,L),t2y2,L))
ans33 =gmpy2.mpz(mod_pow(w2,m2,L))



#验证执行内容
yunanswer = mod_mul(ans1,ans2,L)
yunanswer = mod_mul(yunanswer,ans3,L)
yunanswer2 = mod_mul(ans11,ans22,L)
yunanswer2 = mod_mul(yunanswer2,ans33,L)

answer1 = gmpy2.mpz(mod_mul(r,yunanswer,L))


if answer1 == mod_pow(yp,a,L):
    print("结果正确")
else:
    print("结果错误")













#客户端计算结果内容
print("Realanswer:",gmpy2.mod(yunanswer,N))



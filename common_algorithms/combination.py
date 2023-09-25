from operator import mul
from functools import reduce

#普通に値を算出する場合
def cmb(n,r):
    if n < r or n == 0: return 0
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
print(cmb(1,3))    
a = cmb(52,5)
print(13*12*4*6/a)


#（１０＊＊9＋７）の余りを求める場合（競プロ用）
def cmb2(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10**9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


#計算量はO(n)
#Nが大きくなったら使えない
#何回もnCrの計算をする時に便利（値をストックしてあるので）



#より高速に
def pow(x, n ,p):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = (x*K) % p
        x = (x*x) % p
        n //= 2

    return (K * x) % p




def cmb3(n,r,q):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)    
    s = 1
    for x in range(n,n-r,-1):
        s = (s*x) % q
    t = 1
    for x in range(1,r+1):
        t = (t*x) % q

    #割る数の剰余をどうするかが問題
    t = pow(t,q-2,q)
    return (t * s) % q
#ここだけで計算量はO(q)
    
#合計でO(logq+2r)    
#上のNの値が10**6以上のオーダーかつrがそれ以下ならこっちが速そう
#rの値も大きいと使えない

s = 0
for i in range(1,11):
    s += cmb(i+8,i)

print(s)    

        

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

print(factorization(2019))

## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1
## n == 1 なら[1,1]となってしまうことに注意
## 一つだけの素因数分解ならこれが一番速い
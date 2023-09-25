#エラトステネスの篩（素数列挙）
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: #もしiが探索済みなら
            continue #ループの最初に戻る
        for j in range(i * 2, n + 1, i): #iより大きいiの倍数を探索済みにする
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
#これだけで計算量は O(n/2+n/3+n/5+n/7+.......+n/int(√n)) = O(nloglog√n) = O(n(loglogn+log1/2))
print(primes(100))

#soinnsubunkai1のrange部分をこのリストに書き換えるだけ
def factorization2(n):
    lst = primes(int(-(-n**0.5//1)))
    
    arr = []
    temp = n
    for i in lst:
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

print(factorization2(1))
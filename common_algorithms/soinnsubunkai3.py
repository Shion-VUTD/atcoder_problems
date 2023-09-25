
def factorization3(n):
    #エラトステネスの篩（素数列挙）さらに合成数をふるい落とした素数を記録
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i] != True:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = i
     
    #素因数分解で、余計な素数を探索せずに済む！
    arr = []
    temp = n
    while is_prime[temp] != True and temp != 1:
        k = is_prime[temp]
        cnt=0
        while temp % k == 0:
            cnt+=1
            temp //= k
        arr.append([k, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

print(factorization3(100))
#ここまでの計算量はO(NloglogN(前処理) + logN(実際の分解))

n = 100
A = [1000000,99999,99998]
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(100**0.5) + 1):
    if is_prime[i] != True:
        continue
    for j in range(i * 2, 100 + 1, i):
        is_prime[j] = i

num = [0]*(10**6+1) #LCMの素因数分解


for i in range(n):
  temp = A[i]
  while is_prime[temp] != True and temp != 1:
      k = is_prime[temp]
      cnt=0
      while temp % k == 0:
          cnt+=1
          temp //= k
      
      if num[k] < cnt:
        num[k] = cnt

  if temp!=1:
      if num[temp] < 1:
        num[temp] = 1
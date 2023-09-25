# 素数判定の実装

import math


# 1. 数xの素数判定をする場合 O(√x)
def is_prime(x):
    # 2から√xまでの奇数で割る
    square_root_x = int(math.sqrt(x))
    if x == 1:
        return False
    if x in [2, 3, 5, 7]:
        return True
    elif x % 2 == 0:
        return False
    else:
        for k in range(3, square_root_x + 1):
            if x % k == 0:
                return False
    return True


print(is_prime(119))

# AKS素数判定法というのもある(O(logx^m))


# 2. 数1~xの素数判定を全て行う場合 O(xloglogx)
def eratos(x):
    is_primes = [True] * (x + 1)
    is_primes[0] = False
    is_primes[1] = False
    square_root_x = int(math.sqrt(x))

    for i in range(2, square_root_x + 1):
        if is_primes[i] == True:
            tmp = i * 2
            while tmp <= x:
                is_primes[tmp] = False
                tmp += i

    return is_primes


print(eratos(50))

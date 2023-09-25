def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x


#10**9+7で割った余りを求める場合（競プロ用）
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


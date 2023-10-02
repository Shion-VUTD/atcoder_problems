n, m = map(int, input().split())
dp = [0] * (n+1)
p = 998244353

dp[2] = ((m * (m-1)) % p) % p

if n >= 3:
    dp[3] = (((m * (m-1) % p) * (m-2)) % p) % p

# print(dp[2], dp[3])
if n >= 4:
    for i in range(4, n + 1):
        dp[i] = (dp[i-1] * (m - 2)) % p + (dp[i-2] * (m - 1)) % p
        dp[i] %= p
        # print(dp[i])

print(dp[n])


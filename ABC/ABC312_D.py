s = input()
n = len(s)
if n % 2 == 1:
    print(0)    
    exit()

n = n // 2
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

mod = 998244353

for i in range(1, n + 1):
    if s[i-1] != ")":
        dp[i][0] = dp[i - 1][0]
    for j in range(1, i + 1):
        total = i + j
        x = dp[i][j - 1]
        y = dp[i - 1][j]
        if s[total - 1] == "(":
            dp[i][j] = y
        elif s[total - 1] == ")":
            dp[i][j] = x
        else:
            dp[i][j] = (x + y) % mod


# print(dp)
print(dp[n][n])

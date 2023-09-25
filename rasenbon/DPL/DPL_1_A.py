# コイン問題を2次元DPで解く
# m種類のコインを使ってn円支払う時のコインの最小枚数を求める
# dp[i][j]には、i種類目までのコインを使ってj円支払う際の最小枚数を記録(iは0-index)
# 計算量はO(nm)

n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

dp = [[0] * (n + 1) for i in range(m)]
for j in range(1, n + 1):
    dp[0][j] = j

for i in range(1, m):
    for j in range(1, n + 1):
        if j - coins[i] >= 0:
            dp[i][j] = min([dp[i - 1][j], dp[i][j - coins[i]]+1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[m-1][n])


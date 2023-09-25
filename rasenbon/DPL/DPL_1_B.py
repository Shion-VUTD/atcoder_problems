# 0-1ナップザック問題を2次元DPで解く
# 各荷物には、価値と重みが与えられている
# N種類の荷物がある。重みの合計がWを超えない荷物の詰め方における価値の合計の最大値を求める
# dp[i][j]: i+1番目までの荷物を乗せる際に重みの合計がjを超えないようにするときの価値の最大値(iは0-index)
# 時間計算量O(NM)

n, w = map(int, input().split())
stocks = []
for i in range(n):
    value, weight = map(int, input().split())
    stocks.append((value, weight))

dp = [[0]*(w+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, w+1):
        if j - stocks[i-1][1] >= 0:
            dp[i][j] = max([dp[i-1][j], dp[i-1][j-stocks[i-1][1]] + stocks[i-1][0]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][w])


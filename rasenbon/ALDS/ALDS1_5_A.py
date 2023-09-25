n = int(input())
a = list(map(int, input().split()))
q = int(input())
query = list(map(int, input().split()))
max_value = sum(query)

# i番目までの要素を使ってmを作れる場合Trueを返す

dp = [["Unknown"] * (n + 1) for i in range(max_value + 1)]

for i in range(n + 1):
    dp[0][i] = True

for i in range(1, max_value + 1):
    dp[i][0] = False

for i in range(1, n + 1):
    for m in range(1, max_value + 1):
        m_prep = m - a[i - 1]
        if m_prep < 0:
            dp[m][i] = dp[m][i - 1]
        else:
            dp[m][i] = (dp[m][i - 1] or dp[m_prep][i - 1])

for m in query:
    if dp[m][n]:
        print('yes')
    else:
        print('no')

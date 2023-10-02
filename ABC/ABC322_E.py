n, k, p = map(int, input().split())
developments = []

for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(5 - k):
        inp.append(0)
    developments.append(inp)

# print(developments)

dp = [[[[[
    [10 ** 12 for _ in range(p + 1)
    ] for _ in range(p + 1)
    ] for _ in range(p + 1)] for _ in range(p + 1)
    ] for _ in range(p + 1)] for _ in range(n + 1)
    ]

dp[0][0][0][0][0][0] = 0
for i in range(1, n + 1):
    for j1 in range(p + 1):
        for j2 in range(p + 1):
            for j3 in range(p + 1):
                for j4 in range(p + 1):
                    for j5 in range(p + 1):
                        dp[i][j1][j2][j3][j4][j5] = min(dp[i - 1][j1][j2][j3][j4][j5], dp[i - 1][max(0, j1 - developments[i - 1][1])][max(0, j2 - developments[i - 1][2])][max(0, j3 - developments[i - 1][3])][max(0, j4 - developments[i - 1][4])][max(0, j5 - developments[i - 1][5])] + developments[i - 1][0])
                        # print(i, j1, j2, j3, j4, j5, dp[i][j1][j2][j3][j4][j5])

# print(dp[n][p][p][p][0][0], k)
if k == 1:
    ans = dp[n][p][0][0][0][0]
elif k == 2:
    ans = dp[n][p][p][0][0][0]
elif k == 3:
    ans = dp[n][p][p][p][0][0]
elif k == 4:
    ans = dp[n][p][p][p][p][0]
elif k == 5:
    ans = dp[n][p][p][p][p][p]

if ans == 10 ** 12:
    ans = -1

print(ans)

# k回for文回す部分を可変にする方法はないのか？
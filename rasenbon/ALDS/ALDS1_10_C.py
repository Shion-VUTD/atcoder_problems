n = int(input())

for i in range(n):
    s_a = input()
    s_b = input()
    dp = [[0]*(len(s_b) + 1) for i in range(len(s_a) + 1)]
    for j in range(len(s_a)):
        for k in range(len(s_b)):
            if s_a[j] == s_b[k]:
                dp[j+1][k+1] = dp[j][k] + 1
            else:
                dp[j+1][k+1] = max([dp[j][k+1], dp[j+1][k]]) 
    print(dp[-1][-1])
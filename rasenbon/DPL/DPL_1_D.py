# 最長増加部分列問題を1次元DPで解く
# dp[i]: 長さiの最長増加部分列のうち、末尾の数値の最小値
# このdpの計算を数列Aの要素の数だけ繰り返す(k回目の試行後のdp: k番目までの数を用いた場合のdp)

import bisect

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

dp = [10**9 + 1] * (n + 1)
dp[0] = -1

for k in nums:
    insert_index = bisect.bisect_left(dp, k)
    dp[insert_index] = k

for i, length in enumerate(dp):
    if length == 10**9 + 1:
        print(i - 1)
        exit()

print(n)


# 最大正方形問題(この前のABC311-Eでも出てきた!)
# 各マス(i, j)について、
# dp[i][j]: マス(i, j)を左下の頂点とするような正方形の中で最大のもの

import copy
import numpy as np

h, w = map(int, input().split())
grid = []
for i in range(h):
    line = list(map(int, input().split()))
    grid.append(line)

# 初期化
dp = 1 - np.array(copy.deepcopy(grid))

for i in range(1, h):
    for j in range(1, w):
        max_square_above = dp[i - 1][j]
        max_square_left = dp[i][j - 1]
        if grid[i][j] == 1:
            dp[i][j] = 0
        elif max_square_above != max_square_left:
            dp[i][j] = min([max_square_above + 1, max_square_left + 1])
        elif grid[i - max_square_above][j - max_square_above] == 1:
            dp[i][j] = max_square_above
        else:
            dp[i][j] = max_square_above + 1

print(np.max(dp) ** 2)
# print(dp)


# dp漸化式の別解
dp2 = 1 - np.array(copy.deepcopy(grid))
for i in range(1, h):
    for j in range(1, w):
        max_square_above = dp[i - 1][j]
        max_square_left = dp[i][j - 1]

        # 左上を入れると、max_square_above == max_square_leftの例外処理をしなくて済む
        max_square_upperleft = dp[i - 1][j - 1]

        if grid[i][j] == 1:
            dp2[i][j] = 0
        else:
            dp2[i][j] = (
                min([max_square_above, max_square_left, max_square_upperleft]) + 1
            )

print(np.max(dp2) ** 2)

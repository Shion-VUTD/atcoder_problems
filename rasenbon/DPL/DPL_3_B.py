# 最大長方形問題
#  穴の空いてない部分のみを使ってできる長方形の面積の最大値を求める問題
# 1. まず、各マスから縦にどれだけ行けるかを記録 O(HW)
# 2. 横に続く各線分について、その線分をx軸とするヒストグラムの内部で面積最大の長方形を計算する
#   普通にやったらO(H * W^2)
#   スタックに(ヒストグラムの棒の高さ, x座標)を記録していくことでO(HW)に抑える！ (ALDS1_3_D.pyを参照)

import numpy as np
import copy

h, w = map(int, input().split())
grid = []
for i in range(h):
    line = list(map(int, input().split()))
    line.append(1)
    line = [1] + line
    grid.append(line)


hist_heights = 1 - np.array(copy.deepcopy(grid))
for i in range(1, h):
    for j in range(w+2):
        if hist_heights[i][j] == 0:
            continue
        hist_heights[i][j] = hist_heights[i - 1][j] + 1

# print(hist_heights)

max_area = -1
for i in range(h):
    stack = [(0, hist_heights[i][0])]
    for j in range(1, w + 2):
        # print(stack)
        # 直前よりヒストグラムの棒が高かった場合
        if hist_heights[i][j] > hist_heights[i][j - 1]:
            stack.append((j, hist_heights[i][j]))

        # 直前とヒストグラムの棒が同じだった場合
        elif hist_heights[i][j] == hist_heights[i][j - 1]:
            continue

        # 直前よりヒストグラムの棒が低かった場合
        else:
            while True:
                # print(stack)
                tmp, height_tmp = stack[-1]
                if height_tmp < hist_heights[i][j]:
                    stack.append((j, hist_heights[i][j]))
                    break
                elif height_tmp == hist_heights[i][j]:
                    break
                else:
                    tmp, height_tmp = stack.pop()
                    # 面積が確定する
                    tmp_area = height_tmp * (j - tmp)
                    if max_area < tmp_area:
                        max_area = tmp_area

print(max_area)

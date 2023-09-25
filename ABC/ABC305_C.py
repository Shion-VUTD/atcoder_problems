import numpy as np
from collections import Counter

h, w = map(int, input().split())
maps = [[0] * w for _ in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == "#":
            maps[i][j] = 1

maps = np.array(maps)
sum_axis_0 = list(np.sum(maps, axis=1, keepdims=False))
sum_axis_1 = list(np.sum(maps, axis=0, keepdims=False))
# print(sum_axis_0, sum_axis_1)

sums_0 = Counter(sum_axis_0)
sums_1 = Counter(sum_axis_1)

eaten_0 = sum_axis_0.index(sorted(sums_0.keys(), reverse=True)[1])
eaten_1 = sum_axis_1.index(sorted(sums_1.keys(), reverse=True)[1])

print(eaten_0 + 1, eaten_1 + 1)


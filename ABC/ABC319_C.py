import itertools
import math

maps = []

for i in range(3):
    x, y, z = map(int, input().split())
    for j in [x, y, z]:
        maps.append(j)

lines = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {6, 4, 2}]
p_iters = itertools.permutations(range(9))

num_paths = 0
for p in p_iters:
    is_break_2 = False
    for line in lines:
        value_1 = -1
        value_2 = -1
        is_break = False
        for index in p:
            if index in line:
                if value_1 == -1:
                    value_1 = maps[index]
                elif value_2 == -1:
                    value_2 = maps[index]
                    if value_1 == value_2:
                        is_break = True
                        break
        if is_break:
            is_break_2 = True
            break
    if is_break_2:
        continue
    num_paths += 1

print(num_paths / math.factorial(9))
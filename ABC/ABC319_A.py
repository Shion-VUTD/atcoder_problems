maps = []
from copy import deepcopy
import math

for i in range(3):
    maps.append(list(map(int, input().split())))

# print(maps)

middle_axes = [[[] for i in range(3)] for i in range(3)]
middle_freq = [[0] * 3 for i in range(3)]

"""
for i in range(3):
    if maps[i][0] == maps[i][1] and maps[i][0] != maps[i][2]:
        middle_freq[i][2] += 1
        middle_axes[i][2].append((0, i))
    elif maps[i][0] == maps[i][2] and maps[i][0] != maps[i][1]:
        middle_freq[i][1] += 1
        middle_axes[i][1].append((0, i))
    elif maps[i][1] == maps[i][2] and maps[i][0] != maps[i][1]:
        middle_freq[i][0] += 1
        middle_axes[i][0].append((0, i))

for j in range(3):
    if maps[0][j] == maps[1][j] and maps[0][j] != maps[2][j]:
        middle_freq[2][j] += 1
        middle_axes[2][j].append((1, j))
    elif maps[0][j] == maps[2][j] and maps[0][j] != maps[1][j]:
        middle_freq[1][j] += 1
        middle_axes[1][j].append((1, j))
    elif maps[1][j] == maps[2][j] and maps[0][j] != maps[1][j]:
        middle_freq[0][j] += 1
        middle_axes[0][j].append((1, j))

if maps[0][0] == maps[1][1] and maps[0][0] != maps[2][2]:
    middle_freq[2][2] += 1
    middle_axes[2][2].append((2, 1))
elif maps[0][0] == maps[2][2] and maps[0][0] != maps[1][1]:
    middle_freq[1][1] += 1
    middle_axes[1][1].append((2, 1))
elif maps[1][1] == maps[2][2] and maps[0][0] != maps[1][1]:
    middle_freq[0][0] += 1
    middle_axes[0][0].append((2, 1))


if maps[0][2] == maps[1][1] and maps[0][2] != maps[2][0]:
    middle_freq[2][0] += 1
    middle_axes[2][0].append((2, -1))
elif maps[0][2] == maps[2][0] and maps[0][2] != maps[1][1]:
    middle_freq[1][1] += 1
    middle_axes[1][1].append((2, -1))
elif maps[1][1] == maps[2][0] and maps[0][2] != maps[1][1]:
    middle_freq[0][2] += 1
    middle_axes[0][2].append((2, -1))
"""

print(middle_freq)
print(middle_axes)

stack = []
# 初期値を入れる
for i in range(3):
    for j in range(3):
        if middle_freq[i][j] == 0:
            stack.append([{(i, j)}, middle_freq,  (i, j)])

ans = 0
while stack:
    # print("len:", len(stack), stack)
    tmp = stack.pop()
    visited_nodes, middle_freq, i, j = tmp[0], tmp[1], tmp[2][0], tmp[2][1]
    new_middle_freq = deepcopy(middle_freq)

    # rint(i, j)
    if len(visited_nodes) == 9:
        ans += 1
        print(ans)
        continue
    if (0, i) in middle_axes[i][j]:
        for k in {0, 1, 2} - {j}:
            if middle_freq[i][k] != 0 and (i, k) not in visited_nodes:
                # print(i, k)
                new_middle_freq[i][k] -= 1
                # print("pattern a")
    if (1, j) in middle_axes[i][j]:
        for k in {0, 1, 2} - {i}:
            if (k, j) not in visited_nodes:
                new_middle_freq[k][j] -= 1
                # print("pattern b")
    if i == j and (2, 1) in middle_axes[i][j]:
        for k in {0, 1, 2} - {i}:
            if (k, k) not in visited_nodes:
                new_middle_freq[k][k] -= 1
                # print("pattern c")
    if i + j == 2 and (2, -1) in middle_axes[i][j]:
        for k in {0, 1, 2} - {i}:
            if (k, 2 - k) not in visited_nodes:
                new_middle_freq[k][2 - k] -= 1
                # print("pattern d")

    for k in range(3):
        if middle_freq[i][k] != 0 and (0, i) in middle_axes[i][k]:
            # new_middle_freq[i][k] -= 1
            for l in {0, 1, 2} - {j, k}:
                new_middle_freq[i][l] += 1
                # print("pattern e")
                
    for l in range(3):
        if middle_freq[l][j] != 0 and (1, j) in middle_axes[l][j]:
            # new_middle_freq[l][j] -= 1
            for k in {0, 1, 2} - {i, l}:
                new_middle_freq[k][j] += 1
                # print("pattern f")

    if i == j:
        for k in range(3):
            if j != k and middle_freq[k][k] != 0 and (2, 1) in middle_axes[k][k]:
                new_middle_freq[k][k] -= 1
                for l in {0, 1, 2} - {i, k}:
                    new_middle_freq[l][l] += 1
                    # print("pattern g")

    if i + j == 2:
        for k in range(3):
            if i != k and middle_freq[k][2 - k] != 0 and (2, -1) in middle_axes[k][2 - k]:
                # new_middle_freq[k][2 - k] -= 1
                for l in {0, 1, 2} - {i, k}:
                    new_middle_freq[l][2 - l] += 1
                    # print("pattern h")

    print(new_middle_freq)
    for k in range(3):
        for l in range(3):
            if new_middle_freq[k][l] == 0 and (k, l) not in visited_nodes:
                next_visited_nodes = deepcopy(visited_nodes)
                next_visited_nodes.add((k, l))
                stack.append([next_visited_nodes, new_middle_freq, (k, l)])

# print(ans)              
print(ans / math.factorial(9))
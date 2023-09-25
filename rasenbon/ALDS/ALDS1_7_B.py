# グローバル変数

n = int(input())
adjacency_list = [[] for i in range(n)]
node_types = ["internal node"] * n
parents = [-1] * n
siblings = [-1] * n
heights = [-1] * n
degrees = [0] * n

for i in range(n):
    tmp, left, right = map(int, input().split())
    if left == right == -1:
        node_types[tmp] = "leaf"
        heights[tmp] = 0
    elif left != -1 and right == -1:
        parents[left] = tmp
        degrees[tmp] = 1
        adjacency_list[tmp].append(left)
    elif left == -1 and right != -1:
        parents[right] = tmp
        degrees[tmp] = 1
        adjacency_list[tmp].append(right)
    else:
        parents[left] = tmp
        parents[right] = tmp
        siblings[left] = right
        siblings[right] = left
        degrees[tmp] = 2
        adjacency_list[tmp].append(left)
        adjacency_list[tmp].append(right)


# まず根を調べる
root = -1
for i in range(n):
    if parents[i] == -1:
        node_types[i] = "root"
        root = i
        break


# 各ノードの深さを調べる
stack = [root]
depths = [-1] * n
depths[root] = 0

while stack != []:
    tmp = stack.pop()
    for x in adjacency_list[tmp]:
        if depths[x] == -1:
            depths[x] = depths[tmp] + 1
            stack.append(x)

# 高さを調べる
def cal_height(node):
    if heights[node] != -1:
        return heights[node]
    else:
        height = max([cal_height(x) for x in adjacency_list[node]]) + 1
        heights[node] = height
        return heights[node]

# print(adjacency_list)
# print(node_types)
# print(parents)
# print(depths)

# 出力
for i in range(n): 
    print("node {0}: parent = {1}, sibling = {2}, degree = {6}, depth = {3}, height = {4}, {5}".format(
        i, parents[i], siblings[i], depths[i], cal_height(i), node_types[i], degrees[i]
    ))


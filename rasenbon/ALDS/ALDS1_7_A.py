n = int(input())
adjacency_list = [[] for i in range(n)]
node_types = ["internal node"] * n
parents = [-1] * n

for i in range(n):
    nexts = list(map(int, input().split()))
    if nexts[1] == 0:
        node_types[nexts[0]] = "leaf"
    else:
        for x in nexts[2:]:
            parents[x] = nexts[0]
            adjacency_list[nexts[0]].append(x)

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

# print(adjacency_list)
# print(node_types)
# print(parents)
# print(depths)

# 出力
for i in range(n):
    print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(
        i, parents[i], depths[i], node_types[i], adjacency_list[i]
    ))


"""トポロジカルソート

トポロジカルソートとは、閉路を持たない有効グラフについて、以下の条件を満たすように全頂点を一列に並べ替えるアルゴリズム。
・任意の有向辺について、始点が終点より先に配置されている

"""

from collections import deque

num_nodes, num_edges = map(int, input().split())

# 隣接リストを作る
next_list = [[] for i in range(num_nodes)]
indeg_list = [0] * num_nodes

for i in range(num_edges):
    x, y = map(int, input().split())
    next_list[x].append(y)
    indeg_list[y] += 1

# 出次数0のノードを全部入れて初期化
zero_indeg_queue = deque([])
for i in range(num_nodes):
    if indeg_list[i] == 0:
        zero_indeg_queue.append(i)

ans_list = []

while zero_indeg_queue:
    node = zero_indeg_queue.popleft()
    ans_list.append(node)
    for next_node in next_list[node]:
        indeg_list[next_node] -= 1
        if indeg_list[next_node] == 0:
            zero_indeg_queue.append(next_node)

if len(ans_list) != num_nodes:
    print("CIRCLE!")
else:
    print(ans_list)

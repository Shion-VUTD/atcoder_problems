# 関節点の実装
# 解説はGRL_3_A.pyを参照
import copy
import numpy as np

v, e = map(int, input().split())
next_node_list = [[] for i in range(v)]
for edge in range(e):
    x, y = map(int, input().split())
    next_node_list[x].append(y)
    next_node_list[y].append(x)

# 頂点0を根としたDFS木を作るぜ
orders = [-1] * v  # そのノードがDFS木において何番目か
parents = [-1] * v  # 根は-1のまま, 各ノードのDFS木上の親を管理
warps = [[] for i in range(v)]

stack = [(0, -1)]  # (ノード番号, 親ノード番号)

order_tmp = 0
order_to_node = {}
while stack:  # データの持ち方に工夫が必要
    tmp, parent = stack.pop()
    if orders[tmp] < 0:
        orders[tmp] = order_tmp
        order_to_node[order_tmp] = tmp
        order_tmp += 1
        for node in next_node_list[tmp]:
            if orders[node] >= 0:  # orderが確定している
                print(tmp, node)
                # ワープをカウントする
                if node != parents[tmp]:
                    warps[tmp].append(node)
            else:  # nodeが未確定である
                stack.append((node, tmp))
                parents[node] = tmp
                

print(orders)
print(parents)
print(warps)
# 葉から遡ってlowestを計算
lowests = copy.deepcopy(orders)  # 自分及び自分の子孫のノードからワープして行ける頂点の中で最もorderが早いもの
for i in range(v - 1, -1, -1):
    tmp = order_to_node[i]
    # ワープで行けるorder最小の点を探す
    for warped_node in warps[tmp]:
        if lowests[tmp] > lowests[warped_node]:
            lowests[tmp] = lowests[warped_node]

    # 配るDPでそのノードのparentに影響させる
    parent = parents[tmp]
    if parent != -1 and lowests[parent] > lowests[tmp]:
        lowests[parent] = lowests[tmp]

print(lowests)
articulation_points = []
# 根である場合
if sum(np.array(parents) == 0) >= 2:
    articulation_points.append(0)
# 根でない
for i in range(1, v):
    for j in next_node_list[i]:
        if parents[j] == i and orders[i] <= lowests[j]:
            articulation_points.append(i)
            break
    


print(articulation_points)

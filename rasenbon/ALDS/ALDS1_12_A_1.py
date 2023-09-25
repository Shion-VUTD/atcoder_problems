# プリムのアルゴリズム
# ある連結グラフの最小全域木を求める問題

n = int(input())
adjacency_metrix = []
for i in range(n):
    adjacency_metrix.append(list(map(int, input().split())))

# 1. 各のーどがブロックに属しているか
is_block = [False] * n
is_block[0] = True

# 2. ブロックからそれに属さないノードがどれだけ離れているか
distances_from_tree_block = [10**4] * n
distances_from_tree_block[0] = 0

# 3. 当該ノード
tmp = 0
ans = 0

while True:
    if sum(is_block) == n:
        break

    for i in range(n):
        # 隣接行列に従って重みを更新
        weight = adjacency_metrix[tmp][i]
        if weight != -1 and is_block[i] == False:
            if weight < distances_from_tree_block[i]:
                distances_from_tree_block[i] = weight

    # blockに属さないのーどのなかで距離最小のものを探索
    min_distance_node = -1
    min_distance = 10**4

    for i in range(n):
        if is_block[i] == False and min_distance > distances_from_tree_block[i]:
            min_distance = distances_from_tree_block[i]
            min_distance_node = i

    # 決まったらそれをblockに追加して、それをtmpとして初めに戻る
    tmp = min_distance_node
    is_block[tmp] = True
    ans += min_distance

print(ans)
print(distances_from_tree_block)

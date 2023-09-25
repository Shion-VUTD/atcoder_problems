"""プリムのアルゴリズム"""

import numpy as np
n = int(input())
next_matrix = [[-1]*n for i in range(n)]
for i in range(n):
    input_arr = list(map(int, input().split()))
    for j in range(n):
        next_matrix[i][j] = input_arr[j]
        next_matrix[j][i] = input_arr[j]

# 探索済みかどうかを示す
is_visited = np.array([False] * n)

# 探索済みノードからなる木からの距離
distances = np.array([2000] * n)

# 木全体の高さ
tree_size = 0

# 当該ノード
distances[0] = 0

# print("Input Ended.")

while True:
    # 全て探索済みの時、試行を終了する
    if np.all(is_visited):
        break

    # 記録された距離のうち最短のものを記録して、そのノードを探索済みにする
    confirmed_distance = 2000
    for i in range(n):
        if is_visited[i] == False:
            if confirmed_distance > distances[i]:
                confirmed_distance = distances[i]
                visited_node = i
    is_visited[visited_node] = True

    # 探索済みにしたノードを当該ノードとする
    tmp_node = visited_node
    tree_size += confirmed_distance
    # print(confirmed_distance, tree_size)

    # 当該ノードに隣接する未探索のノードについて最短距離を更新する
    for i in range(n):
        if next_matrix[tmp_node][i] != -1 and is_visited[i] == False:
            tmp_dis = next_matrix[tmp_node][i]
            if tmp_dis < distances[i]:
                distances[i] = tmp_dis
    
print(tree_size)
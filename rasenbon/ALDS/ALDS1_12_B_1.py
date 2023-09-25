import numpy as np

# ダイクストラ法(単一始点最短経路問題)

n = int(input())
adjacency_list = [[] for i in range(n)]
for i in range(n):
    input_list = list(map(int, input().split()))
    x, num_of_adjacent_node = input_list[0], input_list[1]
    for j in range(num_of_adjacent_node):
        adjacency_list[i].append(input_list[2*(j+1): 2*(j+2)])

# print(adjacency_list)
# 確定した地点かどうか
is_confirmed = np.array([False] * n)

# 始点からの距離
distances = [10 ** 6] * n
distances[0] = 0

while True: # O(n)
    # print(is_confirmed)
    if is_confirmed.all(): # O(n)
        break

    # 未確定の地点のうち距離最小のものを確定させる
    min_distance = 10 ** 6
    min_distance_node = "Unknown"
    for i in range(n): # O(n)
        if is_confirmed[i] == False and min_distance > distances[i]:
            min_distance = distances[i]
            min_distance_node = i
    # print(min_distance_node)
    
    is_confirmed[min_distance_node] = True

    # 確定させた地点について、それに隣接する未確定のノードの距離を更新する
    tmp = min_distance_node
    for adjacency_node, distance in adjacency_list[tmp]: # 合計で最大O(n^2)
        if distances[adjacency_node] > distances[tmp] + distance:
            distances[adjacency_node] = distances[tmp] + distance
    
for i in range(n):
    print(i, distances[i])

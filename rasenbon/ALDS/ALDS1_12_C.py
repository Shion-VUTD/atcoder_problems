"""ダイクストラのアルゴリズム(優先度付きキュー版)"""
import heapq

n = int(input())
next_list = [[] for i in range(n)]
for i in range(n):
    input_list = list(map(int, input().split()))
    k = input_list[1]
    for edge in range(k):
        node, weight = input_list[2*(edge+1)], input_list[2*(edge+1)+1]
        next_list[i].append((node, weight))

# print(next_list)

# 必要なデータ構造を準備(distance: 未確定のノードについて、(きょり, ノード)のタプルを保存した優先度付きキュー)
distance_heap = []
heapq.heappush(distance_heap, (0, 0))
ans_distance = [10**5]*n
is_visited = [False]*n

# 0のノードのdistanceを0にする
ans_distance[0] = 0

# ダイクストラ
while True:
    if distance_heap == []:
        for i in  range(n):
            print(i, ans_distance[i])
        break

    # distance最小のノードをpopし確定させる(logV)
    distance, node = heapq.heappop(distance_heap)
    if is_visited[node]: # if distance > ans_distance[i]: でも良い
        continue
    is_visited[node] = True

    # 確定したノードについて、隣接するノードの重みを更新し、それに応じてdistance_heapも更新する
    for next_node, weight in next_list[node]:
        new_distance = distance + weight
        if is_visited[next_node] == False and ans_distance[next_node] > new_distance:
            ans_distance[next_node] = new_distance
            heapq.heappush(distance_heap, (new_distance, next_node)) # 更新前のノードが残っていても、先に取り出されるのはこちらなので良い

        

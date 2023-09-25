# distancesを優先度つきキューにして保持する
import heapq

n = int(input())
adjacency_list = [[] for i in range(n)]
for i in range(n):
    input_list = list(map(int, input().split()))
    x, num_of_adjacent_node = input_list[0], input_list[1]
    for j in range(num_of_adjacent_node):
        adjacency_list[i].append(input_list[2*(j+1): 2*(j+2)])

# 確定しているかどうか
is_confirmed = [False] * n

# 最短距離を優先度付きキューで管理
# 計算量は
distances = []
heapq.heapify(distances)
heapq.heappush(distances, (0, 0))

# 最終的な最短距離は別で管理
ans_distances = [10**6] * n
ans_distances[0] = 0

while distances: 
    distance, tmp = heapq.heappop(distances) # 全体でO(ElogV): 同じものを合計で辺の数だけキューに入れる可能性がある

    # 未確定のノードのうちで距離最小のものを確定させる
    if is_confirmed[tmp] == False: # 同じものを合計で辺の数だけキューに入れる可能性がある
        is_confirmed[tmp] = True
        
    # そのノードに隣接するノードについて距離を更新
    for next_node, next_distance in adjacency_list[tmp]: # 全体でO(ElogV
        if is_confirmed[next_node] == False and ans_distances[next_node] > ans_distances[tmp] + next_distance:
            ans_distances[next_node] = ans_distances[tmp] + next_distance
            heapq.heappush(distances, (ans_distances[next_node], next_node))

for i in range(n):
    print(i, ans_distances[i])
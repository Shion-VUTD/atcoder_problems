"""ダイクストラのアルゴリズム"""

n = int(input())
next_list = [[] for i in range(n)]
for i in range(n):
    input_list = list(map(int, input().split()))
    k = input_list[1]
    for edge in range(k):
        node, weight = input_list[2*(edge+1)], input_list[2*(edge+1)+1]
        next_list[i].append((node, weight))

# print(next_list)

is_visited = [False]*n
distance = [10**5 + 1]*n

# 最初のノードの距離を0にする
distance[0] = 0

while True:
    # 全て確定済みなら、距離を出力後、探索を終了
    if all(is_visited):
        for i in range(n):
            print(str(i) + ' ' + str(distance[i]))
        break

    # 未確定ノードのうち、distance最小のものを確定とする(ここでVかかってしまうので、全体の計算量はV+EではなくV^2になってしまう)
    min_distance = 10**5 + 1
    for i in range(n):
        if is_visited[i] == False and distance[i] < min_distance:
            min_distance = distance[i]
            min_index = i
    
    is_visited[min_index] = True

    # 確定ノードに隣接するノードについて、最短距離を更新する
    for node, weight in next_list[min_index]:
        new_distance = min_distance + weight
        if distance[node] > new_distance:
            distance[node] = new_distance



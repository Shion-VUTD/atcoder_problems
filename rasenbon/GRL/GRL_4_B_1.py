# トポロジカルソート

v, e = map(int, input().split())

# 入次数を管理
indegrees = [0] * v
# 隣接リスト
next_nodes = [[] for i in range(v)]
for i in range(v):
    x, next_x = map(int, input().split())
    next_nodes[x].append(next_x)
    indegrees[next_x] += 1

# 探索済みのエッジを減らす方針でbfs
sorted_nodes = []
is_visited = [False] * v

for i in range(v):
    if indegrees[i] == 0 and is_visited[i] == False:
        is_visited[i] = True

        # 頂点iを起点として探索開始
        topological_dfs = [i]
        while topological_dfs:
            # print(topological_dfs)
            # print(indegrees)
            tmp = topological_dfs.pop()
            sorted_nodes.append(tmp)
            for node in next_nodes[tmp]:
                indegrees[node] -= 1
                if indegrees[node] == 0 and is_visited[node] == False:
                    topological_dfs.append(node)
                    is_visited[node] = True

print(sorted_nodes)

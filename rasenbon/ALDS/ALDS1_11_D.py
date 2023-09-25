# 隣接リストを作る
n, m = map(int, input().split())
adjacency_list = [[] for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    adjacency_list[x].append(y)
    adjacency_list[y].append(x)

stack = []
is_visited = [-1] * n

for i in range(n):
    if is_visited[i] == -1:
        stack.append(i)
        is_visited[i] = i
        while stack:
            tmp = stack.pop()
            for next_node in adjacency_list[tmp]:
                if is_visited[next_node] == -1:
                    stack.append(next_node)
                    is_visited[next_node] = is_visited[tmp]

# print(is_visited)

q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    if is_visited[x] == is_visited[y]:
        print("yes")
    else:
        print("no")

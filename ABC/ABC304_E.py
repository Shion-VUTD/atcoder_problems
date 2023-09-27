n, m = map(int, input().split())

adjacent_list = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    adjacent_list[u - 1].append(v - 1)
    adjacent_list[v - 1].append(u - 1)

# 連結成分に分ける
roots = list(range(n))
is_visited = [False] * n

for i in range(n):
    if is_visited[i]:
        continue
    stack = [i]
    is_visited[i] = True
    while stack:
        tmp = stack.pop()
        for j in adjacent_list[tmp]:
            if is_visited[j]:
                continue
            is_visited[j] = True
            roots[j] = i
            stack.append(j)

# print(roots)

path_already_exits = False
k = int(input())
question_set = set()
for i in range(k):
    u, v = map(int, input().split())
    root_u = roots[u - 1]
    root_v = roots[v - 1]
    if root_u == root_v:
        path_already_exits = True
        continue
    question_set.add((min(root_u, root_v), max(root_u, root_v)))

q = int(input())
for i in range(q):
    if path_already_exits:
        print("No")
        continue
    p, q = map(int, input().split())
    root_p = roots[p - 1]
    root_q = roots[q - 1]
    if root_p == root_q:
        print("Yes")
    elif (min(root_p, root_q), max(root_p, root_q)) in question_set:
        print("No")
    else:
        print("Yes")
        



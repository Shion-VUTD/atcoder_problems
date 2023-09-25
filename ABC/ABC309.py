n1, n2, m = map(int, input().split())
next_list = [[] for i in range(n1 + n2)]

for i in range(m):
    x, y = map(int, input().split())
    next_list[x-1].append(y-1)
    next_list[y-1].append(x-1)

# print(next_list)

# 0から最も遠い点を調べる
from collections import deque
import numpy

que = deque([0])
is_visited = [-1 for i in range(n1+n2)]
is_visited[0] = 0
#print(is_visited)

while len(que) != 0:
    tmp = que.popleft()
    distance = is_visited[tmp]
    for x in next_list[tmp]:
        if is_visited[x] == -1:
            is_visited[x] = distance + 1
            que.append(x)

#print(is_visited)
#print(max(is_visited))

que = deque([n1+n2-1])
is_visited_another = [-1 for i in range(n1+n2)]
is_visited_another[n1+n2-1] = 0
#print(is_visited)

while len(que) != 0:
    tmp = que.popleft()
    distance = is_visited_another[tmp]
    for x in next_list[tmp]:
        if is_visited_another[x] == -1:
            is_visited_another[x] = distance + 1
            que.append(x)

#print(is_visited_another)
#print(max(is_visited_another))

print(max(is_visited_another) + max(is_visited) + 1)



  
  
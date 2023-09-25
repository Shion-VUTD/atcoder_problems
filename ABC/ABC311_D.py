import numpy as np

h, w = map(int, input().split())
maps = []
for i in range(h):
  maps.append(list(input()))
 

stack = [
  ([1, 1], 0),
  ([1, 1], 1),
  ([1, 1], 2),
  ([1, 1], 3)
]

is_visited = [[[False]*4 for j in range(w)] for i in range(h)]
for i in range(4):
	is_visited[1][1][i] = True

move = [
  (0, 1), (0, -1), (1, 0), (-1, 0) 
]

while stack:
  # print(stack)
  tmp, x = stack.pop()
  new_x, new_y = tmp[0] + move[x][0], tmp[1] + move[x][1]
  if maps[new_x][new_y] == "." and is_visited[new_x][new_y][x] == False:
    is_visited[new_x][new_y][x] = True
    stack.append(([new_x, new_y], x))
  elif maps[new_x][new_y] == "#":
    for y in range(4):
      if x != y:
        new_x, new_y = tmp[0] + move[y][0], tmp[1] + move[y][1]
        if maps[new_x][new_y] == "." and is_visited[new_x][new_y][y] == False:
          is_visited[new_x][new_y][y] = True
          stack.append(([new_x, new_y], y))
    

print(sum([sum([max(is_visited[i][j]) for j in range(w)]) for i in range(h)]))
# print(is_visited)
      
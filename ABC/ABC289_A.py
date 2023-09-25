from collections import deque
import sys

num_tests = int(input())
n, m = map(int, input().split())
red_or_blue = list(map(int, input().split()))

next_list = [[] for i in range(n)]
for i in range(m):
  x, y = map(int, input().split())
  next_list[x-1].append(y-1)
  next_list[y-1].append(x-1)
  
print(next_list)

que = deque([])
que.append((0, n-1))
appeared_scene = {}

while que:
    takahashi, aoki = que.popleft()
    if takahashi == n-1 and aoki == 0:
        print('Yes')
        sys.exit()

    next_takahashi = next_list[takahashi]
    if next_takahashi == []:
        print(-1)
        sys.exit()

    next_takahashi_red = []
    next_takahashi_blue = []
    for node in next_takahashi:
        if red_or_blue[node] == 0:
            next_hakatashi_red.append(node)
        else:
            next_hakatashi_blue.append(node)

    next_aoki = next_list[aoki]
    next_aoki_red = []
    next_aoki_blue = []
    for node in next_aoki:
        if red_or_blue[node] == 0:
            next_aoki_red.append(node)
        else:
            next_aoki_blue.append(node)
    
    if next_takahashi_red == []:
        if next_aoki_red == []:
            print(-1)
            sys.exit()
        else:
            





  
  


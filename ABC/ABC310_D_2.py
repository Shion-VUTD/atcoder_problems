from collections import deque
import copy

n, t, m = map(int, input().split())
hate_members = [[] for i in range(n)]

for i in range(m):
  x, y = map(int, input().split())
  hate_members[y-1].append(x-1)
  hate_members[x-1].append(y-1)

que = deque([])
start = [-1] * n

# 最初はチーム0に
start[0] = 0
que.append((start, 1)) # 1番目の人からチーム決まってない

ans = 0

while que:
    division, visited_id = que.pop()
    if visited_id == n:
        teams = [False] * t
        for team in division:
            teams[team] = True
        if sum(teams) == t:
            ans += 1
            
    else:
        is_appendable = [True]*t
        already_divided_teams = set(division)
        for member in hate_members[visited_id]:
            team = division[member]
            if team != -1:
                is_appendable[team] = False

        # 既に探索済みのチームとそうでないチームに分ける
        is_first_team = True
        for team in range(t):
            if is_appendable[team]:
                if team in already_divided_teams:
                    new_division = copy.deepcopy(division)
                    new_division[visited_id] = team
                    que.append((new_division, visited_id+1))
                elif is_first_team:
                    new_division = copy.deepcopy(division)
                    new_division[visited_id] = team
                    que.append((new_division, visited_id+1))
                    is_first_team = False
                else:
                    continue

                

print(ans)



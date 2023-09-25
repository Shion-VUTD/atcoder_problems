import math
import numpy as np

n, t, m = map(int, input().split())
hate_members = [[] for i in range(n)]

for i in range(m):
  x, y = map(int, input().split())
  hate_members[y-1].append(x-1)
  hate_members[x-1].append(y-1)

hate_members = np.array(hate_members)
print(hate_members)
  
num_hate_members = [len(hate_members[i]) for i in range(n)]
max_hate_members = max(num_hate_members)
max_num_teams = max_hate_members + 1

# 1~tチームを使ったチーム分けの個数を考える
ans_for_nums_teams = [-1 for i in range(t)]
sum_for_nums_teams = [-1 for i in range(t)]
for num_teams in range(1, t+1):
  if num_teams < max_num_teams:""
    ans_for_nums_teams[num_teams-1] = 0
    sum_for_nums_teams[num_teams-1] = 0
  else:
    ans_tmp = 1
    for i in range(n):
    	ans_tmp *= (num_teams - np.sum(np.array(hate_members[i]) < i))
    sum_for_nums_teams[num_teams-1] = ans_tmp
    if num_teams != 1:
    	ans_for_nums_teams[num_teams-1] = ans_tmp - sum_for_nums_teams[num_teams-2]

ans_for_nums_teams = np.array(ans_for_nums_teams)

# 各チーム数の分割において、そのチーム分けがどれだけ重複カウントされているか？
multi_counts = [0] * t
for num_teams in range(1, t+1):
    multi_counts[num_teams-1] = math.perm(t, num_teams)

multi_counts = np.array(multi_counts)

print(ans_for_nums_teams)
print(multi_counts)
print(ans_for_nums_teams % multi_counts)
print(np.sum(ans_for_nums_teams // multi_counts))


  

 
  
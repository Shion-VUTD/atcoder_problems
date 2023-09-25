import numpy as np

n, d = map(int, input().split())
suchedules = np.array([np.array([0]*d) for i in range(n)])
for i in range(n):
  schedule = input()
  for j, is_ok in enumerate(schedule):
    if is_ok == "o":
      suchedules[i][j] = 1
# print(suchedules)

all_schedule = list(np.sum(suchedules, axis=0))
# print(all_schedule)

all_schedule.append(0)
max_length = 0
flag = 0
for i in range(d+1):
  # print("flag:", flag)
  if all_schedule[i] == n:
    flag += 1
  elif flag != 0:
    if max_length < flag:
      max_length = flag
    flag = 0

print(max_length)
      
                    



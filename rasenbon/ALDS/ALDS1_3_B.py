n, q = map(int, input().split())
job_dict = {}
for i in range(n):
    name, time = input().split()
    time = int(time)
    job_dict[name] = time

from collections import deque
que = deque([])

for name in job_dict.keys():
    que.append((name, job_dict[name]))

ans = 0
while que:
    name, time = que.popleft()
    if time <= q:
        ans += time
        print(name, ans)
    else:
        time -= 100
        ans += 100
        que.append((name, time))


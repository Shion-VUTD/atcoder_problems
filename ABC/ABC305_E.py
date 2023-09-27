import heapq

n, m, k = map(int, input().split())
adjacency_list = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adjacency_list[a - 1].append(b - 1)
    adjacency_list[b - 1].append(a - 1)

strengths = [-1] * n

for _ in range(k):
    p, h = map(int, input().split())
    strengths[p - 1] = h

strengths_priority_queue = []
heapq.heapify(strengths_priority_queue)

for i, strength in enumerate(strengths):
    heapq.heappush(strengths_priority_queue, (-strength, i))

# print(strengths_priority_queue)
verified = [False] * n

while strengths_priority_queue:
    tmp_strength, tmp_id = heapq.heappop(strengths_priority_queue)
    tmp_strength = -tmp_strength
    if tmp_strength == -1:
        break
    if verified[tmp_id]:
        continue
    verified[tmp_id] = True
    for i in adjacency_list[tmp_id]:
        if verified[i]:
            continue
        strengths[i] = max([strengths[i], tmp_strength - 1])
        if strengths[i] == tmp_strength - 1:
            heapq.heappush(strengths_priority_queue, (-strengths[i], i))

ans = []
for i in range(n):
    if strengths[i] != -1:
        ans.append(i + 1)

print(len(ans))
print(" ".join(map(str, ans)))



    
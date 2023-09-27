import numpy as np

n, m = map(int, input().split())
parents = list(map(int, input().split()))
insurances = [-1] * n

for i in range(m):
    person, insurant_people = map(int, input().split())
    insurances[person - 1] = max([insurant_people, insurances[person - 1]])

# print(insurances)
for i in range(1, n):
    parent = parents[i - 1]
    insurances[i] = max([insurances[i], insurances[parent - 1] - 1])

insurances = np.array(insurances)
print(sum(insurances >= 0))

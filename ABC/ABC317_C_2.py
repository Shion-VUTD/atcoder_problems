import itertools

n, m = map(int, input().split())
edge_costs = [[-1] * n for i in range(n)]
for i in range(n):
    edge_costs[i][i] = 0

for i in range(m):
    left, right, cost = map(int, input().split())
    edge_costs[left - 1][right - 1] = cost
    edge_costs[right - 1][left - 1] = cost

p_iters = itertools.permutations(range(n))
longest_path = -1
for p in p_iters:
    path_tmp = 0
    for i in range(n - 1):
        if edge_costs[p[i]][p[i + 1]] == -1:
            break
        else:
            path_tmp += edge_costs[p[i]][p[i + 1]]
    longest_path = max([longest_path, path_tmp])

print(longest_path)        
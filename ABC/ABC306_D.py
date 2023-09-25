n = int(input())
tastes = []
is_poisons = []
for i in range(n):
    a, b = map(int, input().split())
    tastes.append(b)
    is_poisons.append(a)

maximum_tastes = [[-1] * 2 for i in range(n+1)]
maximum_tastes[0][1] = 0

for i in range(1, n + 1):
    if is_poisons[i-1]:
        maximum_tastes[i][0] = max([maximum_tastes[i-1][1] + tastes[i-1], maximum_tastes[i-1][0]])
        maximum_tastes[i][1] = maximum_tastes[i-1][1]
    else:
        maximum_tastes[i][0] = maximum_tastes[i-1][0]
        maximum_tastes[i][1] = max([maximum_tastes[i-1][0] + tastes[i-1], maximum_tastes[i-1][1], maximum_tastes[i-1][1] + tastes[i-1]])

print(max([maximum_tastes[n][0], maximum_tastes[n][1]]))

n, d = map(int, input().split())
points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append([x, y])

ditsnces = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        ditsnces[i][j] = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2

# print(ditsnces)

stack = [0]
is_visited = [False] * n
while stack:
    now = stack.pop()
    for i in range(n):
        if is_visited[i] is False and ditsnces[now][i] <= d**2:
            stack.append(i)
            is_visited[i] = True

for i in range(n):
    if is_visited[i]:
        print("Yes")
    else:
        print("No")
    



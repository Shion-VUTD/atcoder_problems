from collections import defaultdict

n, m = map(int, input().split())
adjacent_dict = defaultdict(list)

for i in range(m):
    a, b, gap_x, gap_y = map(int, input().split())
    adjacent_dict[a].append((b, gap_x, gap_y))
    adjacent_dict[b].append((a, -gap_x, -gap_y))

stack = [1]
coordinates = ["undeciable"] * (n + 1)
coordinates[1] = (0, 0)

while stack:
    tmp = stack.pop()
    for next_node, gap_x, gap_y in adjacent_dict[tmp]:
        if coordinates[next_node] != "undeciable":
            continue
        coordinates[next_node] = (
            coordinates[tmp][0] + gap_x,
            coordinates[tmp][1] + gap_y,
        )
        stack.append(next_node)

for i in range(1, n + 1):
    if coordinates[i] == "undeciable":
        print("undecidable")
        
    else:
        print(coordinates[i][0], coordinates[i][1])

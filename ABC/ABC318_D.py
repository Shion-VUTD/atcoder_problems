n = int(input())
distances = [[0] * n for i in range(n)]

for i in range(n-1):
    lists = list(map(int, input().split()))
    for j in range(i+1, n):
        distances[i][j] = lists[j - i - 1]

#print(distances)

max_length_paths = [-1] * (2 ** (n))
max_length_paths[0] = 0

for x in range(1, 2 ** (n)):
    ans = 0
    nodes = []
    for i in range(n):
        if (x >> i) & 1:
            nodes.append(i)
    # print(nodes)
    if len(nodes) % 2 == 1:
        for node in nodes:
            y = x - (2 ** node)
            # print("y:", y)
            if ans < max_length_paths[y]:
                ans = max_length_paths[y]
                # print("ans:", ans)
    else:
        # print(x)
        for i, node_1 in enumerate(nodes):
            for j, node_2 in enumerate(nodes[i + 1:]):
                y = x - (2 ** node_1) - (2 ** node_2)
                if ans < max_length_paths[y] + distances[node_1][node_2]:
                    ans = max_length_paths[y] + distances[node_1][node_2]
                    

    max_length_paths[x] = ans

print(max_length_paths[-1])
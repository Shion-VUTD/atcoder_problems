h, w = map(int, input().split())
maps = []
for i in range(h):
    maps.append(input())

is_visited = [[False] * w for _ in range(h)]
is_visited[0][0] = True

snuke = ["s", "n", "u", "k", "e"]
nexts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
if maps[0][0] != "s":
    print("No")
    exit()

stack = [(0, 0, 0)]
while stack:
    # print(stack)
    tmp = stack.pop()
    if tmp[0] == h - 1 and tmp[1] == w - 1:
        print("Yes")
        exit()
    
    for (plus_x, plus_y) in nexts:
        x = tmp[0] + plus_x
        y = tmp[1] + plus_y
        
        if x < 0 or x >= h or y < 0 or y >= w:
            continue
        if is_visited[x][y]:
            continue
        if maps[x][y] == snuke[(tmp[2] + 1) % 5]:
            is_visited[x][y] = True
            stack.append((x, y, (tmp[2] + 1) % 5))
            

print("No")

            

        


        
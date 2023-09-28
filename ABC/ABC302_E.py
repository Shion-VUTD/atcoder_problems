n, q = map(int, input().split())
adjacent_list = [set([]) for _ in range(n)]
ans = n

for _ in range(q):
    query = list(map(int, input().split()))
    command = query[0]
    if command == 1:
        a, b = query[1] - 1, query[2] - 1
        adjacent_list[a].add(b)
        adjacent_list[b].add(a)
        if len(adjacent_list[a]) == 1:
            ans -= 1
        if len(adjacent_list[b]) == 1:
            ans -= 1
        print(ans)
            
    elif command == 2:
        a = query[1] - 1
        if len(adjacent_list[a]) != 0:
            ans += 1
        for next_node in adjacent_list[a]:
            adjacent_list[next_node].discard(a)
            if len(adjacent_list[next_node]) == 0:
                ans += 1
        adjacent_list[a] = set([])
        print(ans)





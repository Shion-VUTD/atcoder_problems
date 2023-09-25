n, m = map(int, input().split())
strongest = [True] * n

strong_list = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    strong_list[a-1].append(b-1)
    strongest[b-1] = False


if strongest.count(True) == 1:
    print(strongest.index(True) + 1)
else:
    print(-1)
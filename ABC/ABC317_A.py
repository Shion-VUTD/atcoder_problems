n, h, x = map(int, input().split())
gap = x - h

medicine = list(map(int, input().split()))

i = 0
while True:
    if i == n:
        break
    if medicine[i] >= gap:
        print(i + 1)
        exit()
    i += 1
    
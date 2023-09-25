from bisect import bisect_left, bisect_right

n, m, d = map(int, input().split())
aoki = list(map(int, input().split()))
snuke = list(map(int, input().split()))

aoki.sort()
snuke.sort()

ans = -1
for i in range(m-1, -1, -1):
    index_left = bisect_left(aoki, snuke[i] - d)
    index_right = bisect_right(aoki, snuke[i] + d)
    if index_left == index_right:
        continue
    ans = max([ans, snuke[i] + aoki[index_right - 1]])

print(ans)
    

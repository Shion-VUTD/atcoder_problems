n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))
s.append(-1)
s.append(10**9 + 1)

s.sort()
t.sort()
ans = 0

for i, x in enumerate(t):
    # leftは常にxより小、rightは常にx以上
    # right - leftが1になったとき、rightがその整数であればOK
    left = 0
    right = n
    while right - left > 1:
        middle = (left + right) // 2
        if s[middle]< x:
            left = middle
        elif s[middle] >= x:
            right = middle

    if s[right] == x:
        ans += 1

print(ans)
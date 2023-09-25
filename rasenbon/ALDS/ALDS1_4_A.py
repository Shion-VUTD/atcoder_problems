n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

s.sort()
t.sort()
ans = 0
flag = 0

for i, x in enumerate(s):
    for j in range(flag, q):
        if t[j] == x:
            ans += 1
            flag = j + 1
            break
        
        elif t[j] > x:
            flag = j
            break
        
print(ans)
    
    





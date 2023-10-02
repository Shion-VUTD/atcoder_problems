from bisect import bisect_left

n, m = map(int, input().split())
fireworks = list(map(int, input().split())) 

for i in range(n):
    print(fireworks[bisect_left(fireworks, i+1)] - (i + 1))
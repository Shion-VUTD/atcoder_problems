n = int(input())
ints = list(map(int, input().split()))
max_int = max(ints)
min_int = min(ints)

total = (max_int + min_int) * (n + 1) // 2
print(total - sum(ints))
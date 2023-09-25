from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

nums_dict = defaultdict(list)

for i, num in enumerate(nums):
    nums_dict[num].append(i + 1)

print(" ".join(map(str, sorted(nums_dict.keys(), key=lambda x: nums_dict[x][1]))))
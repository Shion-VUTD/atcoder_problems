import numpy as np

n = int(input())

nums = list(map(int, input().split()))
nums.sort()
nums = np.array(nums)

total = np.sum(nums)
x = total // n
y = total % n

nums_future = [x] * (n - y) + [x + 1] * y
nums_future = np.array(nums_future)

print(np.sum(np.abs(nums - nums_future)) // 2)

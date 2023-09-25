from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

nums_and_ids = {}
cumulative_sum = defaultdict(int)


# print(nums_and_ids)

num_sandwiches = 0
for i, num in enumerate(nums):
    if num not in nums_and_ids.keys():
        nums_and_ids[num] = [i]
    else:
        num_sandwiches += (
            (i - 1) * len(nums_and_ids[num]) - cumulative_sum[num] - (len(nums_and_ids[num]) * (len(nums_and_ids[num]) - 1)) // 2
        )
        nums_and_ids[num].append(i)
    cumulative_sum[num] += i

print(num_sandwiches)
    
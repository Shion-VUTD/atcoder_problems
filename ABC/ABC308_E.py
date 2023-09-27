from collections import defaultdict
n = int(input())

nums = list(map(int, input().split()))
mexes = input()

dp_dict = defaultdict(int)
whole = {0, 1, 2, 3}
ans = 0

for i in range(n):
    # print(dp_dict)
    num = nums[i]
    char = mexes[i]
    if char == "M":
        dp_dict[(num,)] += 1
    elif char == "E":
        for i in range(3):
            dp_dict[(min([i, num]), max([i, num]))] += dp_dict[(i, )]
    elif char == "X":
        for num_tuple in dp_dict.keys():
            # print(num_tuple)
            if len(num_tuple) == 2:
                num_set = set(num_tuple)
                num_set.add(num)
                num_rests = whole - num_set
                ans += min(num_rests) * dp_dict[num_tuple]



print(ans)
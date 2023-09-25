from collections import defaultdict
import bisect

w, h = map(int, input().split())
n = int(input())
berries = []
for i in range(n):
    x, y = map(int, input().split())
    berries.append((x, y))
a = int(input())
cut_x = [0] + list(map(int, input().split()))
b = int(input())
cut_y = [0] + list(map(int, input().split()))

berries_blocks = defaultdict(int)

def decide_which_block_to_belong(berries, cut_x, cut_y):
    berries_x, berries_y = berries
    index_x = bisect.bisect(cut_x, berries_x) - 1
    block_x = cut_x[index_x]
    index_y = bisect.bisect(cut_y, berries_y) - 1
    block_y = cut_y[index_y]
    return (block_x, block_y)

for berry in berries:
    berries_blocks[decide_which_block_to_belong(berry, cut_x, cut_y)] += 1

# print(berries_blocks)
min_berries = 0
if len(berries_blocks) == (a + 1) * (b + 1):
    min_berries = min(berries_blocks.values())

print(min_berries, max(berries_blocks.values()))
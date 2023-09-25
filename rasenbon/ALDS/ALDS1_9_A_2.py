n = int(input())

binary_heap = list(map(int, input().split()))

for i in range(n):
    ans = []
    node = i + 1
    ans.append("node {}:".format(node))

    key = binary_heap[i]
    ans.append("key = {},".format(key))

    if i != 0:
        parent_key = binary_heap[(i-1)//2]
        ans.append("parent key = {},".format(parent_key))
    
    left_id = 2 * i + 1
    if left_id <= n - 1:
        left_key = binary_heap[left_id]
        ans.append("left key = {},".format(left_key))

    right_id = 2 * i + 2
    if right_id <= n - 1:
        right_key = binary_heap[right_id]
        ans.append("right key = {},".format(right_key))

    print(" ".join(ans))


    

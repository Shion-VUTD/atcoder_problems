n = int(input())
binary_heap = list(map(int, input().split()))

for i in range(n):
    print("node " + str(i+1) + ": key = " + str(binary_heap[i]), end = ', ')
    if i != 0:
        parent = binary_heap[(i - 1) // 2]
        print("parent key = " + str(parent), end=', ')
    
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n:
        print("left key = " + str(binary_heap[left_child]), end = ', ')
    if right_child < n:
        print("right key = " + str(binary_heap[right_child]), end = ',')

    print('\n')
    

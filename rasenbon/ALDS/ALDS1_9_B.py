n = int(input())
heap = list(map(int, input().split()))

target_id = n // 2 - 1
while target_id >= 0:
    target = heap[target_id]
    tmp_id = target_id
    while tmp_id * 2 + 1 < n:
        left_child_id = tmp_id * 2 + 1
        right_child_id = tmp_id * 2 + 2
        if right_child_id < n and heap[right_child_id] > heap[left_child_id] and heap[right_child_id] > heap[tmp_id]:
            heap[tmp_id] = heap[right_child_id]
            tmp_id = right_child_id
            heap[right_child_id] = target
        elif heap[left_child_id] > heap[tmp_id]:
            heap[tmp_id] = heap[left_child_id]
            tmp_id = left_child_id
            heap[left_child_id] = target
        else:
            break;

    target_id -= 1

print(' ' + ' '.join(map(str, heap))) 
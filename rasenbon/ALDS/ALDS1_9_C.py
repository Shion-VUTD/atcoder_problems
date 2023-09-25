from collections import deque
priority_queue = []

def insert(number):
    n = len(priority_queue)
    priority_queue.append(number)
    tmp_id = n

    while (tmp_id > 0):
        parent_id = (tmp_id - 1) // 2
        if priority_queue[parent_id] < number:
            priority_queue[tmp_id] = priority_queue[parent_id]
            priority_queue[parent_id] = number
        else:
            break
        tmp_id = parent_id
    # print(priority_queue)

    
def extractmax():
    n = len(priority_queue)
    last_value = priority_queue[n - 1]
    top_value = priority_queue[0]
    priority_queue[0] = last_value
    priority_queue.pop()
    
    tmp_id = 0
    while tmp_id * 2 + 1 < n - 1:
        left_child_id = tmp_id * 2 + 1
        right_child_id = tmp_id * 2 + 2
        target = priority_queue[tmp_id]

        if right_child_id < n - 1 and priority_queue[right_child_id] > priority_queue[left_child_id] and priority_queue[right_child_id] > target:
            priority_queue[tmp_id] = priority_queue[right_child_id]
            tmp_id = right_child_id
            priority_queue[right_child_id] = target
        elif priority_queue[left_child_id] > priority_queue[tmp_id]:
            priority_queue[tmp_id] = priority_queue[left_child_id]
            tmp_id = left_child_id
            priority_queue[left_child_id] = target
        else:
            break

    print(top_value)

while True:
    s = input()
    if s == "end":
        break
    elif s == "extract":
        extractmax()
    else:
        command, x = s.split()
        insert(int(x))



    





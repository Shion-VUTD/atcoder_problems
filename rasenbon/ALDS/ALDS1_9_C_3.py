import heapq

priority_queue = []

# heapq.heapify()は返り値を持たない破壊的なタイプの関数。
heapq.heapify(priority_queue)
print(type(priority_queue))

while True:
    cmd = input()
    if cmd == "end":
        break
    elif cmd == "extract":
        tmp = heapq.heappop(priority_queue)
        print(-1 * tmp)
    else:
        ins, num = cmd.split()
        heapq.heappush(priority_queue, -1 * int(num))

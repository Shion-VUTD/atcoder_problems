import heapq

n, k, q = map(int, input().split())
priority_queue = []
a_list = [0] * n

heapq.heapify(priority_queue)
for i in range(n):
    heapq.heappush(priority_queue, (0, i))

print(priority_queue)
ans = 0

for i in range(q):
    x, y = map(int, input().split())
    a_tmp = a_list[x-1]
    # k番目の値を持っておく
    a_border = priority_queue[k-1]

    print(a_border)
    if a_border > (-a_tmp, x-1) and a_border > (-y, x-1):
        k += 1
        print("case 1")
        ans += (y - a_tmp)
    elif a_border > (-a_tmp, x-1) and a_border < (-y, x-1):
        print("case 2")
        ans += (-priority_queue[k][0] - a_tmp)
    elif a_border < (-a_tmp, x-1) and a_border < (-y, x-1):
        print("case 3")
        ans += (y - (-priority_queue[k-1][0]))
    heapq.heappush(priority_queue, (-y, x-1))
    a_list[x-1] = y

    print(ans, priority_queue)


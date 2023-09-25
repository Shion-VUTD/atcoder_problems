import bisect

n = int(input())
sleep_rec = list(map(int, input().split()))
total_sleep_rec = []
total_sleep_rec.append(0)
total_sleep_rec.append(0)
for i in range(2, n):
    if i % 2 == 0:
        total_sleep_rec.append(total_sleep_rec[-1] + sleep_rec[i] - sleep_rec[i-1])
    else:
        total_sleep_rec.append(total_sleep_rec[-1])

# print(total_sleep_rec)

q = int(input())
for i in range(q):
    l_sleep, r_sleep = map(int, input().split())
    l = bisect.bisect(sleep_rec, l_sleep) - 1
    r = bisect.bisect(sleep_rec, r_sleep) - 1
    # print(l, r)
    if l % 2 == 0:
        l_total_sleep = total_sleep_rec[l] 
    else:
        l_total_sleep = total_sleep_rec[l] + l_sleep - sleep_rec[l]

    if r % 2 == 0:
        r_total_sleep = total_sleep_rec[r]
    else:
        r_total_sleep = total_sleep_rec[r] + r_sleep - sleep_rec[r]

    print(r_total_sleep - l_total_sleep)

from bisect import bisect_right

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()

a_total = [0]
for i, a_tmp in enumerate(a):
    a_total.append(a_total[i] + a_tmp)

# print(a_total)

def cal_tmp_total(b_tmp):
    inserted_id = bisect_right(a, p - b_tmp)
    return a_total[inserted_id] + b_tmp * inserted_id + p * (n - inserted_id)

ans = 0
for b_tmp in b:
    # print(cal_tmp_total(b_tmp))
    ans += cal_tmp_total(b_tmp)

print(ans)
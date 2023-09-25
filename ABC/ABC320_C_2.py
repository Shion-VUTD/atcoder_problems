import itertools

m = int(input())
s1 = input()
s2 = input()
s3 = input()

appeared_nums_s1 = {}
appeared_nums_s2 = {}
appeared_nums_s3 = {}

for i, x in enumerate(s1):
    if x not in appeared_nums_s1.keys():
        appeared_nums_s1[x] = [i]
    else:
        appeared_nums_s1[x].append(i)

for i, x in enumerate(s2):
    if x not in appeared_nums_s1.keys():
        continue
    else:
        if x not in appeared_nums_s2.keys():
            appeared_nums_s2[x] = [i]
        else:
            appeared_nums_s2[x].append(i)

for i, x in enumerate(s3):
    if x not in appeared_nums_s2.keys():
        continue
    else:
        if x not in appeared_nums_s3.keys():
            appeared_nums_s3[x] = [i]
        else:
            appeared_nums_s3[x].append(i)

def cal_earliest_point(mod, remainders, now):
    # now以上の数字で、modで割った余りがremaindersのいずれかになる最小の数字を返す
    now_rem = now % mod
    now_quo = now // mod
    for remainder in remainders:
        if remainder >= now_rem:
            return remainder + mod * now_quo
    return remainders[0] + mod * (now_quo + 1)

            
slots = [appeared_nums_s1, appeared_nums_s2, appeared_nums_s3]
slot_orders = list(itertools.permutations(range(3)))

if len(appeared_nums_s3.keys()) == 0:
    print(-1)
    exit()

ans = 10**13
for num in appeared_nums_s3.keys():
    # print(num)
    for slot_order in slot_orders:
        slot_first = slots[slot_order[0]][num]
        slot_second = slots[slot_order[1]][num]
        slot_third = slots[slot_order[2]][num]
        # print(slot_first, slot_second, slot_third)

        now = 0
        now = cal_earliest_point(m, slot_first, now)
        now = cal_earliest_point(m, slot_second, now + 1)
        now = cal_earliest_point(m, slot_third, now + 1)
        ans = min([ans, now])
    
    # print(f"ans of num {num}: {ans}")

print(ans)



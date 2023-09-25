n, d, p = map(int, input().split())
daily_charges = list(map(lambda x: -int(x), input().split())) 

q = d - (n % d)
for i in range(q):
    daily_charges.append(0)

daily_charges.sort()
# print(daily_charges)
ans = 0
is_daily_pass = True

# 上から辿っていく
for i in range(0, n, d):
    d_days_charge = -sum(daily_charges[i:i + d])
    if is_daily_pass is False:
        ans += (d_days_charge)
        # print(d_days_charge)
    
    elif (d_days_charge) > p:
        ans += p
        # print(p)

    else:
        ans += (d_days_charge)
        is_daily_pass = False

        # print(d_days_charge)
        
print(ans)
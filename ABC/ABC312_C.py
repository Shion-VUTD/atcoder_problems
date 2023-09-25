update_values = []

n, m = map(int, input().split())
sell_values = list(map(int, input().split()))
buy_values = list(map(int, input().split()))

for i in range(n):
    update_values.append((sell_values[i], 0))
for i in range(m):
    update_values.append((buy_values[i] + 1, 1))

update_values.sort()

# print(update_values)

sell_tmp = 0
buy_tmp = m

for i in range(n+m):
    if update_values[i][1] == 0:
        sell_tmp += 1
    else:
        buy_tmp -= 1
    # print(sell_tmp, buy_tmp)
    if sell_tmp >= buy_tmp:
        print(update_values[i][0])
        exit()
n = int(input())
bet_list = []
bet_num_list = []

for i in range(n):
    c = int(input())
    bet_num_list.append(c)
    a = set(map(int, input().split()))
    bet_list.append(a)

x = int(input())

# print(bet_list)
# print(bet_num_list)
# print(x)

bet_x_ids = []

min_num = 38
for i in range(n):
    if x in bet_list[i]:
        bet_x_ids.append(i)
        if bet_num_list[i] < min_num:
            min_num = bet_num_list[i]

bet_x_min_ids = []
for i in bet_x_ids:
    if bet_num_list[i] == min_num:
        bet_x_min_ids.append(i+1)

print(len(bet_x_min_ids))
print(" ".join(map(str, bet_x_min_ids)))        
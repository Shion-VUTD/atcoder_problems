n = int(input())

like_numbers = []
num_list = list(range(10))

for x in range(1, 2 ** 10):
    tmp = []
    for i in range(10):
        if ((x >> i) & 1):
            tmp.append(str(num_list[9 - i]))
    like_numbers.append(int("".join(tmp)))

# print(len(set(like_numbers)))

like_numbers.sort()
# print(like_numbers[0])
print(like_numbers[n])
    


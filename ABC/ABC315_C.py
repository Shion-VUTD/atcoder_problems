n = int(input())
flavors = []
for i in range(n):
    flover, taste = map(int, input().split())
    flavors.append([taste, flover])

flavors.sort(reverse=True)

taste_init, flavor_init = flavors[0]
if flavor_init != flavors[1][1]:
    print(taste_init + flavors[1][0])
    exit()
else:
    max_tmp = taste_init + flavors[1][0] // 2
    if n == 2:
        print(max_tmp)
        exit()
    for i in range(2, n):
        taste_i, flavor_i = flavors[i]
        if flavor_i != flavor_init:
            print(max([max_tmp, taste_i + taste_init]))
            exit()
    print(max_tmp)
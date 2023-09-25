def cal_ans(n, x, k):
    n_len = len(bin(n)[2:])
    x_bin = bin(x)[2:]
    x_len = len(x_bin)

    ans = 0
    # print(x_bin)

    for freq in range(x_len):
        if freq == k:
            ans += 1
            # print(freq, "pattern 1", ans)
            break
        if (x_len + k - freq * 2) < n_len:
            if freq == 0:
                ans += 2 ** k
                continue
            ans += 2 ** (k - freq - 1)
            # print(freq, "pattern 2", ans)
        elif (x_len + k - freq * 2) > n_len:
            # print(freq, "pattern 3", ans)
            continue
        else:
            if freq == 0:
                y_min = x << k
                y_max = y_min + 2 ** k - 1
                ans += max([0, min([n - y_min + 1, y_max - y_min + 1])])
                # print(freq, y_min, y_max, "pattern 5", ans)
                continue

            y = (x >> (freq - 1))
            if (y & 1):
                y -= 1
            else:
                y += 1

            y_min = y << (k - freq - 1)
            y_max = y_min + 2 ** (k - freq - 1) - 1
            ans += max([0, min([n - y_min + 1, y_max - y_min + 1])])
            #print(freq, y_min, y_max,  "pattern 4", ans)
    
    return ans

t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    print(cal_ans(n, x, k))






            


        
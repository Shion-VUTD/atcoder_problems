# もらうDP
def fib_1(n):
    fib_arr = [0] * (n + 1)
    fib_arr[0] = 1
    if n >= 1:
        fib_arr[1] = 1
    if n >= 2:
        for i in range(2, n + 1):
            fib_arr[i] = fib_arr[i - 1] + fib_arr[i - 2]

    return fib_arr[-1]


# 配るDP
def fib_2(n):
    fib_arr = [0] * (n + 2)
    fib_arr[0] = 1
    for i in range(n):
        fib_arr[i + 1] += fib_arr[i]
        fib_arr[i + 2] += fib_arr[i]

    return fib_arr[-2]


n = int(input())
print(fib_1(n))
print(fib_2(n))

n = int(input())

memo = [-1] * (n + 1)

# メモ化再帰:　計算途中で求めた値をメモするだけ。あとは普通の再帰。
def fib_topdown(i): # i番目のフィボナッチ数列の値(0-indexed)
    if memo[i] != -1:
        return memo[i]
    elif i == 0:
        memo[i] = 1
        return 1
    elif i == 1:
        memo[i] = 1
        return 1
    else:
        ans = fib_topdown(i-1) + fib_topdown(i-2)
        memo[i] = ans
        return ans


print(fib_topdown(n))

# 動的計画法ボトムアップ方式: 1番目から順番に埋めていく
memo = [-1] * (n + 1)

def fib_bottomup(i):
    memo[0] = 1
    memo[1] = 1
    if i == 0 or i == 1:
        return 1
    else:
        for j in range(2, i + 1):
            memo[j] = memo[j-1] + memo[j-2]
    return memo[i]

print(fib_bottomup(n))

assert fib_topdown(n) == fib_bottomup(n)
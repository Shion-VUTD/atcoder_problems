# 計数ソートの実装
# その数以下の数がどれだけあるかを保持しておく

def countingsort(A, k):
    """
    A: 入力行列
    k: 0以上k以下の数字を並べ替える
    """

    #　出力行列
    n = len(A)
    B = [-1] * n
    print(n)
    # 0からkまでの数iについて、i以下の数の個数をC[i]に記載

    C = [0] * (k + 1)
    for i in range(n):
        C[A[i]] += 1

    for i in range(k):
        C[i + 1] = C[i] +  C[i + 1]

    for i in range(n):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    
    return B


n = int(input())
nums = list(map(int, input().split()))
k = max(nums)
print(' '.join(map(str, countingsort(nums, k))))

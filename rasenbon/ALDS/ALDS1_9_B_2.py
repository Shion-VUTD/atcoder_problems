def maxheapify(A, i):
    # 配列Aの、根をi番目の要素とする部分木を二分ヒープにする関数
    ith_key = A[i]
    left_id = i * 2 + 1
    right_id = i * 2 + 2
    if left_id < len(A):
        left_key = A[left_id]
    else:
        left_key = - 10 ** 10
    if right_id < len(A):
        right_key = A[right_id]
    else:
        right_key = - 10 ** 10
    
    if left_key > ith_key and left_key >= right_key:
        A[i] = left_key
        A[left_id] = ith_key
        maxheapify(A, left_id)
    elif right_key > ith_key and left_key < right_key:
        A[i] = right_key
        A[right_id] = ith_key
        maxheapify(A, right_id)

def buildmaxheap(A):

    start = (len(A) - 1) // 2
    for i in range(start, -1, -1):
        maxheapify(A, i)

n = int(input())
A = list(map(int, input().split()))
buildmaxheap(A)
print(" " + " ".join(map(str, A)))
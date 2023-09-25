# マージソートの実装

def merge(A, left, middle, right):
    ans = 0
    line_left = A[left: middle]
    line_right = A[middle: right]
    left_i = -1 # left_i番目までマージしたという目標
    right_i = -1  # right_i番目までマージしたという目標

    while True:
        if left_i == middle - left - 1 and right_i == right - middle - 1:
            break
        elif left_i == middle - left - 1 and right_i < right - middle - 1: # 右側がまだ終わってない
            A[left + left_i + right_i + 2] = line_right[right_i + 1]
            right_i += 1
            ans += 1
        elif left_i < middle - left - 1 and right_i == right - middle - 1: #左側がまだ終わってない
            A[left + left_i + right_i + 2] = line_left[left_i + 1]
            left_i += 1
            ans += 1 
        elif line_left[left_i + 1] >= line_right[right_i + 1]:
            A[left + left_i + right_i + 2] = line_right[right_i + 1]
            right_i += 1
            ans += 1
        else:
            A[left + left_i + right_i + 2] = line_left[left_i + 1]
            left_i += 1
            ans += 1
    return ans


def mergesort(A, left, right): #数列Aのleft番目からからright-1番目までをソートする
    if right - left == 1:
        return 0

    middle = (left + right) // 2 
    ans_left = mergesort(A, left, middle) #　前半をソート
    ans_right = mergesort(A, middle, right) #　後半をソート

    ans_merge = merge(A, left, middle, right) # Aのleft~moddle-1, middle~rightの部分をマージする
    return ans_left + ans_right + ans_merge


n = int(input())
arr = list(map(int, input().split()))

ans = mergesort(arr, left=0, right=n)

print(" ".join(map(str, arr)))
print(ans)






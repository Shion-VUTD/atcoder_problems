# 反転数を求める

def merge_inversion(A, left, middle, right):
    left_nums = A[left: middle]
    right_nums = A[middle: right]

    # 次に比較する数列上のindexを保持
    left_index = 0
    right_index = 0

    num_inversion = 0
    while True:
        if left_index == middle - left and right_index == right - middle:
            break
        elif left_index == middle - left and right_index < right - middle:
            A[left + left_index + right_index] = right_nums[right_index]
            right_index += 1
        elif left_index < middle - left and right_index == right - middle:
            A[left + left_index + right_index] = left_nums[left_index]
            num_inversion += right_index
            left_index += 1
        elif left_nums[left_index] <= right_nums[right_index]:
            A[left + left_index + right_index] = left_nums[left_index]
            num_inversion += right_index
            left_index += 1
        else:
            A[left + left_index + right_index] = right_nums[right_index]
            right_index += 1
        
    return num_inversion



def count_inversion(A, p, r): #数列Aの、p番目からr-1番目までの反転数を求める
    if r - p <= 1:
        return 0
    middle = (p + r) // 2
    ans_1 = count_inversion(A, p, middle)
    ans_2 = count_inversion(A, middle, r)
    return ans_1 + ans_2 + merge_inversion(A, p, middle, r)

n = int(input())
nums = list(map(int, input().split()))
print(count_inversion(nums, 0, n))
    

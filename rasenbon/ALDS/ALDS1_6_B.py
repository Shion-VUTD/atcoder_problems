"""ある要素を基準に、その左側にはその要素以下の要素を、右側にはその要素より大きい要素を配置するPartitionをつくる"""

def pertition(A, p, r):
    """数列Aのp番目からr番目の要素について、A[r]を基準に並べ替える"""

    stand = A[r]
    i = p - 1 # どこまで並べ替えが確定したか

    for j in range(p, r):
        if A[j] <= stand:
            i += 1 # A[j]を配置するのはこのindex
            x = A[j]
            A[j] = A[i]
            A[i] = x # A[i]とA[j]を入れ替える

    A[r] = A[i + 1]
    A[i + 1] = stand
    return i + 1
        
def quicksort(A, p, r): # p番目からr番目までをクイックソートする
    if p >= r:
        return 
    q = pertition(A, p, r)
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)

n = int(input())
card_arr = []
for i in range(n):
    char, num = input().split()
    card_arr.append((int(num), char))

print(card_arr)

quicksort(card_arr, 0, n - 1)

for i in range(n):
    x, y = card_arr[i]
    print(y, x)




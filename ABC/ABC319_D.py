n, m = map(int, input().split())
lengths = list(map(int, input().split()))

#print(lengths)


def is_ok(w):
    # 何個の長さlengthの紐が作れるか
    count = 0
    tmp_line = 0
    for i in range(n):
        # print(count, tmp_line, lengths[i])
        if lengths[i] > w:
            return False
        if tmp_line + lengths[i] <= w:
            tmp_line += (lengths[i] + 1)
        else:
            count += 1
            tmp_line = (lengths[i] + 1)

    if count >= m:
        return False
    # print("count_:", count)
    return True


left = 0
right = 2 * 10**15

while True:
    if right - left == 1:
        print(right)
        exit()
    mid = (left + right) // 2
    if is_ok(mid):
        right = mid
    else:
        left = mid

from collections import Counter

m = int(input())
s1 = input()
s2 = input()
s3 = input()

appeared_nums_s1 = {}
appeared_nums_s2 = {}
appeared_nums_s3 = {}

for i, x in enumerate(s1):
    if x not in appeared_nums_s1.keys():
        appeared_nums_s1[x] = [i]
        appeared_nums_s1[x].append(i + m)
        appeared_nums_s1[x].append(i + 2 * m)
    else:
        appeared_nums_s1[x].append(i)
        appeared_nums_s1[x].append(i + m)
        appeared_nums_s1[x].append(i + 2 * m)

for i, x in enumerate(s2):
    if x not in appeared_nums_s1.keys():
        continue
    else:
        if x not in appeared_nums_s2.keys():
            appeared_nums_s2[x] = [i]
            appeared_nums_s2[x].append(i + m)
            appeared_nums_s2[x].append(i + 2 * m)
        else:
            appeared_nums_s2[x].append(i)
            appeared_nums_s2[x].append(i + m)
            appeared_nums_s2[x].append(i + 2 * m)

for i, x in enumerate(s3):
    if x not in appeared_nums_s2.keys():
        continue
    else:
        if x not in appeared_nums_s3.keys():
            appeared_nums_s3[x] = [i]
            appeared_nums_s3[x].append(i + m)
            appeared_nums_s3[x].append(i + 2 * m)
        else:
            appeared_nums_s3[x].append(i)
            appeared_nums_s3[x].append(i + m)
            appeared_nums_s3[x].append(i + 2 * m)


if len(appeared_nums_s3.keys()) == 0:
    print(-1)
    exit()

def merge_s(l1, l2, l3):

    l1 = list(set(l1))
    l2 = list(set(l2))
    l3 = list(set(l3))
    l1.sort()
    l2.sort()
    l3.sort()
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    tmp_1 = 0
    tmp_2 = 0
    tmp_3 = 0
    ans = 0
    while True:
        # print(tmp_1, tmp_2, tmp_3, cnt_1, cnt_2, cnt_3)
        if cnt_1 >= 1 and cnt_2 >= 1 and cnt_3 >= 1:
            break
        if l1[tmp_1] < l2[tmp_2]:
            if l1[tmp_1] < l3[tmp_3]:
                cnt_1 += 1
                tmp_1 += 1
                ans = l1[tmp_1-1]
            elif l1[tmp_1] == l3[tmp_3]:
                if (cnt_1 == 0 and cnt_3 != 0) or \
                    (cnt_1 == 0 and cnt_3 == 0 and l1[tmp_1] <= l3[tmp_3]):
                    cnt_1 += 1
                    tmp_1 += 1
                    tmp_3 += 1
                    ans = l1[tmp_1-1]
                else:
                    cnt_3 += 1
                    tmp_1 += 1
                    tmp_3 += 1
                    ans = l3[tmp_3-1]
            else:
                cnt_3 += 1
                tmp_3 += 1
                ans = l3[tmp_3-1]
        elif l1[tmp_1] == l2[tmp_2]:
            if l2[tmp_2] < l3[tmp_3]:
                if (cnt_2 == 0 and cnt_1 != 0) or \
                    (cnt_2 == 0 and cnt_1 == 0 and l2[tmp_2] <= l1[tmp_1]):
                    cnt_2 += 1
                    tmp_2 += 1
                    tmp_1 += 1
                    ans = l2[tmp_2-1]
                else:
                    cnt_1 += 1
                    tmp_2 += 1
                    tmp_1 += 1
                    ans = l1[tmp_1-1]
        
            elif l2[tmp_2] == l3[tmp_3]:
                if (cnt_1 == 0 and cnt_2 != 0 and cnt_3 != 0) or \
                    (cnt_1 == 0 and cnt_2 == 0 and cnt_3 != 0 and l1[tmp_1] <= l2[tmp_2]) or \
                        (cnt_1 == 0 and cnt_2 != 0 and cnt_3 == 0 and l1[tmp_1] <= l3[tmp_3]) or \
                            (cnt_1 == 0 and cnt_2 == 0 and cnt_3 == 0 and l1[tmp_1] <= l2[tmp_2] and l1[tmp_1] <= l3[tmp_3]):
                    cnt_1 += 1
                    tmp_1 += 1 
                    tmp_2 += 1
                    tmp_3 += 1
                    ans = l1[tmp_1-1]
                elif (cnt_2 == 0 and cnt_1 != 0 and cnt_3 != 0) or \
                    (cnt_2 == 0 and cnt_1 == 0 and cnt_3 != 0 and l2[tmp_2] <= l1[tmp_1]) or \
                        (cnt_2 == 0 and cnt_1 != 0 and cnt_3 == 0 and l2[tmp_2] <= l3[tmp_3]) or \
                            (cnt_2 == 0 and cnt_1 == 0 and cnt_3 == 0 and l2[tmp_2] <= l1[tmp_1] and l2[tmp_2] <= l3[tmp_3]):
                    cnt_2 += 1
                    tmp_2 += 1
                    tmp_1 += 1
                    tmp_3 += 1
                    ans = l2[tmp_2-1]
                elif (cnt_3 == 0 and cnt_1 != 0 and cnt_2 != 0) or \
                    (cnt_3 == 0 and cnt_1 == 0 and cnt_2 != 0 and l3[tmp_3] <= l1[tmp_1]) or \
                        (cnt_3 == 0 and cnt_1 != 0 and cnt_2 == 0 and l3[tmp_3] <= l2[tmp_2]) or \
                            (cnt_3 == 0 and cnt_1 == 0 and cnt_2 == 0 and l3[tmp_3] <= l1[tmp_1] and l3[tmp_3] <= l2[tmp_2]):
                    cnt_3 += 1
                    tmp_1 += 1
                    tmp_2 += 1
                    tmp_3 += 1
                    ans = l3[tmp_3-1]


            else:
                cnt_3 += 1
                tmp_3 += 1
                ans = l3[tmp_3-1]

        else:
            if l2[tmp_2] < l3[tmp_3]:
                cnt_2 += 1
                tmp_2 += 1
                ans = l2[tmp_2-1]
            elif l2[tmp_2] == l3[tmp_3]:
                if (cnt_2 == 0 and cnt_3 != 0) or \
                    (cnt_2 == 0 and cnt_3 == 0 and l2[tmp_2] <= l3[tmp_3]):
                    cnt_2 += 1
                    tmp_2 += 1
                    tmp_3 += 1
                    ans = l2[tmp_2-1]
                else:
                    cnt_3 += 1
                    tmp_2 += 1
                    tmp_3 += 1
                    ans = l3[tmp_3-1]
            else:
                cnt_3 += 1
                tmp_3 += 1
                ans = l3[tmp_3-1]
        
    return ans


ans = 400
for x in appeared_nums_s3.keys():
    ans_x = merge_s(
        appeared_nums_s1[x],
        appeared_nums_s2[x],
        appeared_nums_s3[x],
    )
    
    if ans_x < ans:
        ans = ans_x


print(ans)

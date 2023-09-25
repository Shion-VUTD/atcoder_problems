from itertools import permutations

def easy_levenshtein(s1, s2):
    differenct_char = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            differenct_char += 1
    return differenct_char


n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

s_perms = list(permutations(s))

is_ok = False
for s_perm in s_perms:
    is_ok_tmp = True
    for i in range(n-1):
        if easy_levenshtein(s_perm[i], s_perm[i+1]) != 1:
            is_ok_tmp = False
            break
    if is_ok_tmp:
        is_ok = True
        break
if is_ok:
    print("Yes")
else:
    print("No")
    
            
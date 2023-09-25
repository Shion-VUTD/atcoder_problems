import copy
from collections import defaultdict

n = int(input())
s = input()
is_large = False
is_small = False

is_larges = [False] * n

ans_s = copy.deepcopy(list(s))

for i in range(n):
    if s[i].isupper():
        is_larges[i] = True

queries = int(input())
is_irregular = defaultdict(int)

for query in range(queries):
    t, x, c = input().split()
    x = int(x)
    if t == "1":
        if is_large == True and is_small == False:
            if (is_large + is_irregular[x-1]) % 2 != c.isupper():
                is_irregular[x-1] = (is_irregular[x-1] + 1) % 2

        elif is_large == False and is_small == True:
            if (is_small + is_irregular[x-1]) % 2 != c.islower():
                is_irregular[x-1] = (is_irregular[x-1] + 1) % 2

        elif is_large == False and is_small == False:
            if (is_larges[x-1] + is_irregular[x-1]) % 2 != c.isupper():
                is_irregular[x-1] = (is_irregular[x-1] + 1) % 2

        else:
            raise ValueError(f"Error!: {x}")

        ans_s[x-1] = c

    elif t == "2":
        is_small = True
        is_large = False
        is_irregular = defaultdict(int)

    else:
        is_large = True
        is_small = False
        is_irregular = defaultdict(int)

# print(ans_s)
# print(is_irregular)
# print(is_large)
# print(is_small)

for i in range(n):
    if is_large == False and is_small == False:
        if (is_larges[i] + is_irregular[i]) % 2 == 1:
            ans_s[i] = ans_s[i].upper()
        else:
            ans_s[i] = ans_s[i].lower()
    elif is_large:
        if is_irregular[i] == 0:
            ans_s[i] = ans_s[i].upper()
        else:
            ans_s[i] = ans_s[i].lower()
    elif is_small:
        if is_irregular[i] == 0:
            ans_s[i] = ans_s[i].lower()
        else:
            ans_s[i] = ans_s[i].upper()


print("".join(ans_s))

# assert "TEEQUICKBROWMFiXJUGPFOVERTBELAZYDOG" == "TEEQUICKBROWMFiXJUGPFOVERTBELAZYDOG"


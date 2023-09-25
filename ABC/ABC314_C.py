import copy

n, m = map(int, input().split())
s = input()
colors = list(map(int, input().split()))

s_copy = copy.deepcopy(list(s))

# 最後にその色の文字のあったindexを入れる
flags = [-1] * m
init_id = [-1] * m

for i in range(n):
    color = colors[i] - 1
    if flags[color] == -1:
        flags[color] = i
        init_id[color] = i
    else:
        s_copy[i] = s[flags[color]]
        flags[color] = i

for i in range(m):
    if flags[i] != -1:
        s_copy[init_id[i]] = s[flags[i]]

print("".join(s_copy))

n = int(input())
degrees = [0] * n
to_list = [[] for _ in range(n)]
from_list = [[] for _ in range(n)]

zero_degrees = []

for i in range(n):
    inp = list(map(int, input().split()))
    degrees[i] = inp[0]
    if inp[0] == 0:
        zero_degrees.append(i)
        continue
    for x in inp[1:]:
        to_list[i].append(x - 1)
        from_list[x - 1].append(i)

# print(degrees)
# print(to_list)
# print(from_list)

# ノード0と連結なノードを探索
is_connected = [False] * n
stack = [0]
is_connected[0] = True

while stack:
    tmp = stack.pop()
    for i in to_list[tmp]:
        if is_connected[i]:
            continue
        is_connected[i] = True
        stack.append(i)

# print(is_connected)

ans_path = []
while zero_degrees:
    tmp = zero_degrees.pop()
    if tmp == 0:
        print(" ".join(map(str, ans_path)))
        exit()
    if is_connected[tmp]:
        ans_path.append(tmp + 1)
        for i in from_list[tmp]:
            degrees[i] -= 1
            if degrees[i] == 0:
                zero_degrees.append(i)



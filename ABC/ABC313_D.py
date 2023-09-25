n, k = map(int, input().split())

index = 0
binaries = ["Unknown"] * n
t_list = []

# まず最初のk個のbinariesを決める

binaries[k] = "x"

# 最初の質問で、初めのk個の偶奇をきく
print("?", end=" ")
for i in range(1, k + 1):
    if i != k:
        print(i, end=" ")
    else:
        print(i)

t_0 = int(input())
t_list.append(t_0)

for i in range(k):
    question = ["?"] + list(range(1, i + 1)) + list(range(i + 2, k + 2))
    print(" ".join(map(str, question)))
    t = int(input())
    if i == 0:
        t_list.append(t)
    if t == t_0:
        binaries[i] = "x"
    else:
        binaries[i] = "y"

# print(binaries)
num_x = binaries.count("x") - 1
num_y = binaries.count("y")
if num_x % 2 == t_0:
    for i in range(k+1):
        if binaries[i] == "x":
            binaries[i] = 1
        else:
            binaries[i] = 0

else:
    for i in range(k+1):
        if binaries[i] == "y":
            binaries[i] = 1
        else:
            binaries[i] = 0

# print(binaries)

# ここからは、k+2個目以降のbinariesを決める
if k + 2 <= n:
    for i in range(k + 1, n):
        question = ["?"] + list(range(i-k+2, i+2)) 
        print(" ".join(map(str, question)))
        t = int(input())
        if t == t_list[-1]:
            binaries[i] = binaries[i-k]
        else:
            binaries[i] = 1 - binaries[i-k]

print("! " + " ".join(map(str, binaries)))
        
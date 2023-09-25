n = int(input())

s = input()

stack = []
tmp = 0 # 左括弧の数
tmp_id = 0
for i in range(n):
    # print(stack ,tmp)
    if s[i] == "(":
        tmp += 1
        stack.append(s[i])
    elif s[i] == ")":
        if tmp <= 0:
            stack.append(s[i])
        else:
            popped = stack.pop()
            while popped != "(":
                popped = stack.pop()
            tmp -= 1
            # print(stack, popped)
    else:
        stack.append(s[i])

print("".join(stack))
terms = input().split()
opperands = ["+", "-", "*"]

stack = []
for term in terms:
    if term not in opperands:
        stack.append(term)
    else:
        x = stack.pop()
        y = stack.pop()
        stack.append(str(eval(y + term + x)))
    
print(stack[0])


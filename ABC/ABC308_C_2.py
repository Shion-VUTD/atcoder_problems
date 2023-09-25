import numpy as np
from functools import cmp_to_key

n = int(input())
denominators = []
numerators = []

for i in range(n):
    a, b = map(int, input().split())
    # print(type(a / (a + b)))
    denominators.append(a + b)
    numerators.append(a)
    
def compare(i, j):
    x_den = denominators[i-1]
    y_den = denominators[j-1]
    x_num = numerators[i-1]
    y_num = numerators[j-1]
    x_num *= y_den
    y_num *= x_den
    if (x_num < y_num) or (x_num == y_num and i > j):
        return 1
    else:
        return -1



arr = sorted(range(1, n+1), key=cmp_to_key(compare))

print(*arr, sep=" ")
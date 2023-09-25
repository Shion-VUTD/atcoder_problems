import numpy as np

n = int(input())
total_denominator = 1
denominators = []
numerators = []

for i in range(n):
    a, b = map(int, input().split())
    total_denominator *= (a + b)
    numerators.append(a)
    denominators.append(a + b)

numerators = np.array(numerators)
denominators = np.array(denominators)
# print(total_denominator, denominators, numerators)
numerators = (total_denominator // denominators) * numerators
numerators = np.argsort(- numerators) + 1

print(*numerators, sep=" ")

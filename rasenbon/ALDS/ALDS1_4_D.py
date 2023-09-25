n, k = map(int, input().split())
weights = []
for i in range(n):
    weights.append(int(input()))

left = 0
right = sum(weights)

def check_loadable(weights, p):
    flag = 0
    k_tmp = 1
    while flag <= n - 1:
        # print(flag)
        weight_tmp = 0
        for j in range(flag, n):
            if weights[j] > p:
                return False
            elif weight_tmp + weights[j] > p:        
                weight_tmp = 0
                k_tmp += 1
                flag = j 
                break

            elif j == n - 1:
                flag = n
                break
    
            else:
                weight_tmp += weights[j]
            
    
    if k_tmp <= k:
        return True
    else:
        return False

# print(check_loadable(weights, 8))


while right - left > 1:
    middle = (left + right) // 2
    if check_loadable(weights, middle):
        right = middle
    else:
        left = middle
    
print(right)



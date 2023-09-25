n = int(input())
matrix_h = []
matrix_w = []
for i in range(n):
    h, w = map(int, input().split())
    matrix_h.append(h)
    matrix_w.append(w)
num_multiplications = [[0]*n for i in range(n)]

for i in range(1, n): 
    for k in  range(0, n-i):
        # num_multiplications[k][k+i]: k番目からk+i番目までの連鎖行列積の最小回数
        ans_tmp = 10 ** 7
        for j in range(k, k+i):
            ans_tmp = min([ans_tmp, 
                num_multiplications[k][j] + num_multiplications[j+1][k+i] + \
                matrix_h[k] * matrix_w[j] * matrix_w[k+i]
            ])
        num_multiplications[k][k+i] = ans_tmp

print(num_multiplications[0][n-1])


    

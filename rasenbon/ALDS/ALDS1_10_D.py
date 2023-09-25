import numpy as np
n = int(input())
dp = np.array([[[0]*3 for j in range(n)] for i in range(n)])

for i in range(n):
    l, m = map(int, input().split())
    dp[i][i][0] = l
    dp[i][i][1] = m


for j in range(1, n): # j+1個の積
    for k in range(n-j): # k番目からk+j番目までの行列の積を考える
        first_matrix_top = k
        min_value = 10**8
        dp[k][k+j][0] = dp[k][k][0]
        dp[k][k+j][1] = dp[k+j][k+j][1]

        for second_matrix_top in range(k+1, k+j+1):
            first_matrix_point = dp[k][second_matrix_top-1][2]
            second_matrix_point = dp[second_matrix_top][k+j][2]
            first_matrix_h = dp[k][second_matrix_top-1][0]
            first_matrix_w = dp[k][second_matrix_top-1][1]
            second_matrix_w = dp[second_matrix_top][k+j][1]
            # print(first_matrix_h, first_matrix_w, second_matrix_w)
            new = first_matrix_point + second_matrix_point + first_matrix_h*first_matrix_w*second_matrix_w
            if new < min_value:
                min_value = new
            
        dp[k][k+j][2] = min_value


print(dp[0][n-1][2])



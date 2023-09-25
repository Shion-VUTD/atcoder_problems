def cal_lcs(x: str, y: str) -> int:
    m = len(x)
    n = len(y)
    lcs_dptable = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            lcs_tmp = max([lcs_dptable[i-1][j], lcs_dptable[i][j-1]])

            if x[i-1] == y[j-1]:
                lcs_tmp = max([lcs_tmp, lcs_dptable[i-1][j-1] + 1])
            
            lcs_dptable[i][j] = lcs_tmp
    
    return lcs_dptable[m][n]


q = int(input())
for i in range(q):
    x = input()
    y = input()
    print(cal_lcs(x, y))


n, m = map(int, input().split())

maps = [list(input()) for _ in range(n)]

tak_code = [["."] * 9 for _ in range(9)]
for i in range(3):
    for j in range(3):
        tak_code[i][j] = "#"
        tak_code[8-i][8-j] = "#"


for i in range(0, n-8):
    for j in range(0, m-8):
        is_tak_code = True
        for k in range(4):
            for l in range(4):
                if maps[i+k][j+l] != tak_code[k][l]:
                    is_tak_code = False
                    break
        
                if maps[i+5+k][j+5+l] != tak_code[5+k][5+l]:
                    is_tak_code = False
                    break

        if is_tak_code:
            print(i+1, j+1)


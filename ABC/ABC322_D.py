def cal_min_rec(polynomio):
    for i in range(4):
        if "#" in polynomio[i]:
            upper_border = i
            break
    for i in range(3, -1, -1):
        if "#" in polynomio[i]:
            lower_border = i
            break
    for i in range(4):
        is_border = False
        for j in range(4):
            if polynomio[j][i] == "#":
                left_border = i
                is_border = True
                # print(left_border)
                break
        if is_border:
            break
    for i in range(3, -1, -1):
        is_border = False
        for j in range(4):
            if polynomio[j][i] == "#":
                right_border = i
                is_border = True
                break
        if is_border:
            break
    return [upper_border, lower_border, left_border, right_border]

polynomio_1 = [input() for _ in range(4)]
polynomio_2 = [input() for _ in range(4)]
polynomio_3 = [input() for _ in range(4)]

#print(cal_min_rec(polynomio_1))
#print(cal_min_rec(polynomio_2))
#print(cal_min_rec(polynomio_3))

def create_polynomio_rotated(polynomio):
    grid = [["."] * 4 for _ in range(4)]
    ways = []
    upper_border, lower_border, left_border, right_border = cal_min_rec(polynomio)
    rotations = [(upper_border, lower_border, left_border, right_border), \
        (left_border, right_border, 3 - lower_border, 3 - upper_border), \
        (3 - lower_border, 3 - upper_border, 3 - right_border, 3 - left_border), \
        (3 - right_border, 3 - left_border, upper_border, lower_border)
    ]

    for i in range(4):
        polynomio_rec = [["."] * (rotations[i][3] - rotations[i][2] + 1) for _ in range(rotations[i][1] - rotations[i][0] + 1)]
        for j in range(rotations[i][0], rotations[i][1] + 1):
            for k in range(rotations[i][2], rotations[i][3] + 1):
                if i == 0:
                    # print("pattern 1", j, k)
                    polynomio_rec[j - rotations[i][0]][k - rotations[i][2]] = polynomio[j][k]
                elif i == 1:
                    # print("pattern 2", j, k, j - rotations[i][0], k - rotations[i][2], k, 3 - j)
                    polynomio_rec[j - rotations[i][0]][k - rotations[i][2]] = polynomio[3 - k][j]
                elif i == 2:
                    # print("pattern 3", j, k)
                    polynomio_rec[j - rotations[i][0]][k - rotations[i][2]] = polynomio[3 - j][3 - k]
                elif i == 3:
                    # print("pattern 4", j, k)
                    polynomio_rec[j - rotations[i][0]][k - rotations[i][2]] = polynomio[k][3 - j]
        ways.append(polynomio_rec)
    # print(ways)
    return ways

#print(create_polynomio_rotated(polynomio_1))
# print(create_polynomio_rotated(polynomio_2))
# print(create_polynomio_rotated(polynomio_3))

def cal_ways_to_set_polynomio(polynomio):
    ways = []
    rotated_polynomios = create_polynomio_rotated(polynomio)

    for rotated_polynomio in rotated_polynomios:
        # print(rotated_polynomio)
        for i in range(4 - len(rotated_polynomio) + 1):
            for j in range(4 - len(rotated_polynomio[0]) + 1):
                grid = [[-1] * 4 for _ in range(4)]
                for k in range(len(rotated_polynomio)):
                    for l in range(len(rotated_polynomio[0])):
                        if rotated_polynomio[k][l] == "#":
                            grid[i + k][j + l] = 1
                ways.append(grid)

    return ways

# print(cal_ways_to_set_polynomio(polynomio_1))

ways_1 = cal_ways_to_set_polynomio(polynomio_1)
ways_2 = cal_ways_to_set_polynomio(polynomio_2)
ways_3 = cal_ways_to_set_polynomio(polynomio_3)

for way_1 in ways_1:
    for way_2 in ways_2:
        for way_3 in ways_3:
            true_flag = True
            for i in range(4):
                for j in range(4):
                    if way_1[i][j] + way_2[i][j] + way_3[i][j] != -1 or way_1[i][j] * way_2[i][j] * way_3[i][j] != 1:
                        true_flag = False
                        break
            if true_flag:
                print("Yes")
                exit()
print("No")
                
            
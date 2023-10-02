# ABC322D 別解

polynomio_1 = [input() for _ in range(4)]
polynomio_2 = [input() for _ in range(4)]
polynomio_3 = [input() for _ in range(4)]


def count_rotations(polynomio):
    rotations = []
    grids_1 = [["."] * 4 for _ in range(4)]
    grids_2 = [["."] * 4 for _ in range(4)]
    grids_3 = [["."] * 4 for _ in range(4)]
    grids_4 = [["."] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            grids_1[i][j] = polynomio[i][j]
            grids_2[i][j] = polynomio[3 - j][i]
            grids_3[i][j] = polynomio[3 - i][3 - j]
            grids_4[i][j] = polynomio[j][3 - i]
    rotations.append(grids_1)
    rotations.append(grids_2)
    rotations.append(grids_3)
    rotations.append(grids_4)
    return rotations

# print(count_rotations(polynomio_1))

def count_ways_to_set_polynomio(polynomio):
    rotations = count_rotations(polynomio)
    ways = []
    for i in range(7):
        for j in range(7):
            for rotation in rotations:
                grids = [[-1] * 10 for _ in range(10)]
                for m in range(4):
                    is_broken = False
                    for n in range(4):
                        if rotation[m][n] == "#":
                            if not (3 <= (i + m) and (i + m) <= 6 and 3 <= (j + n) and (j + n) <= 6):
                                is_broken = True
                                break
                            grids[i + m][j + n] = 1
                    if is_broken:
                        break
                if not is_broken:
                    ways.append(grids)
    return ways

ways1 = count_ways_to_set_polynomio(polynomio_1)
ways2 = count_ways_to_set_polynomio(polynomio_2)
ways3 = count_ways_to_set_polynomio(polynomio_3)

# print(len(ways1), len(ways2), len(ways3))

for way1 in ways1:
    for way2 in ways2:
        for way3 in ways3:
            is_answer = True
            for i in range(3, 7):
                for j in range(3, 7):
                    if not (way1[i][j] + way2[i][j] + way3[i][j] == -1 and way1[i][j] * way2[i][j] * way3[i][j] == 1):
                        is_answer = False
                        break
                if not is_answer:
                    break
            if is_answer:
                print("Yes")
                exit()
print("No")
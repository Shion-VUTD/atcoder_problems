def add_lines(tuple1, tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2
    slope = (y2 - y1) / (x2 - x1)
    if slope == 0:
        x3, y3 = (x1 * (2 / 3) + x2 * (1 / 3), y1)
        x4, y4 = (x1 * (1 / 2) + x2 * (1 / 2), y1 + (x2 - x1) * (3 ** 0.5 / 6))
        x5, y5 = (x1 * (1 / 3) + x2 * (2 / 3), y1)

    elif slope > 0:
        x3, y3 = (x1 * (2 / 3) + x2 * (1 / 3), y1 * (2 / 3) + y2 * (1 / 3))
        x5, y5 = (x1 * (1 / 3) + x2 * (2 / 3), y1 * (1 / 3) + y2 * (2 / 3))
        x4, y4 = (x1, y5)

    elif slope < 0:
        x3, y3 = (x1 * (2 / 3) + x2 * (1 / 3), y1 * (2 / 3) + y2 * (1 / 3))
        x5, y5 = (x1 * (1 / 3) + x2 * (2 / 3), y1 * (1 / 3) + y2 * (2 / 3))
        x4, y4 = (x2, y3)
    

    return (x3, y3), (x4, y4), (x5, y5)


points = {}
points[(0, 0)] = (100, 0)

n = int(input())

for i in range(n):
    tmp = (0, 0)
    while True:
        if tmp == (100, 0):
            break
        next_point = points[tmp]
        (x3, y3), (x4, y4), (x5, y5) = add_lines(tmp, next_point)
        points[tmp] = (x3, y3)
        points[(x3, y3)] = (x4, y4)
        points[(x4, y4)] = (x5, y5)
        points[(x5, y5)] = next_point

        tmp = next_point

tmp = (0., 0.)
while True:
    if tmp == (100., 0.):
        print(100., 0.)
        break

    else:
        print(tmp[0], tmp[1])
        tmp = points[tmp]







    


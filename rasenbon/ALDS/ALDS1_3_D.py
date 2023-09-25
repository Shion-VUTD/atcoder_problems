stack = []
diagram = input()
n = len(diagram)
height = 0
gap_dict = {"/": 1, "_": 0, "\\": -1}
area = 0
areas = []

for i in range(n + 1):
    # 1個前によって今の高さを決める
    if i != 0:
        height += gap_dict[diagram[i - 1]]
    
    # 前が下り坂でないかつスタックの中に値がある時面積を計算して追加
    if i != 0 and diagram[i - 1] == "/" and stack != []:
        print('No')
        start = stack.pop()
        area_tmp = ((i - start) + (i - start - 2)) // 2
        area += area_tmp
        area_append = area_tmp
        print(areas)

        while True:
            if areas == []:
                areas.append((height, area_append))
                break

            if areas[-1][0] >= height:
                areas.append((height, area_append))
                break

            height_prep, area_prep = areas.pop()
            area_append += area_prep




    # 次が下り坂ならスタックに値を追加
    if i != n and diagram[i] == "\\":
        stack.append(i)
        

    

print(area, areas)


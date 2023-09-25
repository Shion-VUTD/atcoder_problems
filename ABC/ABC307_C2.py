ha, wa = map(int, input().split())
map_a = []
for i in range(ha):
    map_a.append(input())

hb, wb = map(int, input().split())
map_b = []
for i in range(hb):
    map_b.append(input())

hx, wx = map(int, input().split())
map_x = []
for i in range(hx):
    map_x.append(input())

black_coordinates_x = set([])
for i in range(hx):
    for j in range(wx):
        if map_x[i][j] == "#":
            black_coordinates_x.add((i, j))

# 黒いマスが全て入ってる最小の長方形を特定する
def crop_rec(h, w, maps):
    blacks = []
    # まず上下
    for i in range(h):
        if maps[i] != "." * w:
            up_end = i
            break
    for j in range(h-1, -1, -1):
        if maps[j] != "." * w:
            low_end = j
            break
    
    # 左右
    for i in range(w):
        if "#" in [maps[k][i] for k in range(h)]:
            left_end = i
            break
    for j in range(w-1, -1, -1):
        if "#" in [maps[k][j] for k in range(h)]:
            right_end = j
            break

    # 黒マスの相対座標
    for i in range(h):
        for j in range(w):
            if maps[i][j] == "#":
                blacks.append((i - up_end, j - left_end))
    
    return low_end - up_end + 1, right_end - left_end + 1, blacks


rec_ha, rec_wa, blacks_a = crop_rec(ha, wa, map_a)
rec_hb, rec_wb, blacks_b = crop_rec(hb, wb, map_b)

synthesized_maps = []
if hx - rec_ha < 0 or wx - rec_wa < 0:
    print("No")
    exit()
if hx - rec_ha < 0 or wx - rec_wa < 0:
    print("No")
    exit()


for i in range(0, hx - rec_ha + 1):
    for j in range(0, wx - rec_wa + 1):
        black_coordinates_tmp_a = set([])
        for black_x, black_y in blacks_a:
            black_coordinates_tmp_a.add((black_x + i, black_y + j))
        for k in range(0, hx - rec_hb + 1):
            for l in range(0, wx - rec_wb + 1):
                black_coordinates_tmp_b = set([])
                for black_x, black_y in blacks_b:
                    black_coordinates_tmp_b.add((black_x + k, black_y + l))
                if black_coordinates_tmp_a | black_coordinates_tmp_b == black_coordinates_x:
                    print("Yes")
                    exit()

print("No")
                



            

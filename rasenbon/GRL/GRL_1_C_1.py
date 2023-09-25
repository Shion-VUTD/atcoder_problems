v, e = map(int, input().split())

max_path_length = 10**12
all_pairs_shortest_paths = [[max_path_length] * v for i in range(v)]
# 自分自身への距離は0
for i in range(v):
    all_pairs_shortest_paths[i][i] = 0

# 初期値は、もし経路があればその重みにする
for edge in range(e):
    start, stop, weight = map(int, input().split())
    all_pairs_shortest_paths[start][stop] = weight


# 各i, j, kについて、
# k回目のforループのall_pairs_shortest_paths[i][j]: iからjまで、頂点0,1,…,k-1のいずれかを経由していくパスのうち最小のパス長
# k=0のときはどの頂点も経由しない

for k in range(v):
    for i in range(v):
        for j in range(v):
            all_pairs_shortest_paths[i][j] = min(
                [
                    all_pairs_shortest_paths[i][j],
                    all_pairs_shortest_paths[i][k] + all_pairs_shortest_paths[k][j],
                ]
            )

# 自分自身へのパス長が負になってたら負閉路あり
for i in range(v):
    if all_pairs_shortest_paths[i][i] < 0:
        raise ValueError("NEGATIVE CYCLE")

# 出力
for i in range(v):
    for j in range(v):
        if all_pairs_shortest_paths[i][j] == 10**12:
            print("INF", end=" ")
        else:
            print(all_pairs_shortest_paths[i][j], end=" ")
    print("\n")

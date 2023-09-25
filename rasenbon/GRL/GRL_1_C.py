"""ワーシャルフロイド法の実装

ワーシャルフロイド法とは、負の閉路を含まないグラフについて、全ての点の組(i, j)について、その最短経路たちを求める
(負の閉路が存在するならそのように記す)アルゴリズムである。
ダイクストラとの違いは以下の通り。
・ダイクストラは、「全ての辺の重みが非負であるようなグラフ」において、「ある一つの点から他の点へのそれぞれの最短経路」をO(((V+E)logV)で求めることができた。
・ワーシャルフロイドは、「負の閉路を含まないグラフ」において、「任意の2点の組を始点終点とする最短経路」をO(V^3)で求めることができる。

"""
import numpy as np
import sys

infinity = 2 * 10**7 + 1

num_nodes, num_edges = map(int, input().split())
next_matrix = np.array([infinity]*(num_nodes*num_nodes)).reshape(num_nodes, num_nodes)
for i in range(num_nodes):
    next_matrix[i, i] = 0

# 隣接行列を作る
for i in range(num_edges):
    x, y, weight = map(int, input().split())
    next_matrix[x, y] = weight

# k = 0 の時でshortest_distancesを初期化
k = 0 # 0,...,k-1のいずれかのノードを経由した場合の最短経路をshortest_distancesに保存する
shortest_distances = next_matrix
print(shortest_distances.shape)

k += 1
# k = 1 から k = num_nodes まで数学的帰納法(動的計画法)
while k <= num_nodes:   
    for i in range(num_nodes):
        for j in range(num_nodes):
            shortest_distances[i, j] = min(
                [shortest_distances[i, j], shortest_distances[i, k-1] + shortest_distances[k-1, j]]
            )
    k += 1

for i in range(num_nodes):
    if shortest_distances[i, i] < 0:
        print('NAGATIVE CIRCLE')
        sys.exit()
    
for i in range(num_nodes):    
    for j in range(num_nodes):
        if shortest_distances[i, j] == infinity:
            print('INF', end = ' ')
        else:
            print(shortest_distances[i, j], end = ' ')
    print('')


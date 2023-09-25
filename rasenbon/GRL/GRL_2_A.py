"""クラスカルのアルゴリズム

最小全域木を1つ求める問題の、プリムのアルゴリズム(計算量O(V^2)またはO((V+E)logV))以外でもう一つ有名な方法。
UnionFindで非連結なブロックを管理するのがミソ。

・エッジを、重みが小さい順にソート
・UnionFindを1点集合(ブロック)の族として初期化
・ソートしたエッジを順に取り出し、閉路を作らないように各ブロックを統合していく
・(具体的には、そのエッジの両端がUnionFind上で異なるブロックに属している場合にそのブロックをエッジで統合する)
"""

from DSL_1_A_UnionFind import UnionFindbySize

v, e = map(int, input().split())
edges = []
for egde in range(e):
    left, right, weight = map(int, input().split())
    edges.append((weight, left, right))

# エッジを重みの昇順に並べる(O(eloge))
edges.sort()
print(edges)

# blockを初期化
blocks = UnionFindbySize(v)

# 最小全域木の重みの総和
ans = 0

# 今までにカウントしたエッジ
cnt = 0

for weight, left, right in edges:  # 全体でelogv
    # print(blocks.all_group_members())
    if cnt == v - 1:
        print(ans)
        break

    if blocks.same(left, right):  # logv
        continue
    blocks.union(left, right)
    cnt += 1
    ans += weight


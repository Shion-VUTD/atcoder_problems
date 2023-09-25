# 木の直径
"""
無向の木Tについて、以下が成り立つ。

任意のT上の点sについて、
{(u, v) | u, v: node, uとvを結ぶ経路がTの直径} \
    = {(x, y) | x, y: Tのnode, xまたはyがsから最も遠い点であり、かつxとyはお互いが最も遠い点同士である}

すなわち、木の直径は次のようなアルゴリズムで求められる。
1. T上任意の点sをとってくる。
2. sから最も遠い点xをとってくる(直径となるパスを全て挙げるなら全列挙する)
3. xから最も遠い点yをとってくる(直径となるパスを全て挙げるなら各xに対し全列挙する)
このとき(x, y)がTの直径(の全て)である。

"""
n = int(input())
adjacency_list = [[] for i in range(n)]

for i in range(n - 1):
    x, y, weight = map(int, input().split())
    adjacency_list[x].append((y, weight))
    adjacency_list[y].append((x, weight))


def search_farthest_node(s):
    stack = [(s, 0)]  # (ノード, 0からそのノードまでの距離)
    is_visited = [False] * n
    is_visited[s] = True
    max_distance = 0
    x = -1
    while stack:
        # print(stack)
        tmp, distance = stack.pop()
        for child, weight in adjacency_list[tmp]:
            if is_visited[child] == False:
                distance += weight
                stack.append((child, distance))
                is_visited[child] = True
                if max_distance < distance:
                    max_distance = distance
                    x = child

    return x, distance


# s = 0とする
# sから最も遠い点を探索
x, _ = search_farthest_node(0)

# xから最も遠い点を探索
y, distance = search_farthest_node(x)

print(distance)

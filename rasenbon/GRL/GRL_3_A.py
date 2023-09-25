"""関節点の検出

DFSを用いて関節点を検出する
・関節点とは？
    連結なグラフについて、その頂点及びそこから出てる辺を全て削除した時に非連結になる点

・検出方法の本質
    ・頂点をてきとーに選び、それを根とするDFS木を作る(連結グラフなので全てのノードを含む)
    ・そのとき、DFSの探索順に頂点を番号づけしておく(ord)
    ・その木のある頂点について、「その頂点の親をまたいで、DFS木においてその頂点の子孫以外の点と子孫の点をつなぐ
    ワープが存在するかどうか判定するためのパラメータ」を導入する(lowest)
        ・lowest[u]: 以下の条件を満たす値の集合の最小値。つまり、自分か自分の子孫からワープして行ける頂点のうちorderが最小のもの
            ・order[u]
            ・lowest[w] if w が u の 子
            ・order[w] if u と w は木に属さない辺で隣り合う
    ・頂点uについて、「自分をまたぐワープ」が存在しないものが関節点
    具体的には、
        ・uが根: 子が2つ以上ある場合は関節点、そうでなければ関節点でない
        ・uが根でない: ある子ノードが存在して、ord[u] <= lowest[w]を満たすならば関節点、そうでなければ関節点でない
    
"""

num_nodes, num_edges = map(int, input().split())

# 隣接リストを作る
next_list = [[] for i in range(num_nodes)]
for i in range(num_edges):
    x, y = map(int, input().split())
    next_list[x].append(y)
    next_list[y].append(x)

# DFS木をつくり、同時にordとlowestを作る
tree = []  # 順番に入れていく
order = [-1] * num_nodes
lowests = [-1] * num_nodes
stack = [(0, 0)]
parents = [-1] * num_nodes
tmp_order = 0

# orderとparentに値を入れる
while stack:
    node, parent = stack.pop()
    if parents[node] == -1:
        parents[node] = parent
        tree.append(node)
        order[node] = tmp_order
        for next_node in next_list[node]:
            stack.append((next_node, node))
        tmp_order += 1

# lowestに値を入れる
for i in range(num_nodes - 1, -1, -1):
    node = tree[i]
    print(node)
    lowest = i
    for next_node in next_list[node]:
        if parents[next_node] == node and lowest > lowests[next_node]:
            lowest = lowests[next_node]
        elif (
            parents[next_node] != node
            and parents[node] != next_node
            and lowest > order[next_node]
        ):
            lowest = order[next_node]
    lowests[node] = lowest


# 関節点かどうかを判定
articulation_points = []

# node = 0の場合
num_child = 0
for next_node in next_list[0]:
    if parents[next_node] == 0:
        num_child += 1
if num_child > 1:
    articulation_points.append(0)

# それ以外
for node in range(1, num_nodes):
    is_articulation = False
    has_child = False
    for next_node in next_list[node]:
        if parents[next_node] == node:
            has_child = True
            if lowests[next_node] >= order[node]:
                is_articulation = True
                break
    if is_articulation and has_child:
        articulation_points.append(node)

print(articulation_points)

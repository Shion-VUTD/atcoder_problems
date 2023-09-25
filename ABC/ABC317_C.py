import copy

n, m = map(int, input().split())
adjacency_list = [[] for i in range(n)]

for i in range(m):
    x, y, length = map(int, input().split())
    adjacency_list[x - 1].append((y - 1, length))
    adjacency_list[y - 1].append((x - 1, length))

# print(adjacency_list)

def cal_max_length_path(target): # targetから最も時間をかけて行ける点を探索
    lengths = [-1] * n
    lengths[target] = 0
    stack = [[{target}, target, 0]] # 探索済みの点の集合と現在の点 
    while stack:
        tmp_path, tmp_node, path_length = stack.pop()
        for (next_node, length) in adjacency_list[tmp_node]:
            if next_node not in tmp_path:
                new_path = copy.deepcopy(tmp_path)
                new_path.add(next_node)
                stack.append([new_path, next_node, path_length + length])
                lengths[next_node] = max([path_length + length, lengths[next_node]])
        # print(stack)
    return max(lengths)

ans = -1
for i in range(n):
    # print(cal_max_length_path(i))
    ans = max([ans, cal_max_length_path(i)])

print(ans)


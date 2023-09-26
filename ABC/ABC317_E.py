from bisect import bisect_left, bisect_right
from collections import deque

h, w = map(int, input().split())
maps = [list(input()) for _ in range(h)]
obstacle_and_people_per_axis0 = [[] for _ in range(h)]
obstacle_and_people_per_axis1 = [[] for _ in range(w)]

for i in range(h):
    for j in range(w):
        if maps[i][j] in {"#", ">", "<", "^", "v"}:
            obstacle_and_people_per_axis0[i].append((j))
            obstacle_and_people_per_axis1[j].append((i))
        elif maps[i][j] == "S":
            start = (i, j)
        elif maps[i][j] == "G":
            goal = (i, j)


queue = deque([start])
is_visited = [[-1] * w for _ in range(h)]  # 最小の移動回数を記録
is_visited[start[0]][start[1]] = 0

while queue:
    tmp_i, tmp_j = queue.popleft()
    # print(tmp_i, tmp_j)
    # print(is_visited)
    if (tmp_i, tmp_j) == goal:
        print(is_visited[tmp_i][tmp_j])
        exit()

    for i, j in [
        (tmp_i + 1, tmp_j),
        (tmp_i - 1, tmp_j),
        (tmp_i, tmp_j + 1),
        (tmp_i, tmp_j - 1),
    ]:
        # print(i, j)
        if i < 0 or i >= h or j < 0 or j >= w:
            continue
        # 既に訪れている場合はスキップ
        if is_visited[i][j] != -1:
            continue

        left = bisect_left(obstacle_and_people_per_axis0[i], j)
        right = bisect_right(obstacle_and_people_per_axis0[i], j)
        up = bisect_left(obstacle_and_people_per_axis1[j], i)
        down = bisect_right(obstacle_and_people_per_axis1[j], i)

        # print(left, right, up, down)

        # 既に障害物か人がいる場合はスキップ
        if left != right:
            continue
        if up != down:
            continue

        # 人の視線の先にある場合はスキップ
        if left != 0 and maps[i][obstacle_and_people_per_axis0[i][left - 1]] == ">":
            # print("left!")
            continue
        if (
            right != len(obstacle_and_people_per_axis0[i])
            and maps[i][obstacle_and_people_per_axis0[i][right]] == "<"
        ):
            # print("right!")
            continue
        if up != 0 and maps[obstacle_and_people_per_axis1[j][up - 1]][j] == "v":
            # print("up!")
            continue
        if (
            down != len(obstacle_and_people_per_axis1[j])
            and maps[obstacle_and_people_per_axis1[j][down]][j] == "^"
        ):
            # print("down!")
            continue

        queue.append((i, j))
        is_visited[i][j] = is_visited[tmp_i][tmp_j] + 1


print(-1)

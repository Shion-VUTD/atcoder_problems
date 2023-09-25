n = int(input())

scores = list(map(int, input().split()))
max_score = max(scores)
if scores[0] == max_score and scores.count(max_score) == 1:
    print(0)
else:
    print(max_score - scores[0] + 1)

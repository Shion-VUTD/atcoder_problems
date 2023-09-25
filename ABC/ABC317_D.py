n = int(input())

needed_votes_and_seats = []
total_seats = 0
already_got_seats = 0

for i in range(n):
    takahashi, aoki, seats = map(int, input().split())
    kahannsu = (takahashi + aoki) // 2 + 1
    if kahannsu <= takahashi:
        already_got_seats += seats
    else:
        needed_votes_and_seats.append((kahannsu - takahashi, seats))
    total_seats += seats

needed_total_seats = total_seats // 2 + 1 - already_got_seats
# print(needed_votes_and_seats, needed_total_seats)

if needed_total_seats <= 0:
    print(0)
    exit()

dp = [
    [10**13] * (needed_total_seats + 1)
    for i in range(len(needed_votes_and_seats) + 1)
]
dp[0][0] = 0
for i in range(1, len(needed_votes_and_seats) + 1):
    for j in range(needed_total_seats + 1):
        if j >= needed_votes_and_seats[i - 1][1]:
            dp[i][j] = min(
                [
                    dp[i - 1][j],
                    dp[i - 1][j - needed_votes_and_seats[i - 1][1]]
                    + needed_votes_and_seats[i - 1][0],
                ]
            )
        else:
            dp[i][j] = min(
                [dp[i - 1][j], dp[i - 1][0] + needed_votes_and_seats[i - 1][0]]
            )
print(dp[-1][-1])

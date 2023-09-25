import heapq

n, m = map(int, input().split())
weights = [0] * n
active_people = list(range(n))
heapq.heapify(active_people)
eating_people_and_return_time = []
heapq.heapify(eating_people_and_return_time)

for i in range(m):
    time, weight, interval = map(int, input().split())
    # print(active_people, eating_people_and_return_time)
    while True:
        if len(eating_people_and_return_time) == 0 or eating_people_and_return_time[0][0] > time:
            break
        else:
            return_person = heapq.heappop(eating_people_and_return_time)
            heapq.heappush(active_people, return_person[1])
    if len(active_people) == 0:
        continue
    eating_person = heapq.heappop(active_people)
    weights[eating_person] += weight
    heapq.heappush(eating_people_and_return_time, (time + interval, eating_person))


for weight in weights:
    print(weight)



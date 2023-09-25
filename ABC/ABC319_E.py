n, takahashi_to_busstop, busstop_to_aoki = map(int, input().split())
busstop_intervals = []
bus_transportation_times = []
total_transportation_times = [takahashi_to_busstop]

for i in range(n-1):
    p, t = map(int, input().split())
    busstop_intervals.append(p)
    bus_transportation_times.append(t)
    total_transportation_times.append(total_transportation_times[-1] + t)


mod_3_8_6_table = [[0, 9, 18, 3, 12, 21, 6, 15], [16, 1, 10, 19, 4, 13, 22, 7], [8, 17, 2, 11, 20, 5, 14, 23]]

def cal_init_mod_x(mod_3, mod_5, mod_7, mod_8, x):
    if x == 1:
        return 0
    elif x == 2 or x == 4:
        return mod_8 % x
    elif x == 3:
        return mod_3
    elif x == 5:
        return mod_5
    elif x == 6:
        return mod_3_8_6_table[mod_3][mod_8]
    elif x == 7:
        return mod_7
    elif x == 8:
        return mod_8


def cal_total_wasted_times(mod_3, mod_5, mod_7, mod_8):
    total_wasted_times = [0]
    for i in range(1, n):
        mod_init = cal_init_mod_x(mod_3, mod_5, mod_7, mod_8, busstop_intervals[i - 1])
        mod_transport = total_transportation_times[i - 1]
        total_wasted_time_tmp = (total_wasted_times[-1] + mod_transport + mod_init) % busstop_intervals[i - 1]
        if total_wasted_time_tmp != 0:
            total_wasted_time_tmp = busstop_intervals[i - 1] - total_wasted_time_tmp
        total_wasted_times.append(total_wasted_times[-1] + total_wasted_time_tmp)
    # print(total_wasted_times)

    return total_wasted_times[-1]

def cal_total_cost(mod_3, mod_5, mod_7, mod_8):
    total_wasted_time = cal_total_wasted_times(mod_3, mod_5, mod_7, mod_8)
    # print(total_wasted_time)
    total_cost = total_wasted_time + total_transportation_times[-1] + busstop_to_aoki
    return total_cost

mod_to_total_cost = {}
for mod_3 in range(3):
    for mod_5 in range(5):
        for mod_7 in range(7):
            for mod_8 in range(8):
                mod_to_total_cost[(mod_3, mod_5, mod_7, mod_8)] = cal_total_cost(mod_3, mod_5, mod_7, mod_8)

print(mod_to_total_cost)
num_queries = int(input())
for i in range(num_queries):
    q = int(input())
    mod_3 = q % 3
    mod_5 = q % 5
    mod_7 = q % 7
    mod_8 = q % 8
    print(mod_to_total_cost[(mod_3, mod_5, mod_7, mod_8)] + q)









# 最小コストソート
# 巡回置換に分けよう

def find_cycle_replacement_blaock(A):
    """
    returns:
        {サイクルの最小の数: 巡回する個数}の辞書
    """
    n = len(A)
    cycle_dict = {}
    is_visited = [False] * max(A) 
    for i in range(n):
        if is_visited[A[i] - 1] == False:
            is_visited[A[i] - 1] = True
            conponents = [A[i]]
            j = i + 1
            while True:
                if A[j - 1] == i + 1:
                    break
                j = A[j - 1]
                is_visited[A[j - 1] - 1] = True
                conponents.append(A[j - 1])

            cycle_dict[i + 1] = conponents
    
    return cycle_dict
        
def cal_min_sost(A):
    cycle_dict = find_cycle_replacement_blaock(A)
    # print(cycle_dict)
    ans = 0
    for index, conponents in cycle_dict.items():
        if len(conponents) > 1:
            ans += sum(conponents)
            ans += index * (len(conponents) - 2)

    return ans

n = int(input())
nums = list(map(int, input().split()))
print(cal_min_sost(nums))
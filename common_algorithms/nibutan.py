#二分探索
#(ここではlen=10としている)

#okが左側
def is_ok(i):
    return i <= 5 #大きい側がTrue
#is_okは条件を満たすかどうかの判定
 
ok = -1
ng = 10
def bis(n,m):
    ok = n
    ng = m
    while ng-ok > 1:
        mid = (ok+ng) // 2 # 平均(小数切り捨て)
        if is_ok(mid):
            ok = mid
        else:
    	    ng = mid
    return (ok,ng) # "5 6" が返される

#okが右側
def is_ok2(i):
    return i > 5 #大きい側がTrue
 
def bis_right(n,m):
    ok,ng = n,m # さっきと逆なので注意
    while ok-ng > 1: # さっきと逆なので注意。abs(ok-ng)のように汎用的に書く流派もある
        mid = (ok+ng) // 2 # 平均(小数切り捨て)
        if is_ok2(mid):
            ok = mid
        else:
    	    ng = mid
    return (ok,ng) # "6 5" が出力される

#計算量はO(log(len))
print(ord('a'))
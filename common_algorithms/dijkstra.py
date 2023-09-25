from heapq import heappush, heappop

def dijkstra(s,n,adj):
    INF = 10 ** 9
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] *n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        if seen[v] == True:
            pass
        else:
            seen[v] = True
            for to, cost in adj[v]:   #ノードvに隣接しているノードに対して
                if seen[to] == False and dist[v] + cost < dist[to]:
                    dist[to] = dist[v] + cost
            
                    heappush(hq, (dist[to], to))
           
    print(hq,dist)
            
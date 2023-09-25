n, q = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.depths = [0] * n # i番目の値は、そのノードの各が属する木における深さを表す
        self.parents = [i for i in range(n)] # i番目の値はその親ノードを返す
        self.nodes_per_tree = {}
        # 木の高さを取得するのってどう持っていたら一番効率が良い？
    
    def find(self, x): # xの属する木の根を返す
        # 根までたどる
        tmp = x
        same_branch = [tmp]
        while True:
            if self.parents[tmp] = tmp:
                # 経路圧縮
                for node in same_branch:
                    self.parents[node] = tmp
                    self.depths[node] = 1
                return tmp
            else:
                tmp = self.parents[tmp]
                same_branch.append[tmp]
        
    def same(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        return  root_x == root_y

    def union(self, x, y): # xの属する木とyの属する木を結合する
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            



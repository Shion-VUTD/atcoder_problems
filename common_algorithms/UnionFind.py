class UnionFind():
    def __init__(self,n):
        #親を与えるリストを定義
        self.par = [i for i in range(n+1)]
        #木の深さを与えるリストを定義
        self.rank = [0] * (n+1)

    #根を検索
    def find(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #併合
    def union(self,x,y):
        #根を取得
        x = self.find(x)
        y = self.find(y)

        #xを根とする木よりyを根とする木の方が深ければ、xをyとひっつけて根をyとする
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        #もしそうじゃないなら、yをxとひっつけて根をxとする
        else:
           self.par[y] = x
           #もしxを根とする木とyを根とする木の深さが等しければ、ひっつけた分だけxを根とする木の深さが１増える
           self.rank[x] += 1


    #同じ集合に属するか判定
    def same_check(self,x,y):
        return self.find(x) == self.find(y)

#使い方
unionfind = UnionFind(3)
print(unionfind.par)
print(unionfind.find(1))

unionfind.union(1,3)
print(unionfind.find(3))


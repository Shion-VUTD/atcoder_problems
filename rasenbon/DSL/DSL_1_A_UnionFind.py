from collections import defaultdict
from typing import List

"""
UnionFind: 互いに素な集合をあつかうデータ構造

n個の要素がある場合、以下の操作が償却計算量O(logn)でできることが特徴。

・find(x) : xが属する木(の根)を見つけて出力する
・union(x, y) : xが属する木とyが属する木を結合する

union(x, y)の計算量をO(n)ではなくO(logn)で抑えられるようにするために、以下2つの工夫をする。
・経路圧縮: find(x)で親をたどる際に、途中に登場するノードの親を全て根に付け替える
・rank(size)が大きい方の木に小さい方をつける
rankは、「初期値は0で、union時に二つの木のrankが同じなら+1, ことなるならそのまま」という値として定義する(≠木の高さ)。
このとき、rankが増えるのは高々log(n)回なので、上で抑えられる。
size(集合の要素数)を指標とする場合も全く同じことで、サイズkの集合をUnionFindの木にした時、上のようにそのrankはlogkで抑えられるので同様に
計算量も抑えられる。


"""


class UnionFindbySize:
    """要素を0~n-1という数字(index)で管理するUnionFind"""

    def __init__(self, n):
        self.n = n  # 要素数
        self.parents_or_sizes = [-1] * n  # 根でないノードはその親を持ち、根であるノードは-(その木の要素数)を持つ

    def find(self, x):
        """xが属する木の根ノードを返す"""
        if self.parents_or_sizes[x] < 0:
            return x
        else:
            self.parents_or_sizes[x] = self.find(self.parents_or_sizes[x])  # 経路圧縮
            return self.parents_or_sizes[x]

    def union(self, x, y):
        """xが属する木とyが属する木を結合する"""
        x = self.find(x)
        y = self.find(y)

        if self.parents_or_sizes[x] >= self.parents_or_sizes[y]:
            self.parents_or_sizes[x] += self.parents_or_sizes[y]
            self.parents_or_sizes[y] = x
        elif self.parents_or_sizes[x] < self.parents_or_sizes[y]:
            self.parents_or_sizes[y] += self.parents_or_sizes[x]
            self.parents_or_sizes[x] = y

    def same(self, x, y):
        """xとyが同じ木に属するか判定する"""
        return self.find(x) == self.find(y)

    def size(self, x):
        """xが属する木の要素数を返す"""
        x = self.find(x)
        return -self.parents_or_sizes[x]

    def members(self, x):
        """xが属する集合の要素を列挙する"""
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """根ノードのリストを返す"""
        return [
            i
            for i, x in enumerate(self.parents_or_sizes)
            if self.parents_or_sizes[x] < 0
        ]

    def group_count(self):
        """木の数を数える"""
        return len(self.roots())

    def all_group_members(self):
        """group_members[root]がその木の要素を表すようなdefaultdictを考える"""
        group_members = defaultdict(list)
        for i in range(self.n):
            group_members[self.find(i)].append(i)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


class UnionFindLabel(UnionFindbySize):
    def __init__(self, labels: List):
        self.n = len(labels)
        self.parents_or_sizes = [-1] * self.n

        # indexとlabelを互換するDictを作る
        self.index_to_label = {}
        self.label_to_index = {}
        for i, label in enumerate(labels):
            index_to_label[i] = label
            index_to_label[label] = i

    def find_label(self, label):
        return self.index_to_label[super().find(self.label_to_index[label])]

    def union(self, label_x, label_y):
        super().union(self.label_to_index[label_x], self.label_to_index[label_y])

    def size(self, label):
        return super().size(self.label_to_index[label])

    def same(self, label_x, label_y):
        return super().same(self.label_to_index[label_x], self.label_to_index[label_y])

    def roots(self):
        return [
            self.index_to_label[i] for i in range(self.n) if self.parents_or_sizes < 0
        ]

    def all_group_members(self):
        group_members = defaultdict(list)
        for i in range(self.n):
            group_members[self.index_to_label[super.find()]].append(
                self.index_to_label[i]
            )

        return group_members


def main():
    n, q = map(int, input().split())
    union_find = UnionFindbySize(n)
    for i in range(q):
        command, x, y = map(int, input().split())
        if command:
            print(union_find.same(x, y))
        else:
            union_find.union(x, y)


if __name__ == "__main__":
    main()

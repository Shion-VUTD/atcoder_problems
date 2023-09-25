"""セグ木を作ろう

セグ木は、
・値の更新
・区間に依存する何かしらのパラメータを取得する
が同時に起こる場合に利用される。

"""

class SegmentMinimumTree:
    def __init__(self, arr, infinity):
        self.arr = arr
        self.infinity = infinity
        self.seg_tree = None
        self.arr_expanded_length = None

    def make_segment_tree(self): 
        """配列からセグ木を作る"""

        arr_length = len(self.arr)
        arr_expanded_length = 1 # セグ木となる配列の最下段の長さ
        while True:
            if arr_length <= arr_expanded_length:
                break
            arr_expanded_length *= 2

        tree_length = 2 * arr_expanded_length - 1 # 必要となるセグ木の長さ

        segment_tree = [self.infinity]*tree_length

        # 最下段に値を入れる
        for i in range(arr_expanded_length - 1, arr_expanded_length + arr_length - 1):
            segment_tree[i] = self.arr[i - arr_expanded_length + 1]
        
        # 最下段以外に値を入れる
        tmp_index = arr_expanded_length - 2
        while tmp_index >= 0:
            segment_tree[tmp_index] = min([segment_tree[tmp_index * 2 + 1], segment_tree[tmp_index * 2 + 2]])
            tmp_index -= 1
        
        self.seg_tree = segment_tree
        self.arr_expanded_length = arr_expanded_length
    

    def update(self, i, x): 
        """arrのうちi番目の値をxに変える"""
        self.arr[i] = x
        self.seg_tree[i + self.arr_expanded_length - 1] = x
        tmp_index = i + self.arr_expanded_length - 1
        while tmp_index >= 0:
            tmp_index = (tmp_index - 1) // 2
            self.seg_tree[tmp_index] = min([self.seg_tree[tmp_index * 2 + 1], self.seg_tree[tmp_index * 2 + 2]])
        
    def getmin(self, a, b, k, l, r): 
        """
        [a, b) と, seg_treeのk番目のノードで表される区間[l, r) の共通部分の最小値を求める
        int a, b: 区間
        int k: 注目ノードのseg_tree上のindex
        int l, r: seg_tree[k]が表す区間
        """

        if b <= l or a >= r:
            return self.infinity
        elif a >= r and l < b:
            return self.getmin(self, a, b, 2 * k + 1, l, (l + r) // 2)
        elif a < r and b <= l:
            return self.getmin(self, a, b, 2 * k + 2, (l + r) // 2, r)
        else:
            return self.seg_tree[k]
            





def main():
    arr = list(map(int, input().split()))
    segment_tree = SegmentMinimumTree(arr, infinity=1000)
    print(segment_tree.segtree)


if __name__ == "__main__":
    main()
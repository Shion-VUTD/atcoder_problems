class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.len = 0
    def insert(self, x):
        # まず末尾に追加
        self.queue.append(x)
        self.len += 1
        index = self.len - 1
        
        # 順に上にあげる
        while True:
            if index <= 0:
                break
            parent_id = (index - 1) // 2
            if self.queue[index] <= self.queue[parent_id]:
                break
            else:
                parent_key = self.queue[parent_id]
                self.queue[index] = parent_key
                self.queue[parent_id] = x
                index = parent_id
        
    def extract(self):
        # 末尾の要素を根にもってくる
        last = self.queue.pop()
        self.len -= 1
        if self.len == 0:
            return last
        root = self.queue[0]
        if self.len >= 1:
            self.queue[0] = last

        index = 0
        # 順に下に下ろす
        while True:
            if index >= self.len // 2:
                break
            left_id = 2 * index + 1
            left_key = self.queue[left_id]
            right_id = 2 * index + 2
            if right_id < self.len:
                right_key = self.queue[right_id]
            else:
                right_key = -1
            if last >= left_key and last >= right_key:
                break
            elif last < left_key and left_key >= right_key:
                self.queue[left_key] = last
                self.queue[index] = left_key
                index = left_key
            elif last < right_key and left_key < right_key:
                self.queue[right_key] = last
                self.queue[index] = right_key
                index = right_key
        
        return root

queue = PriorityQueue()
while True:
    s = input()
    if s == "end":
        break
    elif s == "extract":
        print(queue.extract())
    else:
        insert, num = s.split()
        queue.insert(int(num))


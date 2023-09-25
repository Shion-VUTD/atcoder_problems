from collections import defaultdict

class LinkedList:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.linked_dict = defaultdict(lambda: [])
        
    def add_top(self, x):
        self.top = x
        self.linked_dict[x].append((-1, self.top))
        
        self.linked_dict[self.top][0] = 
        
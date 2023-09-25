# Binary Search Treeを実装

class BinarySearchTreeNode:
    def __init__(self, x):
        self.parent = None
        self.left = None
        self.right = None
        self.value = x

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, x: int):
        x = BinarySearchTreeNode(x)
        if self.root is None:
            self.root = x
        else:
            tmp = self.root
            ##print(x.value)
            #print(tmp.value, tmp.left, tmp.right)
            
            while True:
                if (tmp.left is None) and x.value <= tmp.value:
                    tmp.left = x
                    x.parent = tmp
                    #print('A')
                    break
                elif (tmp.right is None) and x.value >= tmp.value:
                    tmp.right = x
                    x.parent = tmp
                    #print('B')
                    break
                elif (tmp.left != None) and x.value <= tmp.value:
                    tmp = tmp.left
                    #print(tmp.value)
                elif (tmp.right != None) and x.value >= tmp.value:
                    tmp = tmp.right
                    #print('D')
                else:
                    raise ValueError('Error!')

    def find(self, x: int):
        tmp = self.root
        while True:
            # print(tmp.value)
            if x == tmp.value:
                return tmp
            elif x < tmp.value:
                # print('a')
                if tmp.left is None:
                    return "Not Found"
                else:
                    tmp = tmp.left
            else:
                # print('b')
                if tmp.right is None:
                    return "Not Found"
                else:
                    tmp = tmp.right

    def delete(self, x: int):
            x = self.find(x)
            if x != 'NotFound':
                parent = x.parent
                if x.left is None and x.right is None:
                    if parent.left == x:
                        parent.left = None
                    else:
                        parent.right = None
                elif x.left is not None and x.right is None:
                    x.left.parent = parent
                    if parent.left == x:
                        parent.left = x.left
                    else:
                        parent.right = x.left
                elif x.left is None and x.right is not None:
                    x.right.parent = parent
                    if parent.left == x:
                        parent.left = x.right
                    else:
                        parent.right = x.right
                else:
                    x.value = x.left.value
                    self.delete(x.left)
            else:
                raise ValueError


    def preorder_display(self):
        ans = []
        stack = [self.root]
        while stack != []:
            tmp = stack.pop()
            ans.append(tmp.value)
            left, right = tmp.left, tmp.right
            if right != None:
                stack.append(right)
            if left != None:
                stack.append(left)
        return ans
    
    def inorder_display_tmp(self, tmp):
        left, right = tmp.left, tmp.right
        if left != None:
            left_block = self.inorder_display_tmp(left)
        else:
            left_block = []
        
        if right != None:
            right_block = self.inorder_display_tmp(right)
        else:
            right_block = []

        return left_block + [tmp.value] + right_block   
    
    def inorder_display(self):
        return self.inorder_display_tmp(self.root)


bst = BinarySearchTree()
n = int(input())
for i in range(n):
    command = input().split()
    if len(command) == 2:
        term, num = command
        if term == "insert":
            bst.insert(int(num))
        elif term == "find":
            if bst.find(int(num)) == "Not Found":
                print('no')
            else:
                print('yes')
        elif term == "delete":
            bst.delete(int(num))
            
    else:
        print(' ' + ' '.join(map(str, bst.inorder_display())))
        print(' ' + ' '.join(map(str, bst.preorder_display())))
    

# 大小関係があきらかにおかしい場合型のミスマッチを疑え！！！
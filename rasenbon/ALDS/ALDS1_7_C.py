n = int(input())
adjacencies = [[] for i in range(n)]
is_root = [True] * n
for i in range(n):
    tmp, left, right = map(int, input().split())
    adjacencies[tmp].append(left)
    adjacencies[tmp].append(right)
    if left != -1:
        is_root[left] = False
    if right != -1:
        is_root[right] = False

# rootを決める
root = -1
for i in range(n):
    if is_root[i]:
        root = i
        break

def preorder_sort(adjacencies):
    ans = []
    stack = [root]
    while stack != []:
        tmp = stack.pop()
        ans.append(tmp)
        left, right = adjacencies[tmp]
        if right != -1:
            stack.append(right)
        if left != -1:
            stack.append(left)
    
    return ans

def inorder_sort(adjacencies, tmp):
    left, right = adjacencies[tmp]
    if left != -1:
        left_block = inorder_sort(adjacencies, left)
    else:
        left_block = []
    
    if right != -1:
        right_block = inorder_sort(adjacencies, right)
    else:
        right_block = []

    return left_block + [tmp] + right_block    

def postorder_sort(adjacencies, tmp):
    left, right = adjacencies[tmp]
    if left != -1:
        left_block = postorder_sort(adjacencies, left)
    else:
        left_block = []
    
    if right != -1:
        right_block = postorder_sort(adjacencies, right)
    else:
        right_block = []

    return left_block + right_block + [tmp] 

print("Preorder")
print(' ' + ' '.join(map(str, preorder_sort(adjacencies))))
print("Inorder")
print(' ' + ' '.join(map(str, inorder_sort(adjacencies, root))))
print("Postorder")
print(' ' + ' '.join(map(str, postorder_sort(adjacencies, root))))
    

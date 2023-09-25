n = int(input())
preorder_list = list(map(int, input().split()))
inorder_list = list(map(int, input().split()))

inorder_index_list = [-1] * n
for i, x in enumerate(inorder_list):
    inorder_index_list[x - 1] = i

def postorder(tmp_id, tmp, preorder_left, preorder_right, inorder_left, inorder_right):

    tmp_postorder_id = inorder_index_list[tmp - 1]
    left_inorder_block_left = inorder_left
    left_inorder_block_right = tmp_postorder_id 
    right_inorder_block_left = tmp_postorder_id + 1
    right_inorder_block_right = inorder_right

    left_inorder_block_num = left_inorder_block_right - left_inorder_block_left
    right_inorder_block_num = right_inorder_block_right - right_inorder_block_left

    left_preorder_block_left = tmp_id + 1
    left_preorder_block_right = tmp_id + left_inorder_block_num + 1
    right_preorder_block_left = left_preorder_block_right
    right_preorder_block_right = left_preorder_block_right + right_inorder_block_num

    left_new_tmp_id = tmp_id + 1
    right_new_tmp_id = right_preorder_block_left

    if left_preorder_block_left == left_preorder_block_right:
        left_block = []
    else:
        left_new_tmp = preorder_list[left_new_tmp_id]
        left_block = postorder(
            left_new_tmp_id, 
            left_new_tmp, 
            left_preorder_block_left, 
            left_preorder_block_right, 
            left_inorder_block_left,
            left_inorder_block_right
            )

    if right_preorder_block_left == right_preorder_block_right:
        right_block = []
    else:
        right_new_tmp = preorder_list[right_new_tmp_id]
        right_block = postorder(
            right_new_tmp_id, 
            right_new_tmp, 
            right_preorder_block_left, 
            right_preorder_block_right, 
            right_inorder_block_left,
            right_inorder_block_right
        )

    return left_block + right_block + [tmp]

print(' '.join(map(str, postorder(0, preorder_list[0], 0, n, 0, n))))



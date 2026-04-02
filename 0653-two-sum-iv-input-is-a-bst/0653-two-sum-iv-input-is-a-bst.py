# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def inorder_traversal(node):
            if not node:
                return 
            
            inorder_traversal(node.left)
            arr.append(node.val)
            inorder_traversal(node.right)

        inorder_traversal(root)

        check = {}
        for idx in range(len(arr)):
            if k-arr[idx] in check:
                return True
            else:
                check[arr[idx]] = idx

        return False
        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def _inorder_traversal(self, node):
        if not node:
            return 
        
        self._inorder_traversal(node.left)
        self.arr.append(node.val)
        self._inorder_traversal(node.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        self._inorder_traversal(root)

        check = {}
        for idx in range(len(self.arr)):
            if k-self.arr[idx] in check:
                return True
            else:
                check[self.arr[idx]] = idx

        return False
        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode], val: str):
            if not node.left and not node.right:
                self.res += int(val)
                return 

            if node.left:
                dfs(node.left, val + str(node.left.val))

            if node.right:
                dfs(node.right, val + str(node.right.val))

        dfs(root, str(root.val))

        return self.res


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, root: Optional[TreeNode]):
        if not root:
            return 0

        leftH = self.get_height(root.left)
        rightH = self.get_height(root.right)

        return max(leftH, rightH)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftH = self.get_height(root.left)
        rightH = self.get_height(root.right)

        return abs(leftH - rightH) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
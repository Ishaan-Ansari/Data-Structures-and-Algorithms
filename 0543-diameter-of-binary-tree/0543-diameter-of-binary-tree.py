# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.get_height(root.left), self.get_height(root.right))+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftH = self.get_height(root.left)
        rightH = self.get_height(root.right)


        leftdia = self.diameterOfBinaryTree(root.left)
        rightdia = self.diameterOfBinaryTree(root.right)

        return max(leftH + rightH, leftdia, rightdia)

        
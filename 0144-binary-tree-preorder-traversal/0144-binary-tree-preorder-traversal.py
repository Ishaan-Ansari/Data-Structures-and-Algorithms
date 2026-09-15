# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        # root -> left -> right
        if root is None:
            return self.ans
        
        self.ans.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.ans
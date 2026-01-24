# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def solve(self, root:Optional[TreeNode]) -> None:
        if not root:
            return

        self.solve(root.left)
        self.solve(root.right)
        self.ans.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.solve(root)
        return self.ans


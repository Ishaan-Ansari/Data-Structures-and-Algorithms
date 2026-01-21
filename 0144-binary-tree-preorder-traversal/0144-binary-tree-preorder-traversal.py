# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        self.ans.append(root.val)
        self.solve(root.left)
        self.solve(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.solve(root)
        return self.ans
        

        
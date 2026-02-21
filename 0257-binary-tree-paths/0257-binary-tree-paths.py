# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def solve(self, root):
        if not root:
            return 

        self.path.append(str(root.val))

        if not root.left and not root.right:
            self.res.append("->".join(self.path))
        else:
            self.solve(root.left)
            self.solve(root.right)

        self.path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        self.solve(root)

        return self.res
        
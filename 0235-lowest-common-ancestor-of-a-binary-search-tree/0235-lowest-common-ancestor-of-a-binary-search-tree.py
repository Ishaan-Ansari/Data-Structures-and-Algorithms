# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        curr = root.val

        if curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root
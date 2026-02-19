# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # simple sa BFS along with indexing 
        q = collections.deque()
        q.append((root, 0))

        maxi = 0

        while q:
            leftMost = q[0][1]
            rightMost = q[-1][1]
            maxi = max(maxi, rightMost-leftMost+1)    
            qLen = len(q)
            for i in range(qLen):
                node, i = q.popleft()
                if node.left:
                    q.append((node.left, 2*i+1))
                if node.right:
                    q.append((node.right, 2*i+2))
        return maxi
        
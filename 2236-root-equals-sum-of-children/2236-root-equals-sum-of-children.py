# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        q = deque()
        q.append(root)
        # level = 

        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()

                if not node.left and not node.right:
                    continue

                num1 = node.left.val if node.left else 0
                num2 = node.right.val if node.right else 0

                if node.val != num1 + num2:
                    return False
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return True
            

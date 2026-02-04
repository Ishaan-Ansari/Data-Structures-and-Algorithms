# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.cnt = 0

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if not level:
                continue
                
            if self.cnt % 2 == 0:
                self.res.append(level)
            else:
                level.reverse()
                self.res.append(level)

            self.cnt += 1

        return self.res
            

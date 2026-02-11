# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _check(self, arr: List[int]) -> bool:
        left, right = 0, len(arr)-1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else: # Record the 'None' to preserve structure
                    level.append(None)

            if level:
                if not self._check(level):
                    return False

        return True
                        

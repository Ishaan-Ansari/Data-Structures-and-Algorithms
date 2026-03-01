# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1+self.countNodes(root.left)+self.countNodes(root.right)

        # res = []
        # q = collections.deque()
        # q.append(root)

        # while q:
        #     level = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         res.append(level)

        # ans = 0
        # for i in res:
        #     ans += len(i)

        # return ans
        
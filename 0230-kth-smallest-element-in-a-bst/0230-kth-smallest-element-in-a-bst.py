# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.result = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        self.inorder(root, k)

        return self.result

    def inorder(self, root, k):
        """Since we're traversing inorder we just need to keep a track of counter"""
        # Base case: if node is null, or if we ALREADY found the result, stop.
        if not root or self.result is not None:
            return

        self.inorder(root.left, k)

        self.count += 1
        if self.count == k:
            self.result = root.val
            return

        self.inorder(root.right, k)
        

# class Solution:
#     def __init__(self):
#         self.nums = []

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         if not root:
#             return 0

#         self.inorder(root)

#         return self.nums[k-1]

#     def inorder(self, root):
#         """In BST inorder traversal gives sorted array"""
#         if not root:
#             return

#         self.inorder(root.left)
#         self.nums.append(root.val)
#         self.inorder(root.right)
        
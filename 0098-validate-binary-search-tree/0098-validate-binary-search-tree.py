# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low = -math.inf, high = math.inf):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            # Check the left subtree
            validate_left_subtree = validate(node.left, low, node.val)

            # Check right sub tree
            validate_right_subtree = validate(node.right, node.val, high)

            return validate_left_subtree and validate_right_subtree
        
        return validate(root)

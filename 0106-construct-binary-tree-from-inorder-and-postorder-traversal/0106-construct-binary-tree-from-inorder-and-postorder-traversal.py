# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None

        # Get the root from post-order
        root = TreeNode(postorder[-1])

        # Identitfy from where the tree is to be splitted
        mid = inorder.index(postorder[-1])

        # Take the first nodes
        root.left = self.buildTree(inorder[:mid], postorder[:mid])

        # Start after the left subtree's nodes, and stop BEFORE the last element (which was our root).
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        return root
        
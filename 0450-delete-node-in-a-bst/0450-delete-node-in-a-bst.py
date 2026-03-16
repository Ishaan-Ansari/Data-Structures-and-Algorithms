# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 3: Node has 2 children
            # Find the inorder successor (smallest node in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Replace current node's value with the successor's value
            root.val = curr.val

            root.right = self.deleteNode(root.right, root.val)

        return root
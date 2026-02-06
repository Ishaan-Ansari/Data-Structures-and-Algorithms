'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def __init__(self):
        self.res = []

    def left_tree(self, root):
        if not root:
            return 
        
        if not root.left and not root.right:
            return
        
        self.res.append(root.data)
        if not root.left:
            self.left_tree(root.right)
            
        else:
            self.left_tree(root.left)
        
    def leaf_nodes(self, root):
        if not root:
            return 
        
        if not root.left and not root.right:
            self.res.append(root.data)
        
        self.leaf_nodes(root.left)
        self.leaf_nodes(root.right)
        
    def right_tree(self, root):
        if not root:
            return 
        
        if not root.left and not root.right:
            return
        

        if not root.right:
            self.right_tree(root.left)
        else:
            self.right_tree(root.right)
            
        self.res.append(root.data)
        
    def boundaryTraversal(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.data]

            
        self.res.append(root.data)
            
        self.left_tree(root.left)
        self.leaf_nodes(root)
        self.right_tree(root.right)

        return self.res
        
        
        

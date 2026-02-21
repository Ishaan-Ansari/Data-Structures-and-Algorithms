# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        self.visited = set()

    def solve(self, root, d, k): # Here root is target node
        if not root or root in self.visited:
            return

        self.visited.add(root)
        
        if d == k:
            self.res.append(root.val)
        else:
            self.solve(root.left, d+1, k)
            self.solve(root.right, d+1, k)
            self.solve(root.parent, d+1, k)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        # DFS to attach a 'parent' attribute to every node
        def add_parent(node, parent=None):
            if node:
                node.parent = parent
                add_parent(node.left, node)
                add_parent(node.right, node)

        add_parent(root)

        self.solve(target, 0, k)

        return self.res
        
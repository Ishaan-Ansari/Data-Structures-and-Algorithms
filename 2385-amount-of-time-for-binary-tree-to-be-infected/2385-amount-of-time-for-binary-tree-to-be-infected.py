# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:     
        if not root:
            return 0

        start_node = None

        def add_parent(node, parent=None):
            nonlocal start_node

            if not node:
                return 

            node.parent = parent

            if node.val == start:
                start_node = node
        
            add_parent(node.left, node)
            add_parent(node.right, node)

        add_parent(root)

        queue = deque([(start_node, 0)])

        visited = {start_node}
        max_minutes = 0

        while queue:
            current, minutes = queue.popleft()
            max_minutes = max(max_minutes, minutes)

            directions = [current.left, current.right, getattr(current, 'parent', None)]

            for neighbor in directions:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, minutes+1))


        return max_minutes
        
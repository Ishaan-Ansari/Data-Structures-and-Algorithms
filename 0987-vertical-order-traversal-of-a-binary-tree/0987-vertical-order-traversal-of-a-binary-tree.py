# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # The 'node_list' will store tuples: (column, row, value)
        node_list = []

        def dfs(node, col, row):
            if not node:
                return 
            
            node_list.append((col, row, node.val))

            dfs(node.left, col-1, row+1)
            dfs(node.right, col+1, row+1)

        dfs(root, 0, 0)

        node_list.sort()

        column_table = defaultdict(list)
        for col, row, val in node_list:
            column_table[col].append(val)

        
        return list(column_table.values())


        
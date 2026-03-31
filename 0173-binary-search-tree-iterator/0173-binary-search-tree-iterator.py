# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self._push_left(root)

    def _push_left(self, root: Optional[TreeNode]):
        while root is not None:
            self.arr.append(root)
            root = root.left

    def next(self) -> int:
        top_node = self.arr.pop()

        if top_node.right:
            self._push_left(top_node.right)
        
        return top_node.val
        
    def hasNext(self) -> bool:
        return len(self.arr) > 0

    # def __init__(self, root: Optional[TreeNode]):
    #     self.sorted_values = []
    #     self.index = -1
        
    #     self._inorder_traversal(root)

    # def _inorder_traversal(self, root: Optional[TreeNode]):
    #     if not root:
    #         return 
        
    #     self._inorder_traversal(root.left)
    #     self.sorted_values.append(root.val)
    #     self._inorder_traversal(root.right)

    # def next(self) -> int:
    #     self.index += 1
    #     return self.sorted_values[self.index]

    # def hasNext(self) -> bool:
    #     return (self.index+1) < len(self.sorted_values)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
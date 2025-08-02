"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return head

        orig_to_clone = {}
        curr = head

        while curr:
            orig_to_clone[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            clone = orig_to_clone[curr]
            clone.next = orig_to_clone.get(curr.next)
            clone.random = orig_to_clone.get(curr.random)
            curr = curr.next

        return orig_to_clone[head]

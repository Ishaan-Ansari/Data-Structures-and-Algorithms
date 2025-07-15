# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev      

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return head
        
    #     stack = deque()

    #     curr = head
    #     while curr:
    #         stack.append(curr.val)
    #         curr = curr.next

    #     curr = head
    #     while stack:
    #         curr.val = stack.pop()
    #         curr = curr.next

    #     return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def _reverse_ll(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dq = deque()
        curr = head 

        while curr:
            dq.append(curr.val)
            curr = curr.next

        curr = head

        while curr:
            curr.val = dq.pop()            
            curr = curr.next

        return head
    
    def _remove_node_at_idx(self, head: Optional[ListNode], idx: int) -> Optional[ListNode]:
        if head is None or idx < 0:
            return head

        if idx == 0:
            return head.next

        prev, curr = head, head.next
        pos = 1

        while curr and pos<idx:
            prev = curr
            curr = curr.next
            pos += 1
        
        if curr is None:    # out of bounds
            return head

        prev.next = curr.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self._reverse_ll(head)
        head = self._remove_node_at_idx(head, n-1)
        head = self._reverse_ll(head)

        return head

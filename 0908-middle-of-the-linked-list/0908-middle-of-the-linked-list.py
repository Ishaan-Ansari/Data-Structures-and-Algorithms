# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty or single node
        if head is None or head.next is None:
            return head

        slow = head
        fast = head

        # Here we've to consider both the cases 
        while fast is not None  and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

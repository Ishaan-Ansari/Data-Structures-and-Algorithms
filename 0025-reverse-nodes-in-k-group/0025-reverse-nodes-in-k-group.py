# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = tail = ListNode(0)
        curr = head
        lst = []

        while curr:
            lst.append(curr.val)
            if len(lst) == k:
                for num in reversed(lst):
                    tail.next = ListNode(num)
                    tail = tail.next
                lst.clear()
            curr = curr.next

        for num in lst:
            tail.next = ListNode(num)
            tail = tail.next

        return dummy.next

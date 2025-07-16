# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = fast =head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast: break
        else: return None
    
        ptr1, ptr2 = head, slow

        while ptr1 is not ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next

        return ptr1


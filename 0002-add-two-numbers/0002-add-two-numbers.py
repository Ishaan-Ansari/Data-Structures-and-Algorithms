# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2

        dummy = tail = ListNode(0)
        c1, c2  = l1, l2
        carry = 0

        while c1 or c2 or carry:
            x = c1.val if c1 else 0
            y = c2.val if c2 else 0
            sum = x + y + carry
            carry = sum//10

            tail.next = ListNode(sum % 10)
            tail = tail.next
            
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

        return dummy.next
        
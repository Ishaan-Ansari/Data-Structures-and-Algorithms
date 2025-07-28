# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverse_ll(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

    def addOne(self, head): 
        if head is None:
            return None
        
        rev_head = self._reverse_ll(head)

        curr = rev_head
        carry = 1
        prev = None

        while curr and carry:
            s = curr.val + carry
            curr.val = s % 10
            carry = s // 10
            prev = curr
            curr = curr.next

        if carry:
            prev.next = ListNode(carry)
        
        return self._reverse_ll(rev_head)
        

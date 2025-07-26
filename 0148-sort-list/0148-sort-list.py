# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        
        lst = []
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next

        # lst = sorted(lst)
        lst.sort()

        curr = head
        for num in lst:
            curr.val = num
            curr = curr.next
        
        return head

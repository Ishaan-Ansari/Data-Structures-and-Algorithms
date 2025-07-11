# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # list is emprt or it has single node
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

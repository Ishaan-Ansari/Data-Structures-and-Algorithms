# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:   # empty or single node
            return head

        lst = [] # initialize a empty list
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next

        curr = head
        for i in range(0, len(lst), 2):
            curr.val = lst[i]
            curr = curr.next

        for i in range(1, len(lst), 2):
            curr.val = lst[i]
            curr = curr.next

        return head

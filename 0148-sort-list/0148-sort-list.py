# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left, right = self._split_list(head)

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return self._merge_list(left_sorted, right_sorted)

    def _split_list(self, head: Optional[ListNode]) -> tuple[ListNode, ListNode]:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        return head, mid

    def _merge_list(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(0)  # dummy node init to 0
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # Advance tail to the node we just added
            tail = tail.next

        # Whichever list still has nodes can just be tacked on.
        tail.next = l1 or l2
        return dummy.next

#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head 
        
#         lst = []
#         curr = head

#         while curr:
#             lst.append(curr.val)
#             curr = curr.next

#         # lst = sorted(lst)
#         lst.sort()

#         curr = head
#         for num in lst:
#             curr.val = num
#             curr = curr.next
        
#         return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        l1, l2 = headA, headB

        while l1 is not l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1

        # l1 = headA

        # while l1:
        #     l2 = headB
        #     while l2:
        #         if l1 is l2:
        #             return l1
        #         l2 = l2.next
        #     l1 = l1.next
        
        # return None
            
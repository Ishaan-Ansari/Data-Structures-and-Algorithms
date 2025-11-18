import heapq as hp
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        hq = []
        
        for head in lists:
            current = head
         
            while current is not None:
                hp.heappush(hq, current.val)
                current = current.next

        dummy = ListNode(0)
        tail = dummy

        while len(hq) > 0:
            val = hp.heappop(hq)
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next




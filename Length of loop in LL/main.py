# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        if head is None: # list is empty
            return 0
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break   # slow -> start of the loop

        else:       # else fast hits None
            return 0

        count = 1
        fast = fast.next        # initialize with start

        while slow != fast:
            count += 1
            fast = fast.next

        return count

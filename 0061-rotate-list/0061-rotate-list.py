# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate(self, arr: list) -> list:
        temp = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp
        return arr
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        k = k % len(arr)  

        for _ in range(k):
            arr = self.rotate(arr)

        dummy = tail = ListNode(0)

        for num in arr:
            tail.next = ListNode(num)
            tail = tail.next

        return dummy.next

        
        
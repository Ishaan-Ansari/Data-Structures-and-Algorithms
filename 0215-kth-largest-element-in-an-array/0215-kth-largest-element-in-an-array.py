import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1.... Sort and return
        # TC - NLogN
        # ---------------------------------

        n = len(nums)
        if not nums:
            return 0

        # nums.sort()
        # return nums[n - k]

        # To make it max heap simply reverse the sign
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        KthMaxi = None
        for _ in range(k):
            KthMax = heapq.heappop(max_heap)

        return -KthMax





import sys

class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N-1
        ans = sys.maxsize

        while left<=right:
            mid = left + (right-left)//2
            if nums[left] <= nums[mid]:
                ans = min(ans, nums[left])
                left = mid+1
            else:
                ans = min(ans, nums[mid])
                right = mid-1

        return ans
        
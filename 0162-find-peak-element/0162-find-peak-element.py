class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[N-1] > nums[N-2]:
            return N-1

        left, right = 1, N-2

        while left <= right:
            mid = left+(right-left)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid

            if nums[mid]>nums[mid-1]:
                left = mid+1
            
            else:
                right = mid-1

        return -1
        